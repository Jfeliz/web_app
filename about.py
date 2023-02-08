#load necessary modules
import streamlit as st

#define the app/page and its contents
def app():
    st.subheader('About')
    st.write('Welcome to my database web app')
    st.markdown("\n")
    st.write("My goal with this app is to present work I have actually done with the SQL query language using some provided healthcare data from a book I purchased. The app is written in Python with\n")
    st.write("Streamlit as the front end framework and the data stored on Google BigQuery as the back end. I present queries for users to view the sql syntax, execute it, and see the results displayed.\n")  
    st.write("There are instances where some syntax would be difficult to execute, such as ALTER or UPDATE, with permissions to consider for each viewer or trying to recreate a table each time as reasons to avoid.\n")
    st.write("In these cases I chose to display the table as it was before, the query to perform, and then the results. I also include what the query is supposed to do as well as the syntax in code form.")
   
