#SQL functions page

#load libraries
import streamlit as st
import os
import pandas_gbq

os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = '/home/mark/Documents/Data_Projects/web-app/web-app-341703-626adddc7d5a.json'
project_id = 'web-app-341703'

def app():
    st.subheader('SQL - Functions')
    
# The following lines create a 2 column layout for a query (incl. what is does, the T-SQL syntax used and display of the query) and a refresh button

#------Query1------
    with st.container():

        col1, col2 = st.columns([5,1])
    
    with col1:
        with st.form(key='query1', clear_on_submit = True):
                st.write("This query selects the maximum prediceted readmission rate for all providers. [MAX]")
                st.code("SELECT MAX(predicted_readmission_rate) AS Max_Readmission_Rate\nFROM hosp_info.readmission_reduction")
                submit_code = st.form_submit_button("Execute") 
            
    if submit_code:

        with open('queries/functions/MAX.sql') as f:
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
                st.write("This query counts the nuber of hospitals in California. [COUNT]")
                st.code("SELECT COUNT(*) AS Number_of_Hospitals_in_Calif\nFROM hosp_info.hospital_general_information\nWHERE state = 'CA' [COUNT]")
                submit_code = st.form_submit_button("Execute") 
            
    if submit_code:

        with open('queries/functions/COUNT.sql') as f:
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
                st.write("This query returns the length of characters in the hospital name [LENGTH]")
                st.code("SELECT hospital_name, LENGTH(hospital_name) AS Number_of_Characters\nFROM hosp_info.hospital_general_information\nLIMIT 10")
                submit_code = st.form_submit_button("Execute") 
            
    if submit_code:

        with open('queries/functions/LENGTH.sql') as f:
                contents = f.read()
                df = pandas_gbq.read_gbq(contents, project_id)
                st.table(df)
 
    with col2:
            # this line is a shortcut to clicking the hamburger menu to refresh
                st.button(key='<unique name>', label='Refresh screen')

#------Query4------
    with st.container():

        col1, col2 = st.columns([5,1])
    
    with col1:
        with st.form(key='query4', clear_on_submit = True):
                st.write("Returns the minimum uninsured rate. [MIN]")
                st.code("SELECT MIN(disabled_medicare_rate) AS Min_Disabled_Medicare_Rate\nFROM hosp_info.measures_of_birth_and_death")
                submit_code = st.form_submit_button("Execute") 
            
    if submit_code:

        with open('queries/functions/MIN.sql') as f:
                contents = f.read()
                df = pandas_gbq.read_gbq(contents, project_id)
                st.table(df)
                #st.write(df)

    with col2:
            # this line is a shortcut to clicking the hamburger menu to refresh
                st.button(key='Refresh4', label='Refresh screen')

#------Query5------
    with st.container():

        col1, col2 = st.columns([5,1])
    
    with col1:
        with st.form(key='query5', clear_on_submit = True):
                st.write("<Returns sum of all deaths from all hospitals [SUM]")
                st.code("SELECT SUM(total_deaths) AS Sum_of_Deaths_all_Hospitals \nFROM hosp_info.measures_of_birth_and_death")
                submit_code = st.form_submit_button("Execute") 
            
    if submit_code:

        with open('queries/functions/SUM.sql') as f:
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
                st.write("Retunrs the sum of the primary care physician rate and then rounds it. [ROUND]")
                st.code("SELECT ROUND(SUM(prim_care_phys_rate),1) as Primary_Care_Physician_Rate\nFROM hosp_info.measures_of_birth_and_death")
                submit_code = st.form_submit_button("Execute") 
            
    if submit_code:

        with open('queries/functions/ROUND.sql') as f:
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
                st.write("Returns the number of providers in each city and state, then groups by city and state. [GROUP BY] ")
                st.code("SELECT COUNT(provnum) provider_name, city, state\nFROM hosp_info.nursing_home_provider_info\nGROUP BY city, state\nLIMIT 10")
                submit_code = st.form_submit_button("Execute") 
            
    if submit_code:

        with open('queries/functions/GROUPBY.sql') as f:
                contents = f.read()
                df = pandas_gbq.read_gbq(contents, project_id)
                st.table(df)

    with col2:
            # this line is a shortcut to clicking the hamburger menu to refresh
                st.button(key='Refresh7', label='Refresh screen')

#------Query8------
    with st.container():

        col1, col2 = st.columns([5,1])
    
    with col1:
        with st.form(key='query8', clear_on_submit = True):
                st.write("Returns the average number of readmissions and rounds it. [AVG]")
                st.code("SELECT AVG(number_of_readmissions) as Avg_Number_of_Readmissions\nFROM hosp_info.readmission_reduction")
                submit_code = st.form_submit_button("Execute") 
            
    if submit_code:

        with open('queries/functions/AVG.sql') as f:
                contents = f.read()
                df = pandas_gbq.read_gbq(contents, project_id)
                st.table(df)

    with col2:
            # this line is a shortcut to clicking the hamburger menu to refresh
                st.button(key='Refresh8', label='Refresh screen')

#------Query9------
    with st.container():

        col1, col2 = st.columns([5,1])
    
    with col1:
        with st.form(key='query9', clear_on_submit = True):
                st.write("Returns all hospitals by satate name with FIPS code over 10 [HAVING]")
                st.code("SELECT COUNT(provider_id), state_name\nFROM hosp_info.measures_of_birth_and_death\nGROUP BY state_name\nHAVING COUNT(state_fips_code) > 10 ")
                submit_code = st.form_submit_button("Execute") 
            
    if submit_code:

        with open('queries/functions//HAVING.sql') as f:
                contents = f.read()
                df = pandas_gbq.read_gbq(contents, project_id)
                st.table(df)
                #st.write(df)

    with col2:
            # this line is a shortcut to clicking the hamburger menu to refresh
                st.button(key='Refresh9', label='Refresh screen')