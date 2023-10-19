import streamlit as st

def app():
    # st.title("Logout Page")
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


    if 'user' not in st.session_state:
        st.session_state.user = None

    if st.session_state.user:
        st.write(f"Logged in as {st.session_state.user}")

        # Create a checkbox to confirm the logout
        confirm_logout = st.button("Confirm Logout")
        
        if confirm_logout:
            st.session_state.user = None
            st.write("You have successfully logged out.")
        else:
            st.write("Are you sure you want to log out?")
    else:
        st.title("Logged Out")
        st.write("You are already logged out.")
        st.button("Login", key="login_button")

if __name__ == '__main__':
    app()
