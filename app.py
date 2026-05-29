from flask import Flask, request, render_template
import cv2
import numpy as np
import os

app = Flask(__name__)
os.makedirs('static', exist_ok=True) 

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

        # --- B. PROCESS THE IMAGE ---
        img = cv2.imread(filepath)
        
        # NEW: Save the original color image before doing anything else
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

        return render_template('index.html', 
                               processed=True, 
                               current_ksize=ksize, 
                               current_lap=lap_mode.title()) 

    return render_template('index.html', processed=False)

if __name__ == '__main__':
    app.run(debug=True)