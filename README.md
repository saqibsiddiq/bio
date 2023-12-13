# Genomic Image Analysis Streamlit App

## Overview
This Streamlit app allows users to upload genomic images, perform image analysis, and visualize the results interactively. The app analyzes the uploaded image by converting it to grayscale, applying thresholding, and labeling connected components.

## Features
- Upload genomic images (JPEG, JPG, PNG).
- Display the uploaded genomic image.
- Perform image analysis including:
  - Conversion to grayscale.
  - Otsu's thresholding.
  - Binary image cleanup.
  - Labeling connected components.
- Display grayscale, binary, and labeled images with interactive plots.

## How to Use
1. Clone the repository to your local machine.
2. Install the required dependencies:
   ```bash
   pip install streamlit numpy scikit-image matplotlib
