#about.py

#load necessary modules
import streamlit as st

#define the app/page and its contents
def app():
    st.subheader('About')
    st.write('Welcome to my database web app')
    st.markdown("\n")
    st.write("My goal with this app is to present work I have actually done in the SQL query language. I wanted to avoid copying someone else's tutorial/code\n")
    st.write("and not having a way to show the results of a course I passed, I figured I would need to create an app to do this. The app is written in Python with\n")
    st.write("Streamlit as the front end framework and the data stored on Google Cloud and using BigQuery.")
    st.markdown("\n")
    st.write("I start with Basic and Advanced where the viewer can run the queries with results displayed and a refresh button. I also include what the query is supposed to\n")
    st.write("do as well as the syntax in code form. The data comes from a book I purchased called 'Data Analytics in Healthcare Research'.")
    st.markdown("\n")
    st.write("There were some challenges with some of the statements via this app and there is more info for those queries.") 
    st.markdown("\n")
    st.write("String Functions and Window Functions are being worked on.")
    
    
