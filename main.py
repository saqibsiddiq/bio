import numpy as np
import matplotlib.pyplot as plt
from skimage import io, color, measure
from skimage.segmentation import clear_border
from skimage.morphology import binary_erosion, binary_dilation, disk
from skimage.measure import regionprops
from skimage.filters import threshold_otsu

# Load the genomic image (replace 'your_image_path.png' with the actual path to your image)
image_path = 'gnome.png'
genomic_image = io.imread(image_path)

# Convert the image to grayscale, ignoring alpha channel if present
gray_image = color.rgb2gray(genomic_image[:, :, :3])  # Use only the first three channels (RGB)

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

# Display the original image, binary image, and labeled image
fig, axes = plt.subplots(1, 3, figsize=(12, 4))
axes[0].imshow(genomic_image)
axes[0].set_title('Original Image')

axes[1].imshow(binary_image, cmap='gray')
axes[1].set_title('Binary Image')

axes[2].imshow(labeled_image, cmap='nipy_spectral')
axes[2].set_title('Labeled Image')

plt.show()

