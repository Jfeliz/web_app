#about.py

#load necessary modules
import streamlit as st

#define the app/page and its contents
def app():
    st.subheader('About')
    st.write('Welcome to my database web app')
    st.markdown('\n')
    st.write('My goal with this app is to present 'evidence of experience' with the SQL query language using some provided healthcare data from a book I purchased.\n")
    st.write('The app also helps to reinforce some basic Python skills I learned to present some basic to advanced SQL queries that I have done.')
    st.markdown('\n')
    st.write('The app is written in Python with the Streamlit library as the front end framework and the data stored on Google BigQuery as the back end. I present my queries\n')
    st.write('for users to view the SQL syntax, execute it, and see the results displayed.\n')  
    st.markdown('\n')
    st.write('There are instances where some SQL queries would be difficult to execute, such as ALTER or UPDATE, because of permissions to consider for each viewer or trying\n') 
    st.write('to recreate a table each time as reasons to avoid.\n')
    st.write('In these cases I chose to display the table as it was before, the query, and then display the results. I also include what the query is supposed to\n')
    st.write('do as well as the syntax in code form.")
    
