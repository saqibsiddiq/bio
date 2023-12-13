import streamlit as st
import numpy as np
import matplotlib.pyplot as plt
from skimage import io, color, measure
from skimage.segmentation import clear_border
from skimage.morphology import binary_erosion, binary_dilation, disk
from skimage.measure import regionprops
from skimage.filters import threshold_otsu

def perform_image_analysis(image):
    # Convert the image to grayscale, ignoring alpha channel if present
    gray_image = color.rgb2gray(image[:, :, :3])  # Use only the first three channels (RGB)

    # Apply Otsu's thresholding to segment the image
    threshold_value = threshold_otsu(gray_image)
    binary_image = gray_image > threshold_value

    # Clean up the binary image
    binary_image = clear_border(binary_image)
    binary_image = binary_erosion(binary_image, disk(2))
    binary_image = binary_dilation(binary_image, disk(5))

    # Label connected components in the binary image
    labeled_image = measure.label(binary_image)

    # Measure properties of labeled regions
    regions = regionprops(labeled_image)

    # Extract features from the regions (for demonstration, we'll print the area of each region)
    for region in regions:
        print(f"Region Area: {region.area}")

    return gray_image, binary_image, labeled_image

def main():
    st.title("Genomic Image Analysis with Streamlit")

    # Upload image through Streamlit
    uploaded_file = st.file_uploader("Choose a genomic image...", type=["jpg", "jpeg", "png"])

    if uploaded_file is not None:
        # Display the uploaded image
        image = io.imread(uploaded_file)
        st.image(image, caption="Uploaded Genomic Image", use_column_width=True)

        # Perform image analysis
        gray_image, binary_image, labeled_image = perform_image_analysis(image)

        # Display results
        st.subheader("Grayscale Image")
        plt.imshow(gray_image, cmap='gray')
        st.pyplot()

        st.subheader("Binary Image")
        plt.imshow(binary_image, cmap='gray')
        st.pyplot()

        st.subheader("Labeled Image")
        plt.imshow(labeled_image, cmap='nipy_spectral')
        st.pyplot()

if __name__ == "__main__":
    main()

     

