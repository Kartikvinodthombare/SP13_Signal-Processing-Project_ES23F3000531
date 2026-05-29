from flask import Flask, request, render_template, redirect, url_for
import cv2
import numpy as np
import os

app = Flask(__name__)
os.makedirs('static', exist_ok=True) 

def calculate_metrics(original, filtered):
    mse = np.mean((original.astype("float") - filtered.astype("float")) ** 2)
    if mse == 0:
        return 0.0, 100.0 
    psnr = 10 * np.log10((255 ** 2) / mse)
    return round(mse, 2), round(psnr, 2)

@app.route('/', methods=['GET', 'POST'])
def home():
    if request.method == 'POST':
        ksize = int(request.form['ksize'])       
        lap_mode = request.form['lap_mode']      
        
        if ksize % 2 == 0:
            ksize += 1

        file = request.files.get('image') 
        filepath = os.path.join('static', 'uploaded.jpg')

        if file and file.filename != '':
            file.save(filepath)

        if not os.path.exists(filepath):
            return render_template('index.html', processed=False, error="Please upload an image first.")

        img = cv2.imread(filepath)
        cv2.imwrite('static/color.jpg', img)

        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        cv2.imwrite('static/gray.jpg', gray)

        mean_img = cv2.blur(gray, (ksize, ksize))
        cv2.imwrite('static/mean.jpg', mean_img)

        gauss_img = cv2.GaussianBlur(gray, (ksize, ksize), 0)
        cv2.imwrite('static/gauss.jpg', gauss_img)

        if lap_mode == 'sharpen':
            kernel = np.array([[0, -1, 0], [-1, 5, -1], [0, -1, 0]])
            lap_img = cv2.filter2D(gray, -1, kernel)
        else:
            kernel = np.array([[0, -1, 0], [-1, 4, -1], [0, -1, 0]])
            lap_img = cv2.filter2D(gray, -1, kernel)
            
        cv2.imwrite('static/laplacian.jpg', lap_img)

        mean_mse, mean_psnr = calculate_metrics(gray, mean_img)
        gauss_mse, gauss_psnr = calculate_metrics(gray, gauss_img)
        lap_mse, lap_psnr = calculate_metrics(gray, lap_img)

        return render_template('index.html', 
                               processed=True, 
                               current_ksize=ksize, 
                               current_lap=lap_mode.title(),
                               mean_mse=mean_mse, mean_psnr=mean_psnr,
                               gauss_mse=gauss_mse, gauss_psnr=gauss_psnr,
                               lap_mse=lap_mse, lap_psnr=lap_psnr) 

    return render_template('index.html', processed=False)

# NEW: The Clear App function
@app.route('/clear')
def clear_app():
    # Find the uploaded image
    filepath = os.path.join('static', 'uploaded.jpg')
    # If it exists, delete it from the hard drive
    if os.path.exists(filepath):
        os.remove(filepath)
    # Send the user back to the default home page
    return redirect(url_for('home'))

if __name__ == '__main__':
    app.run(debug=True)