#sql_basics.py

# import libraries
import streamlit as st
import pandas_gbq
from google.cloud import bigquery
from google.oauth2 import service_account
from PIL import Image

#read credentails for BigQuery access
credentials = service_account.Credentials.from_service_account_info(
    st.secrets["secrets.toml"]
)
client = bigquery.Client(credentials=credentials)
#project_id = 'web-app-341703'

def app():
    st.subheader('SQL - Basics')
    
    with st.container():

        col1, col2 = st.columns([5,1])
        
    #------Query1------
    with col1:
        with st.form(key='query1', clear_on_submit = True):
                st.write("Return all hospitals in the state of California. [SELECT]")
                st.code("SELECT hospital_name, city \nFROM hosp_info.hospital_general_information \nLIMIT 10")
                submit_code = st.form_submit_button("Execute") 
            
    if submit_code:

        with open('queries/basic/SELECT.sql') as f:
                contents = f.read()
                df = pandas_gbq.read_gbq(contents)
                st.table(df)

    with col2:
            # this line is a shortcut to clicking the hamburger menu to refresh
                st.button(key='Refresh1', label='Refresh screen')
    
    #------Query2------
    with st.container():

        col1, col2 = st.columns([5,1])
   
    with col1:
        with st.form(key='query2', clear_on_submit = True):
                st.write("Return all hospitals where the state is CA. [WHERE]")
                st.code("SELECT hospital_name, city, state, county_name, hospital_type, hospital_ownership FROM hosp_info.hospital_general_information \nWHERE state = 'CA'")
                submit_code = st.form_submit_button("Execute") 
            
    if submit_code:

        with open('queries/basic/WHERE.sql') as f:
                contents = f.read()
                df = pandas_gbq.read_gbq(contents)
                st.table(df)

    with col2:
            # this line is a shortcut to clicking the hamburger menu to refresh
                st.button(key='Refresh2', label='Refresh screen')

    #------Query3------
    with st.container():

        col1, col2 = st.columns([5,1])
   
    with col1:
        with st.form(key='query3', clear_on_submit = True):
                st.write("Return all hospitals in the city of Orlando, Florida that are Acute Care Hospitals. [AND]")
                st.code("SSELECT hospital_name, state, hospital_type\nFROM hosp_info.hospital_general_information \nWHERE state='FL' AND hospital_type = 'Acute Care Hospitals'")
                submit_code = st.form_submit_button("Execute") 
            
    if submit_code:

        with open('queries/basic/AND.sql') as f:
                contents = f.read()
                df = pandas_gbq.read_gbq(contents)
                st.write(df)

    with col2:
            # this line is a shortcut to clicking the hamburger menu to refresh
                st.button(key='Refresh3', label='Refresh screen')

    #------Query4------
    with st.container():

        col1, col2 = st.columns([5,1])
    
    with col1:
        with st.form(key='query4', clear_on_submit = True):
                st.write("Return all hospitals in the state of CA or CO and are Acute Care VA Hospitals. [OR]")
                st.code("SELECT hospital_name, city, state, county_name, hospital_type, hospital_ownership \nROM hosp_info.hospital_general_information \nWHERE (state='CA' OR state='CO') AND hospital_type='ACUTE CARE - VETERANS ADMINISTRATION'")
                submit_code = st.form_submit_button("Execute") 
            
    if submit_code:

        with open('queries/basic/OR.sql') as f:
                contents = f.read()
                df = pandas_gbq.read_gbq(contents)
                st.table(df)

    with col2:
            # this line is a shortcut to clicking the hamburger menu to refresh
                st.button(key='Refresh4', label='Refresh screen')

    #------Query5------
    with st.container():

        col1, col2 = st.columns([5,1])
    
    with col1:
        with st.form(key='query5', clear_on_submit = True):
                st.write("Return all hospitals by city and state ordered by state and ascending. [ORDER BY and ASC]")
                st.code("SELECT hospital_name, city, state \nFROM hosp_info.hospital_general_information ORDER BY state ASC\nLIMIT 25")
                submit_code = st.form_submit_button("Execute") 
            
    if submit_code:

        with open('queries/basic/ORDER_BY_and_ASC.sql') as f:
                contents = f.read()
                df = pandas_gbq.read_gbq(contents)
                st.table(df)

    with col2:
            # this line is a shortcut to clicking the hamburger menu to refresh
                st.button(key='Refresh5', label='Refresh screen')

    #------Query6------
    with st.container():

        col1, col2 = st.columns([5,1])
    
    with col1:
        with st.form(key='query6', clear_on_submit = True):
                st.write("Return unique infection measure names. [DISTINCT]")
                st.code("SELECT DISTINCT(measure_name), hospital_name \nFROM hosp_info.hospital_associated_infection")
                submit_code = st.form_submit_button("Execute") 
            
    if submit_code:

        with open('queries/basic/DISTINCT.sql') as f:
                contents = f.read()
                df = pandas_gbq.read_gbq(contents)
                st.table(df)

    with col2:
            # this line is a shortcut to clicking the hamburger menu to refresh
                st.button(key='Refresh6', label='Refresh screen')

#------Query7------
    with st.container():

        col1, col2, col3 = st.columns([3,3,3])
    
    with col1:
            st.write("Filter NULL values for the score for measure_name. [IS NOT NULL]")
            image = Image.open('images/is_not_null_before.png')
            st.image(image, caption='Before')
         
    with col2:
        with st.form(key='query7', clear_on_submit = True):
             st.code("SELECT measure_name, score \nFROM hosp_info.hospital_associated_infection \nWHERE score IS NOT NULL, LIMIT '10' ")
             submit_code = st.form_submit_button("Execute") 
            
    if submit_code:
        with open('queries/basic/IS_NOT_NULL.sql') as f:
            contents = f.read()
            df = pandas_gbq.read_gbq(contents)

        with col3:
            st.table(df)
            st.image(image, caption='After')
            st.button(key='Refresh7', label='Refresh screen')

#------Query8------
    st.write("For the CREATE, INSERT, DROP, ALTER, UPDATE and DELETE statements I kept things simple by showing how the queries would be executed in the Bigquery console. ")
    
    with st.container():

        col1, col2 = st.columns([5,5])
    
    with col1:
        st.write("This query drops a new table if it exists, creates a new table and inserts a new record. [DROP, CREATE, INSERT]")
        st.code("DROP TABLE IF EXISTS hosp_info.newtable;\nCREATE TABLE newtable\n(\n  provider_npi INTEGER,\n  provider_id INTEGER,\n  hospital_name STRING,\n  address STRING,\n  city STRING,\n  state STRING,\n  state_code INTEGER,\n  zipcode INTEGER,\n  county_name STRING,\n  phone_number STRING,\n  hospital_type STRING,\n  hospital_ownership STRING,\n  emergency_services BOOLEAN,\n);\n\nINSERT INTO newtable\nVALUES (9893458312, 1015, 'WASHINGTON MEDICAL CLINIC', '300 PARSONS STREET', 'PRESCOTT', 'AZ', 4, 86313, 'YAVAPAI', '(928)445-4734', 'ACUTE CARE - VETERANS ADMINISTRATION', 'Government Federal', false);\n\nSELECT *\n FROM newtable;")
            
    with col2:
        image = Image.open('images/drop_create_insert.png')
        st.image(image, caption='After')
            
#------Query9------
    with st.container():

        col1, col2 = st.columns([5,5])
    
    with col1:
        st.write("This query updates a record in the new table and returns the results of the update (Washington Medical Clinic to Washington Federal Medical Clinic). [UPDATE]")
        st.write("\n")
        st.code("UPDATE hosp_info.newtable\nSET hospital_name = 'WASHINGTON FEDERAL MEDICAL CLINIC'\nWHERE provider_id = 1015;\n\nSELECT * FROM hosp_info.newtable")
    
    with col2:
        st.write("\n")
        st.write("\n")
        st.write("\n")
        st.write("\n")
        image = Image.open('images/update.png')
        st.image(image, caption='After')

#------Query10------
    with st.container():

        col1, col2 = st.columns([5,5])
    
    with col1:
        st.write("This query adds a new column to the new table. [ALTER]")
        st.code("ALTER TABLE hosp_info.newtable\nADD COLUMN country STRING; \nSELECT * FROM hosp_info.newtable")
    
    with col2:
        st.write("\n")
        st.write("\n")
        st.write("\n")
        st.write("\n")
        image = Image.open('images/alter.png')
        st.image(image, caption='After')


#------Query11------
    with st.container():

        col1, col2 = st.columns([5,5])
    
    with col1:
        
            st.write("This query deletes the record that was originally created. [DELETE]")
            st.code("DELETE FROM hosp_info.newtable\nWHERE provider_id = 1015;\n\nSELECT * FROM hosp_info.newtable") 

    with col2:
        st.write("\n")
        st.write("\n")
        st.write("\n")
        st.write("\n")
        image = Image.open('images/delete.png')
        st.image(image, caption='After')
