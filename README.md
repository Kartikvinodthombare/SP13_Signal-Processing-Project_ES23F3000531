# Image Filter Lab (SP13)

**Signal Processing Project: Image Smoothing and Sharpening**

A lightweight, interactive web application built with Python and OpenCV to demonstrate fundamental 2D signal processing concepts. This application allows users to upload an image and instantly apply spatial filters — Mean, Gaussian, and Laplacian — to observe how matrix convolution affects visual data.

---

## Tech Stack

- **Backend:** Python, Flask, OpenCV (`cv2`), NumPy
- **Frontend:** HTML5, CSS3 (Flexbox)
- **Architecture:** Client-Server model

---

## Features

- **Grayscale Conversion:** Automatically simplifies 3-channel color images into 1-channel arrays for processing.
- **Low-Pass Filtering (Blurring):**
  - **Mean Filter:** Uniform averaging for basic smoothing.
  - **Gaussian Filter:** Bell-curve weighted averaging for natural, photographic blurring.
- **High-Pass Filtering (Edge Detection):**
  - **Laplacian Filter:** Second-order derivative spatial operator. Includes both an Edge Map mode and a Sharpened mode.
- **Dynamic Kernel Sizes:** Users can adjust the convolution matrix size from 3x3 up to 99x99.
- **Smart Caching:** Process different filters on the same image without re-uploading the file each time.

---

## Installation and Setup

### Prerequisites

Make sure you have **Python** installed on your system. You can download it from [python.org](https://www.python.org/).

### 1. Install Dependencies

Open your terminal and run:

```bash
pip install flask opencv-python numpy
```

### 2. Run the Application

Navigate to your project folder in the terminal and run:

```bash
python app.py
```

Once the server is running, open your browser and go to:

```
http://127.0.0.1:5000
```

---

## Usage

1. Open the web app in your browser.
2. Upload a test image.
3. Select a kernel size (must be an odd number, e.g., 3, 5, 15).
4. Choose the Laplacian mode: Sharpened or Edge Map.
5. Click **Apply Filters**.
6. Scroll down to view and download your results.

---

## Author

| Field | Details |
|---|---|
| Name | Kartik Vinod Thombare |
| Roll Number | ES23F3000531 |
| Course / Project | SP13 — Signal Processing |
| Institute | Indian Institute of Technology Madras (BS Electronic Systems) |
