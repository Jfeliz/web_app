#main-app.py


# import libraries
import streamlit as st

st.set_page_config(layout="wide") # can only be used once and must be the first line

import about
import sql_basics
import sql_advanced
import sql_functions
#import sql_string_functions
#import sql_window_functions
#import python
import references
import contact



PAGES = {
    "About": about,
    "SQL - Basics": sql_basics,
    "SQL - Advanced": sql_advanced,
    "SQL - Functions": sql_functions,
    #"SQL - String Functions": sql_string_functions,
    #"SQL- Window Functions": sql_window_functions,
    #"Python": python,
    "References": references,
    "Contact": contact
}
st.sidebar.title('Menu')
selection = st.sidebar.radio("Please make a selection ...", list(PAGES.keys()))
page = PAGES[selection]
page.app()

#with open('static/css/style.css') as f:
#    st.markdown(f'<style>(f.read()</style>', unsafe_allow_html=True)