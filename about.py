import streamlit as st
import pandas as pd

def app():
    # st.write('about')
#background image
    import base64 
    def add_bg_from_local(image_file):
            with open(image_file, "rb") as image_file:
                encoded_string = base64.b64encode(image_file.read())
            st.markdown(
                f"""
                <style>
                .stApp {{
                    background-image: url(data:image/{"png"};base64,{encoded_string.decode()});
                    background-size: cover
                }}
                </style>
                """,
                unsafe_allow_html=True
                )
    add_bg_from_local('the2.jpeg') 

    st.title("About The Shield")
    st.write("<h6 style='font-weight: bold; font-style: italic; font-family: Optima; color: #8BE8E5'>Built by TAIWO K. LASH</h6>", unsafe_allow_html=True)
    st.markdown("<br><br>", unsafe_allow_html=True)

    # st.markdown("<h4 style='font-weight: bold; colour: #E55604'>Overview</h4>", unsafe_allow_html=True)
    # st.markdown("<p style='text-align: justify; color: #F5FCCD; background-color: #252B48; padding: 10px;'>Online payment fraud is a significant concern for financial institutions, e-commerce platforms, and consumers. Fraudsters continually devise new methods to exploit vulnerabilities in online payment systems, resulting in financial losses and security breaches. This application is built to identify online payment fraud swiftly and prevent fraudulent transactions in real-time.</p>", unsafe_allow_html=True)


# Add an overview
    st.markdown("<h3 style='font-weight: bold; color: black;'>Overview</h3>", unsafe_allow_html=True)
    st.markdown(
        """
        <p style='text-align: justify; color: black; background-color: white; padding: 10px;'>
        Welcome to 'The Shield'—your powerful ally against online payment fraud. In today's digital age, online payment fraud poses a significant threat to financial institutions, e-commerce platforms, and consumers alike. Fraudsters are relentless in their pursuit of exploiting vulnerabilities in online payment systems, leading to substantial financial losses and security breaches.
        </p>
        <p style='text-align: justify; color: black; background-color: white; padding: 10px;'>
        'The Shield' is not just an application; it's your dedicated safeguard. This innovative solution is designed to swiftly identify online payment fraud and prevent fraudulent transactions in real-time. Our state-of-the-art algorithms and technologies work tirelessly to keep your financial transactions secure and fraud-free. With 'The Shield' by your side, you can confidently navigate the digital landscape, knowing that your financial interests are protected.
        </p>
        <p style='text-align: justify; color: black; background-color: white; padding: 10px;'>
        At 'The Shield,' we are committed to staying one step ahead of fraudsters, ensuring your peace of mind in an evolving digital world. We believe in the power of technology to safeguard your financial well-being. 'The Shield' is more than just an application; it's a promise of security and trust.
        </p>
        """,
        unsafe_allow_html=True
    )

                # data = pd.read_csv('onlinefraud.csv')
    df = pd.read_csv('column explanation.txt')
            # df.reset_index(drop=True, inplace=True)
