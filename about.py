#about.py

#load necessary modules
import streamlit as st

#define the app/page and its contents
def app():
    st.subheader('About')
    st.write('Welcome to my database web app')
    st.markdown("\n")
    st.write("My goal with this app is to present 'evidence experience: work I have actually done with the SQL query language using some provided healthcare data from a book I purchased. The app also helps to reinforce some\n")
    st.write("basic Python skills and a good reference of SQL queries that I have done and a springboard to more complex queries.\n")
    st.write("The app is written in Python with Streamlit as the front end framework and the data stored on Google BigQuery as the back end. I present my queries for users to view the sql syntax, execute it, and see the results displayed.\n")  
    st.write("There are instances where some syntax would be difficult to execute, such as ALTER or UPDATE, permissions to consider for each viewer or trying to recreate a table each time as reasons to avoid.\n")
    st.write("In these cases I chose to display the table as it was before, the query to perform, and then display the results. I also include what the query is supposed to\n")
    st.write("do as well as the syntax in code form.")
    st.markdown("\n")
    st.write("This wasn't an easy app to create even with all the help available but I persisted and am glad to share it.")
    st.markdown("\n")
    st.write("I look forward to providing more queries for my viewers")
    
    
