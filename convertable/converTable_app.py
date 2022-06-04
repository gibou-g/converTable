import streamlit as st
from PIL import Image, ImageEnhance, ImageOps
from re import search
import cv2 as cv
import numpy as np

#
#     TODO:
#         - add adaptive mean and gaussian thresholding using cv
#         - refactor

#

if __name__ == "__main__":
    logo = Image.open("doc/logos/converTable logo.png")
    st.image(logo)
    st.title("ConverTable")
    desc = """
        An app to convert tabular data on images to DataFrames. \n
        Upload an image to get started. Use the sidebar to configure
        image and table settings.
    """
    st.write(desc)

    # sidebar
    with st.sidebar:
        st.header("Image settings")
        img_size = st.selectbox(
            "Preview size", ["256x256", "512x512", "720x720", "1024x1024"]
        )
        brightness = st.slider("Adjust brigtness", 0, 100)
        sharpness = st.slider("Sharpen", 0, 2)
        threshold_method = st.selectbox(
            "Threshold method", [None, "Adaptive Mean", "Adaptive Gaussian"]
        )
        greyscale = st.checkbox("Convert to greyscale?")

        apply = st.button("Apply")
        reset = st.button("Reset")

        st.header("Table settings")
        st.number_input(
            "Number of rows to show in preview (default = 5, max = 20)", 5, 20
        )
        table_info = st.checkbox("Show table info?")

    input_file = st.file_uploader("Upload Image")

    # add columns here: 1 for image preview and the other
    # for what pdfplumber extracts from file
    col1, col2 = st.columns(2)

    if apply:
        with col1:
            if input_file:
                input_img = Image.open(input_file)
                if greyscale:
                    input_img = ImageOps.grayscale(input_img)

                st.header("Image preview")
                resize_val = int(search("\d+", img_size).group(0))
                input_img = ImageEnhance.Brightness(input_img).enhance(
                    factor=brightness / 100
                )
                input_img = ImageEnhance.Sharpness(input_img).enhance(factor=sharpness)

                preview_img = input_img.resize((resize_val, resize_val))

                # show preview
                st.image(preview_img)
    elif reset:  # undo everything
        st.experimental_rerun()

    outfile = st.selectbox("Export", ["CSV", "Google Sheets"])

    if outfile.startswith("Google"):
        st.text_input("Input public Google sheets URL")  # currently does nothing:
        # if exception occurs, download csv instead
    else:
        pass
        # st.download_button('Download DataFrame', out_data)
