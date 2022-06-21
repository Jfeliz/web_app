import streamlit as st

def app():
    st.subheader('References')
    st.write('Data Analytics in Healthcare Research; Tools and Strategies; David T. Marc, MBS, CHDA | Ryan H. Sandefer, MA, CPHIT')
    st.write("\n")
    st.subheader('Training')
    st.write("'Learning SQL Programming' from LinkedIn Learning")
    st.write("\n")
    st.subheader('Other')
    link = '[Link](https://github.com/mmoralls/web_app) to my Github repository'
    st.markdown(link,unsafe_allow_html=True)

    #include the author of the main app
