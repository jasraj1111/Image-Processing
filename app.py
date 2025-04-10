import streamlit as st
import cv2
from script1 import display_image
from script1 import resize_image
from script1 import convert_to_grayscale
from script2 import plot_histogram
from script2 import contrast_stretching
from script2 import thresholding
from script2 import graylevel_slicing
from script2 import bit_plane_slicing
from script2 import smoothen_image
from PIL import Image
import numpy as np

st.set_page_config(page_title="Image Processing Suite", layout="wide")

st.title("🖼️ Image Processing with OpenCV + Streamlit")

# Image selection
image_option = st.selectbox("Choose an image to process:", ("pic_1.jpg", "pic_2.jpg"))
img = cv2.imread(image_option)  # This loads it in BGR (default)
img_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)  # Convert to RGB for Streamlit
st.image(img_rgb, caption="Original Image", use_column_width=True)


# Operation choice
option = st.selectbox(
    "Choose an operation:",
    [
        "None",
        "Dlsplay Image",
        "Resize image",
        "Convert to Grayscale",
        "Grayscale Histogram",
        "Contrast Stretching",
        "Thresholding",
        "Graylevel Slicing",
        "Bit Plane Slicing",
        "Smoothen Image using a 3x3 Kernel"
    ]
)

if option != "None":
    if option == "Grayscale Histogram":
        plot_histogram(img)
        st.pyplot()
        

    elif option == "Contrast Stretching":
        stretched = contrast_stretching(img)  # for example
        st.image(stretched, caption="Contrast Stretched", channels="GRAY")

    elif option == "Thresholding":
        thresh = thresholding(img)
        st.image(thresh, caption="Thresholded Image", channels="GRAY")
    
    elif option == "Graylevel Slicing":
        lower = st.number_input("Enter lower bound (0-255):", 0, 255, 100)
        upper = st.number_input("Enter upper bound (0-255):", 0, 255, 150)
        sliced = graylevel_slicing(img, lower, upper)
        st.image(sliced, caption=f"Graylevel Slicing ({lower}-{upper})", channels="GRAY")

    elif option == "Bit Plane Slicing":
        planes = bit_plane_slicing(img)
        for i, plane in enumerate(planes):
            st.image(plane, caption=f"Bit Plane {i}", channels="GRAY")

    elif option == "Smoothen Image using a 3x3 Kernel":
        smoothed = smoothen_image(img)
        st.image(smoothed, caption="Smoothed Image using 3x3 Kernel", channels="GRAY")

    elif option == "Display Image":
        display_image("Original Image", img)
        st.image(img, caption="Original Image", channels="GRAY")

    elif option == "Resize image":
        scale_percent = st.slider("Resize percentage:", 10, 100, 50)
        resized = resize_image(img, scale_percent)
        st.image(resized, caption=f"Resized Image ({scale_percent}%)")
    
    elif option == "Convert to Grayscale":
        gray = convert_to_grayscale(img)
        st.image(gray, caption="Grayscale Image", channels="GRAY")