from PIL import Image, ImageEnhance, ImageOps, ImageFilter
import streamlit as st
import numpy as np
import io

# Set page config for wide layout (optional but recommended)
st.set_page_config(layout="wide")

st.title('PhotoEditor')

# Create columns for cleaner layout
col1, col2, col3 = st.columns([1, 3, 1.5])  # Adjust the width of col1 as needed

# Define the list of filters
filters = [
    "Original",
    "Blur",
    "Sharpen",
    "Grayscale",
    "Sepia",
    "Edge Detection",
    "Emboss",
    "Invert Colors",
    "Brightness Adjustment",
    "Contrast Adjustment",
    "Saturation Adjustment",
    "Gaussian Blur",
    "Box Blur",
    "Motion Blur",
    "Median Filter"
]

# Content for each column, with placeholders for menu items and image input
with col1:
    st.subheader("Menu")

    # Filter Names (using st.write or st.selectbox)
    st.write("Filters:")
    selected_filter = st.selectbox("Choose Filter", filters)
    
    # Slider for filter value (if applicable)
    if selected_filter in ["Brightness Adjustment", "Contrast Adjustment", "Saturation Adjustment"]:
        filter_value = st.slider("Adjust Value", min_value=1, max_value=100, value=50)
    
    # Slider for flipping image
    flip_value = st.slider("Flip Image", min_value=0, max_value=1, step=1)
    
    # Slider for rotating image
    rotate_value = st.slider("Rotate Image", min_value=0, max_value=360, step=1)
    
    # Cropping sliders
  
with col2:
    st.subheader("Output")
    # Add functionalities for image processing and displaying results here
    st.write(f"Filter Applied : {selected_filter}")

    # Display uploaded image if it exists
    uploaded_file = st.session_state.get('uploaded_file')
    if uploaded_file:
        # Convert uploaded image to PIL Image
        pil_image = Image.open(uploaded_file)
        
        # Flip the image based on flip_value
        if flip_value == 1:
            pil_image = ImageOps.flip(pil_image)
        
        # Rotate the image based on rotate_value
        pil_image = pil_image.rotate(rotate_value, expand=True)

        # Apply selected filter if applicable
        if selected_filter == "Original":
            st.image(np.array(pil_image), caption="Original Image")
        elif selected_filter == "Blur":
            # Apply blur filter
            filtered_image = pil_image.filter(ImageFilter.BLUR)
            st.image(filtered_image, caption="Blurred Image")
        elif selected_filter == "Sharpen":
            # Apply sharpen filter
            filtered_image = pil_image.filter(ImageFilter.SHARPEN)
            st.image(filtered_image, caption="Sharpened Image")
        elif selected_filter == "Grayscale":
            # Convert to grayscale
            filtered_image = pil_image.convert('L')
            st.image(filtered_image, caption="Grayscale Image")
        elif selected_filter == "Sepia":
            # Convert to sepia tone
            filtered_image = ImageOps.colorize(pil_image.convert('L'), (210, 180, 140), (255, 255, 255))
            st.image(filtered_image, caption="Sepia Image")
        elif selected_filter == "Edge Detection":
            # Apply edge detection
            filtered_image = pil_image.filter(ImageFilter.FIND_EDGES)
            st.image(filtered_image, caption="Edge Detection")
        elif selected_filter == "Emboss":
            # Apply emboss filter
            filtered_image = pil_image.filter(ImageFilter.EMBOSS)
            st.image(filtered_image, caption="Embossed Image")
        elif selected_filter == "Invert Colors":
            # Invert colors
            filtered_image = ImageOps.invert(pil_image)
            st.image(filtered_image, caption="Inverted Colors")
        elif selected_filter == "Brightness Adjustment":
            # Adjust brightness
            enhancer = ImageEnhance.Brightness(pil_image)
            filtered_image = enhancer.enhance(filter_value / 50)  # Adjust enhancement factor as needed
            st.image(filtered_image, caption="Brightness Adjusted Image")
        elif selected_filter == "Contrast Adjustment":
            # Adjust contrast
            enhancer = ImageEnhance.Contrast(pil_image)
            filtered_image = enhancer.enhance(filter_value / 50)  # Adjust enhancement factor as needed
            st.image(filtered_image, caption="Contrast Adjusted Image")
        elif selected_filter == "Saturation Adjustment":
            # Adjust saturation
            enhancer = ImageEnhance.Color(pil_image)
            filtered_image = enhancer.enhance(filter_value / 50)  # Adjust enhancement factor as needed
            st.image(filtered_image, caption="Saturation Adjusted Image")
        elif selected_filter == "Gaussian Blur":
            # Apply Gaussian blur
            filtered_image = pil_image.filter(ImageFilter.GaussianBlur(radius=2))  # Adjust radius as needed
            st.image(filtered_image, caption="Gaussian Blurred Image")
        elif selected_filter == "Box Blur":
            # Apply Box blur
            filtered_image = pil_image.filter(ImageFilter.BoxBlur(radius=2))  # Adjust radius as needed
            st.image(filtered_image, caption="Box Blurred Image")
        elif selected_filter == "Motion Blur":
            # Apply Motion blur
            kernel = ImageFilter.Kernel((3, 3), [1, 0, -1, 1, 0, -1, 1, 0, -1], scale=1)
            filtered_image = pil_image.filter(kernel)
            st.image(filtered_image, caption="Motion Blurred Image")
        elif selected_filter == "Median Filter":
            # Apply Median filter
            filtered_image = pil_image.filter(ImageFilter.MedianFilter(size=3))  # Adjust size as needed
            st.image(filtered_image, caption="Median Filtered Image")

with col3:
    st.subheader("Image")
    uploaded_file = st.file_uploader("Upload Image", type=["jpg", "png", "jpeg"])
    # Store uploaded image in session state
    if uploaded_file is not None:
        st.session_state.uploaded_file = uploaded_file
    # Display uploaded image if it exists
    if uploaded_file:
        st.image(uploaded_file, caption="Uploaded Image")
