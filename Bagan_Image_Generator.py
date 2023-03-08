import streamlit as st
from PIL import Image
import base64


def add_bg_from_local(image_file):
    with open(image_file, "rb") as image_file:
        encoded_string = base64.b64encode(image_file.read())
    st.markdown(
        f"""
    <style>
    .stApp {{
        background-image: url(data:image/{"jpg"};base64,{encoded_string.decode()});
        background-size: cover;
        opacity: 0.9;

        
    }}

    </style>
    """,
        unsafe_allow_html=True
    )


def about_page():
    add_bg_from_local("image/background2.png")

    original_title = '<b><p style="font-family:Optima;  font-size: 40px;text-align:center">Bagan Image Generator(BIG)</p></b>'
    st.markdown(original_title, unsafe_allow_html=True)
    
    st.header(" Team BIG 	:robot_face: ")
    members = '<ul style="list-style-type:square"><li style=" font-size: 20px;">Bhone Myint Swe</li><li style=" font-size: 20px;">Min Thaw Phyo</li></ul><br/>'
    st.markdown(members, unsafe_allow_html=True)
    st.subheader("About This Project:dart:")

    about = '<p style=" font-size: 20px;">The Bagan Image Generating GAN project is an image generation project that uses Generative Adversarial Networks (GANs) to produce images of the ancient pagodas of Bagan, located in Myanmar. The project was developed by Team GAN</p><br/>'
    st.markdown(about, unsafe_allow_html=True)
    col1, col2, col3 = st.columns(3)

    with col1:
        image = Image.open("image/baganImg1.jpg")
        st.image(image)

    with col2:
        image = Image.open("image/baganImg2.jpg")
        st.image(image)

    with col3:
        image = Image.open("image/baganImg3.jpg")

        st.image(image)


def gan_model_1_page():
    add_bg_from_local("image/background2.png")
    st.title('Comparsing Between Original Images and Generated Images')
    # data set 4 pone normal image ko pya gif nhk generated phit tk hr ko pya

    col1, col2 = st.columns(2)
    with col1:
        original_image_title = '<p style=" font-size: 20px; text-align:center">Original Images(128x128)</p>'
        st.markdown(original_image_title, unsafe_allow_html=True)
        st.write('')
        st.write('')
        col11, col12, col13 = st.columns(3)
        with col11:
            st.write('')
        with col12:

            image = Image.open(
                "image/original_img1.png")
            st.image(image)
            st.write('')
            st.write('')
            image1 = Image.open(
                "image/original_img2.png")
            st.image(image1)
        with col13:
            st.write('')

    with col2:
        original_image_title1 = '<p style=" font-size: 20px; text-align:center">Generated Images(128x128)</p>'
        st.markdown(original_image_title1, unsafe_allow_html=True)
        st.write('')
        st.write('')

        col21, col22, col23 = st.columns(3)

        with col21:
            st.write('')

        with col22:

            image = Image.open(
                "image/generated_image1.jpg")
            st.image(image)
            st.write('')
            st.write('')
            image = Image.open(
                "image/generated_image2.jpg")
            st.image(image)
        with col23:
            st.write('')


def app():

    st.set_page_config(page_title='GAN App', layout='wide')
    st.sidebar.title('Navigation:gear:')
    pages = {'Home Page ': about_page, 'GAN Model': gan_model_1_page}
    page = st.sidebar.radio('Select a page', list(pages.keys()))
    pages[page]()


if __name__ == '__main__':
    app()
