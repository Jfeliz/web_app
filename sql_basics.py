#app2.py
import streamlit as st
import pandas_gbq
import pandas as pd
import os

os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = '/home/mark/Documents/Data_Projects/web-app/web-app-341703-626adddc7d5a.json'
project_id = 'web-app-341703'

def app():
    st.subheader('SQL - Basics')
    
    with st.container():

        col1, col2 = st.columns([5,1])
        
    #------Query1------
    with col1:
        with st.form(key='query1', clear_on_submit = True):
                st.write("Return all hospitals in California [SELECT]")
                st.code("SELECT hospital_name, city \nFROM hosp_info.hospital_general_information \nLIMIT 10")
                submit_code = st.form_submit_button("Execute") 
            
    if submit_code:

        with open('queries/basic/SELECT.sql') as f:
                contents = f.read()
                df = pandas_gbq.read_gbq(contents, project_id)
                st.table(df)

    with col2:
            # this line is a shortcut to clicking the hamburger menu to refresh
                st.button(key='Refresh1', label='Refresh screen')
    
    #------Query2------
    with st.container():

        col1, col2 = st.columns([5,1])
   
    with col1:
        with st.form(key='query2', clear_on_submit = True):
                st.write("Return all hospitals where the state is CA [WHERE]")
                st.code("SELECT hospital_name, city, state, county_name, hospital_type, hospital_ownership FROM hosp_info.hospital_general_information \nWHERE state = 'CA'")
                submit_code = st.form_submit_button("Execute") 
            
    if submit_code:

        with open('queries/basic/WHERE.sql') as f:
                contents = f.read()
                df = pandas_gbq.read_gbq(contents, project_id)
                st.table(df)

    with col2:
            # this line is a shortcut to clicking the hamburger menu to refresh
                st.button(key='Refresh2', label='Refresh screen')

    #------Query3------
    with st.container():

        col1, col2 = st.columns([5,1])
   
    with col1:
        with st.form(key='query3', clear_on_submit = True):
                st.write("Return all hospitals in the city of Orlando, Florida that are Acute Care Hospitals [AND]")
                st.code("SELECT hospital_name, city, state, county_name, hospital_type, hospital_ownership \nFROM hosp_info.hospital_general_information \nWHERE state='FL' AND city='Orlando' AND hospital_type = 'Acute Care Hospitals'")
                submit_code = st.form_submit_button("Execute") 
            
    if submit_code:

        with open('queries/basic/AND.sql') as f:
                contents = f.read()
                df = pandas_gbq.read_gbq(contents, project_id)
                st.write(df)

    with col2:
            # this line is a shortcut to clicking the hamburger menu to refresh
                st.button(key='Refresh3', label='Refresh screen')

    #------Query4------
    with st.container():

        col1, col2 = st.columns([5,1])
    
    with col1:
        with st.form(key='query4', clear_on_submit = True):
                st.write("Return all records for hospitals in the state of CA or CO and are Acute Care Hospitals [OR]")
                st.code("SELECT hospital_name, city, state, county_name, hospital_type, hospital_ownership \nROM hosp_info.hospital_general_information \nWHERE (state='CA' OR state='CO') AND hospital_type='ACUTE CARE - VETERANS ADMINISTRATION'")
                submit_code = st.form_submit_button("Execute") 
            
    if submit_code:

        with open('queries/basic/OR.sql') as f:
                contents = f.read()
                df = pandas_gbq.read_gbq(contents, project_id)
                st.table(df)

    with col2:
            # this line is a shortcut to clicking the hamburger menu to refresh
                st.button(key='Refresh4', label='Refresh screen')

    #------Query5------
    with st.container():

        col1, col2 = st.columns([5,1])
    
    with col1:
        with st.form(key='query5', clear_on_submit = True):
                st.write("Return all hospitals by city and state ordered by state ascending [ORDER BY and ASC]")
                st.code("SELECT hospital_name, city, state \nFROM hosp_info.hospital_general_information ORDER BY state ASC\nLIMIT 25")
                submit_code = st.form_submit_button("Execute") 
            
    if submit_code:

        with open('queries/basic/ORDER_BY_and_ASC.sql') as f:
                contents = f.read()
                df = pandas_gbq.read_gbq(contents, project_id)
                st.table(df)

    with col2:
            # this line is a shortcut to clicking the hamburger menu to refresh
                st.button(key='Refresh5', label='Refresh screen')

    #------Query6------
    with st.container():

        col1, col2 = st.columns([5,1])
    
    with col1:
        with st.form(key='query6', clear_on_submit = True):
                st.write("Display a unique county and hospital name [DISTINCT]")
                st.code("SELECT DISTINCT(county_name), hospital_name \nFROM hosp_info.hospital_general_information WHERE county_name = 'SAN FRANCISCO'")
                submit_code = st.form_submit_button("Execute") 
            
    if submit_code:

        with open('queries/basic/DISTINCT.sql') as f:
                contents = f.read()
                df = pandas_gbq.read_gbq(contents, project_id)
                st.table(df)

    with col2:
            # this line is a shortcut to clicking the hamburger menu to refresh
                st.button(key='Refresh6', label='Refresh screen')

#------Query7------
    with st.container():

        col1, col2 = st.columns([5,1])
    
    with col1:
        with st.form(key='query7', clear_on_submit = True):
                st.write("Filter NULL values for the score for measure_name [IS NOT NULL]")
                st.code("SELECT measure_name, score \nFROM hosp_info.hospital_associated_infection \nWHERE score IS NOT NULL, LIMIT '10' ")
                submit_code = st.form_submit_button("Execute") 
            
    if submit_code:

        with open('queries/basic/IS_NOT_NULL.sql') as f:
                contents = f.read()
                df = pandas_gbq.read_gbq(contents, project_id)
                st.table(df)

    with col2:
            # this line is a shortcut to clicking the hamburger menu to refresh
                st.button(key='Refresh7', label='Refresh screen')

    st.write("For the CREATE, INSERT, DROP, ALTER, UPDATE and DELETE statements I tried to create a temporary session using CTE or Temporary Table to avoid complications\n")
    st.write ("with a permanent table, like managing access to the table with multiple individuals, security, etc.\n") 
    st.write ("So I decided to present the query as it would be executed in the Bigquery console, save the output to csv and then have the app read and display the results.")

#------Query8------
    with st.container():

        col1, col2 = st.columns([5,1])
    
    with col1:
                st.write("This query drops a new table if it exists, creates a new table and inserts a new record. [DROP, CREATE, INSERT]")
                st.code("DROP TABLE IF EXISTS hosp_info.newtable;\nCREATE TABLE newtable\n(\n  provider_npi INTEGER,\n  provider_id INTEGER,\n  hospital_name STRING,\n  address STRING,\n  city STRING,\n  state STRING,\n  state_code INTEGER,\n  zipcode INTEGER,\n  county_name STRING,\n  phone_number STRING,\n  hospital_type STRING,\n  hospital_ownership STRING,\n  emergency_services BOOLEAN,\n);\n\nINSERT INTO newtable\nVALUES (9893458312, 1015, 'WASHINGTON MEDICAL CLINIC', '300 PARSONS STREET', 'PRESCOTT', 'AZ', 4, 86313, 'YAVAPAI', '(928)445-4734', 'ACUTE CARE - VETERANS ADMINISTRATION', 'Government Federal', false);\n\nSELECT *\n FROM newtable;")
                data = pd.read_csv('queries/create_insert_newtable.csv')
                st.table(data)

#------Query9------
    with st.container():

        col1, col2 = st.columns([5,1])
    
    with col1:
        
                st.write("This query updates a record in the new table and returns the results of the update [UPDATE]")
                st.write("\n")
                st.code("UPDATE hosp_info.newtable\nSET hospital_name = 'WASHINGTON FEDERAL MEDICAL CLINIC'\nWHERE provider_id = 1015;\n\nSELECT * FROM hosp_info.newtable")
                data = pd.read_csv('queries/update_newtable.csv')
                st.table(data)

#------Query10------
    with st.container():

        col1, col2 = st.columns([5,1])
    
    with col1:
        
                st.write("This query adds a new column to the new table. [ALTER]")
                st.code("ALTER TABLE hosp_info.newtable\nADD COLUMN country STRING; \nSELECT * FROM hosp_info.newtable")
                data = pd.read_csv('queries/alter_newtable.csv')
                st.table(data)

#------Query11------
    with st.container():

        col1, col2 = st.columns([5,1])
    
    with col1:
        
                st.write("This query deletes the record that was originally created. [DELETE]")
                st.code("DELETE FROM hosp_info.newtable\nWHERE provider_id = 1015;\n\nSELECT * FROM hosp_info.newtable") 
