import streamlit as st
import numpy as np
from PIL import Image
from detection.object_detection import detect_object

# Application UI Parameters for streamlit to modify the default UI contents.
MAX_WIDTH = 1200
padding_top = 0
st.markdown(f"""<style>
.reportview-container .main .block-container{{
    max-width: {MAX_WIDTH}px;
    padding-top: {padding_top}rem;
    }}
</style>""",unsafe_allow_html=True,)
st.markdown(
    """
<style>
.sidebar .sidebar-content {
    background-image: linear-gradient(#FFFFFF,#FFFFFF);
    color: black;
}
</style>
""",
    unsafe_allow_html=True,
)

st.set_option('deprecation.showPyplotGlobalUse', False)
st.set_option('deprecation.showfileUploaderEncoding', False)

def local_css(file_name):
    with open(file_name) as f:
        st.markdown(f'<style>{f.read()}</style>', unsafe_allow_html=True)

local_css("css/style.css")

#  Application Title and Image for the application
st.sidebar.image("images/pwc-logo-dark.png", caption=None, width=80, use_column_width=False)
st.sidebar.title("Sign & Signspot Detection")


showWarningOnDirectExecution = False
st.set_option('deprecation.showfileUploaderEncoding', False)
def main():
    st.title("Sign & Signspot Detection")
    

    app_choice = st.sidebar.radio("Approaches", ["Yolo OD Model", "Hybrid - Contor + OD"])

    if app_choice is not None:
        img_array = upload_image_ui()
        if img_array is not None:
            image = detect_object(img_array)
            st.image(image)

def upload_image_ui():
    uploaded_image = st.sidebar.file_uploader("Please choose an image file", type=["png", "jpg", "jpeg"])
    if uploaded_image is not None:
        try:
            image = Image.open(uploaded_image)
        except Exception:
            st.error("Error: Invalid image")
        else:
            img_array = np.array(image)
            return img_array

if __name__ == '__main__':
    main()
