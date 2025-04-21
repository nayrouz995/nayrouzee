import streamlit as st
from db.firebase_app import register
from streamlit_extras.switch_page_button import switch_page
from utils.streamlit_utils import hide_icons, hide_sidebar, remove_whitespaces
import pyrebase
import os
from dotenv import load_dotenv
load_dotenv()


st.set_page_config(layout="wide", initial_sidebar_state="collapsed")
hide_icons()
hide_sidebar()
remove_whitespaces()
clicked_login=st.button("Already registered? Click here to login!")
if clicked_login:
    switch_page("login")

if 'profile'not in st.session_state:
            st.session_state.profile = "verifier"

form = st.form("login")
email = form.text_input("Enter your email").strip()
password = form.text_input("Enter your password", type="password").strip()
   
submit = form.form_submit_button("Register")
if submit:
    if not email or not password:
            st.error("Please enter both email and password.")
        

    if st.session_state.profile == "verifer":
               valid_email = os.getenv("institute_email").strip()
               valid_pass = os.getenv("institute_password").strip()
               if email==valid_email & password==valid_pass:
                   switch_page("verifier")
                   st.session_state.profile = "verifier"
    else:
        result = register(email, password)
        print(result)
        if result == "success":
            st.success("register successful!")
            switch_page("institute")
        else:
            st.error("Invalid credentials!")






