import streamlit as st
import pickle
import pandas as pd

def app():

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

        # data = pd.read_csv('onlinefraud.csv')
    df = pd.read_csv('column explanation.txt', sep =':')
        # df.reset_index(drop=True, inplace=True)
    # with st.expander("Variable Definitions"):
    st.markdown("<h4 style = 'top-margin: 0rem;text-align: center; color: black;'>Variable Definition</h4>", unsafe_allow_html=True)
    # st.markdown("Variable Definition")
    st.table(df)