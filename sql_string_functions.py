#sql_string_functions

#import required libraries
import streamlit as st
from PIL import Image
import pandas_gbq
from google.cloud import bigquery
from google.oauth2 import service_account

#read credentials for BigQuery access
credentials = service_account.Credentials.from_service_account_info(
    st.secrets["gcp_service_account"]
)
client = bigquery.Client(credentials=credentials)
project_id = 'web-app-341703'

def app():
    st.subheader('SQL - String Functions')
    
    #------Query1------
    with st.container():
        st.write("For this query I used a temporary table to change a data type. As shown in the left image the original column is named 'score' and the new column is named score1.")
        col1, col2, col3 = st.columns([3,3,3])
   
    with col1:
        image = Image.open('images/datatype_before.png')
        st.write("This query casts the score column data type of STRING to INTEGER and a new table. [SAFE CAST]")
        st.image(image, caption='Before')

    with col2:
        st.write("\n")
        st.write("\n")
        st.code("SELECT score,\nSAFE_CAST(score AS INTEGER) AS score1\nFROM hosp_info.timely_and_effective_care")

    with col3:
        
        image = Image.open('images/datatype_after.png')
        st.image(image, caption='After')

     #------Query2------
    with st.container():
        
        col1, col2, col3 = st.columns([3,3,3])
    
    with col1:
        st.write("This query combines measure name with measure id [CONCAT]")
        image = Image.open('images/concat_before.png')
        st.image(image, caption='Before')

    with col2:
        with st.form(key='query2', clear_on_submit = True):
            st.code("SELECT \n  CONCAT('CLABSI Lower Confidence Limit',';', ' ','HAI_1_CI_LOWER') \n  AS Concat\nFROM hosp_info.hospital_associated_infection\nLIMIT 10")
            submit_code = st.form_submit_button("Execute")
     
    if submit_code:

        with open('queries/string_functions/CONCAT.sql') as f:
            contents = f.read()
            df = pandas_gbq.read_gbq(contents, project_id)
               
        with col3:
            st.table(df)
            st.image(image, caption='After')
            st.button(key='Refresh2', label='Refresh screen')

     #------Query3------
    with st.container():
        
        col1, col2, col3 = st.columns([3,3,3])

    with col1:
        st.write("This query returns a substring of a footnote. [SUBSTR]")
        image = Image.open('images/substr_before.png')
        st.image(image, caption='Before')
        
    with col2:
        with st.form(key='query3', clear_on_submit = True):
            st.code("SELECT\n    SUBSTR(footnote, 4, 7) AS Returned_word\nFROM hosp_info.hospital_associated_infection\nWHERE footnote IS NOT NULL\nLIMIT 10")
            submit_code = st.form_submit_button("Execute") 
            
    if submit_code:

        with open('queries/string_functions/SUBSTR.sql') as f:
            contents = f.read()
            df = pandas_gbq.read_gbq(contents, project_id)
            
   
        with col3:
            st.table(df)
            st.image(image, caption='After')
            st.button(key='Refresh3', label='Refresh screen')
    
       #------Query4------
    with st.container():
        
        col1, col2, col3 = st.columns([3,3,3])

    with col1:
        st.write("This query returns the first occurence of the letter 's' in the measure_name field. [INSTR]")
        image = Image.open('images/instr_before.png')
        st.image(image, caption='Before')
        
    with col2:
        st.write("\n")
        st.write("\n")
        with st.form(key='query4', clear_on_submit = True):
            st.code("SELECT measure_name,\nINSTR(measure_name, 's') AS First_occurence_of_s\nFROM hosp_info.hospital_associated_infection\nLIMIT 10")
            submit_code = st.form_submit_button("Execute")
            st.write("\n")
                        
    if submit_code:

        with open('queries/string_functions/INSTR.sql') as f:
            contents = f.read()
            df = pandas_gbq.read_gbq(contents, project_id)
            
   
        with col3:
            st.table(df)
            st.image(image, caption='After')
            st.button(key='Refresh4', label='Refresh screen')

       #------Query5------
    with st.container():
        
        col1, col2, col3 = st.columns([3,3,3])

    with col1:
        st.write("This query removes the trailing number '_1' in the measure_id column. [TRIM]")
        image = Image.open('images/trim_before.png')
        st.image(image, caption='Before')
        
    with col2:
        st.write("\n")
        st.write("\n")
        with st.form(key='query5', clear_on_submit = True):
            st.code("SELECT\n  TRIM(measure_id, '_1') as Trimmed_ID\nFROM hosp_info.medicare_hospital_spending_per_patient\nLIMIT 10;")
            submit_code = st.form_submit_button("Execute")
            st.write("\n")
                        
    if submit_code:

        with open('queries/string_functions/TRIM.sql') as f:
            contents = f.read()
            df = pandas_gbq.read_gbq(contents, project_id)
            
   
        with col3:
            st.table(df)
            st.image(image, caption='After')
            st.button(key='Refresh5', label='Refresh screen')         