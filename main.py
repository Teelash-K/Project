import streamlit as st
import pickle
import pandas as pd
from streamlit_option_menu import option_menu
import  home, features, about, logout
import sqlite3

st.set_page_config(
    page_title = "The Shield",
)


# connect to SQLite DB
conn = sqlite3.connect('users.db')
c = conn.cursor()

# user table
c.execute('''CREATE TABLE IF NOT EXISTS users(
         username TEXT, password TEXT
)''')

# # def create_users(username, password):
# c.execute("INSERT INTO users VALUES ('teelash', 'password')")
# conn.commit()
# conn.close()

def authenticate_user(username, password):
    c.execute("SELECT password FROM users WHERE username = ?", (username,))
    result = c.fetchone()
    if result and result[0] == password:
        return True
    return False


def login_signup():
        st.markdown("<h1 style = 'top-margin: 0rem;text-align: center; color: #7C73C0;'>Welcome to The Shield 🛡</h1>", unsafe_allow_html=True)
        # st.markdown('Welcome to :purple[The Shield] 🛡')
        # st.title("Loging or Sign Up")
        login_signup_page = st.selectbox("Select an option to log in or sign up", ["Login", "Signup"])

        if login_signup_page == "Login":
            login_username = st.text_input("Username (login)")
            login_password = st.text_input("Password (login)", type = "password")

        if st.button("Login"):
            if authenticate_user(login_username, login_password):
                st.session_state.user = login_username
                st.success("Login successful.")
            
            else:
                st.error("Login failed. Enter a valid username or password.")
        
        elif login_signup_page =="Signup":
            signup_username = st.text_input("Username (signup)")
            signup_password = st.text_input("Password", type = "password")

            if st.button("Sign Up"):
                c.execute("INSERT INTO users VALUES (?, ?)", (signup_username, signup_password))
                conn.commit()
                st.success("Account created.")

# def home_app():
#      st.title("Home")
#      st.write("Welcome to the Home page!")

# def about_app():
#      st.title("About")
#      st.write("Welcome to the About page!")     

# def logout_app():
#      st.title("Logout")
#      st.write("You have successfully logged out.")

class MultiApp:

    def __init__(self):
        self.apps = []

    def add_app(self, title, func):
        self.apps.append({
            "title": title,
            "function": func
        })

    def run(self):
        with st.sidebar:
            app = option_menu(
                menu_title = 'The Shield',
                options = ['Home', 'Features', 'About', 'Logout'],
                icons = ['house-fill', '', 'person-circle', 'info', 'Logout'],
                menu_icon = 'shield-fill',
                default_index = 1,
                styles = {
                    "container": {"padding": "5!important", "background-color":'#9F91CC'},
                    "icon":{"color": "white", "font-size": "23px"},
                    "nav-link": {"color": "white", "font-size": "20px", "text-align": "left", "margin": "0px", "--hover-color": "#82A0D8"},
                    "nav-link-selected": {"background-color": "#8DDFCB"},
                    })

        if app == "Home":
            home.app()
        if app == "Features":
            features.app()
        if app == "About":
            about.app()
        if app == "Logout":
            logout.app()

    # run()
if __name__ == '__main__':
    if 'user' not in st.session_state:
        st.session_state.user = None

    if st.session_state.user is None:
        login_signup()
    else:
        multi_app = MultiApp()
        multi_app.add_app('Home', home.app)
        multi_app.add_app('Features', features.app)
        multi_app.add_app('About', about.app)
        multi_app.add_app('Logout', logout.app)
        multi_app.run()    

