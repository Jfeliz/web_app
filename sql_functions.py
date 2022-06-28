#SQL functions page

#load libraries
import streamlit as st
import pandas_gbq
from google.cloud import bigquery
from google.oauth2 import service_account

#read credentails for BigQuery access
credentials = service_account.Credentials.from_service_account_info(
    st.secrets["gcp_service_account"]
)
client = bigquery.Client(credentials=credentials)
project_id = 'web-app-341703'

def app():
    st.subheader('SQL - Functions')
    
# The following lines create a 2 column layout for a query (incl. what is does, the T-SQL syntax used and display of the query) and a refresh button

#------Query1------
    with st.container():

        col1, col2 = st.columns([5,1])
    
    with col1:
        with st.form(key='query1', clear_on_submit = True):
                st.write("This query selects the maximum predicted readmission rate for all providers. [MAX]")
                st.code("SELECT ROUND(MAX(predicted_readmission_rate), 1) AS Max_Readmission_Rate\nFROM hosp_info.readmission_reduction")
                submit_code = st.form_submit_button("Execute") 
            
    if submit_code:

        with open('queries/functions/MAX.sql') as f:
                contents = f.read()
                df = pandas_gbq.read_gbq(contents, project_id, credentials=credentials)
                st.table(df)

    with col2:
            # this line is a shortcut to clicking the hamburger menu to refresh
                st.button(key='Refresh1', label='Refresh screen')

#------Query2------
    with st.container():

        col1, col2 = st.columns([5,1])
    
    with col1:
        with st.form(key='query2', clear_on_submit = True):
                st.write("This query counts the nubmer of hospitals in California. [COUNT]")
                st.code("SELECT hospital_name, COUNT(*) AS Number_of_Hospitals_in_Calif\nFROM hosp_info.hospital_general_information\nWHERE state = 'CA'\nGROUP BY hospital_name")
                submit_code = st.form_submit_button("Execute") 
            
    if submit_code:

        with open('queries/functions/COUNT.sql') as f:
                contents = f.read()
                df = pandas_gbq.read_gbq(contents, project_id, credentials=credentials)
                st.table(df)

    with col2:
            # this line is a shortcut to clicking the hamburger menu to refresh
                st.button(key='Refresh2', label='Refresh screen')

#------Query3------
    with st.container():

        col1, col2 = st.columns([5,1])
    
    with col1:
        with st.form(key='query3', clear_on_submit = True):
                st.write("This query returns the length of characters in the hospital name. [LENGTH]")
                st.code("SELECT hospital_name, LENGTH(hospital_name) AS Number_of_Characters\nFROM hosp_info.hospital_general_information\nLIMIT 10")
                submit_code = st.form_submit_button("Execute") 
            
    if submit_code:

        with open('queries/functions/LENGTH.sql') as f:
                contents = f.read()
                df = pandas_gbq.read_gbq(contents, project_id, credentials=credentials)
                st.table(df)
 
    with col2:
            # this line is a shortcut to clicking the hamburger menu to refresh
                st.button(key='<unique name>', label='Refresh screen')

#------Query4------
    with st.container():

        col1, col2 = st.columns([5,1])
    
    with col1:
        with st.form(key='query4', clear_on_submit = True):
                st.write("Returns the minimum life expectancy in the state of Alabama. [MIN]")
                st.code("SELECT ROUND(MIN(avg_life_expect), 1) AS Min_Avg_Life_Expectancy\nFROM hosp_info.measures_of_birth_and_death\nWHERE state_name = 'Alabama'")
                submit_code = st.form_submit_button("Execute") 
            
    if submit_code:

        with open('queries/functions/MIN.sql') as f:
                contents = f.read()
                df = pandas_gbq.read_gbq(contents, project_id, credentials=credentials)
                st.table(df)

    with col2:
            # this line is a shortcut to clicking the hamburger menu to refresh
                st.button(key='Refresh4', label='Refresh screen')

#------Query5------
    with st.container():

        col1, col2 = st.columns([5,1])
    
    with col1:
        with st.form(key='query5', clear_on_submit = True):
                st.write("Returns sum of discharges from all hospitals [SUM]")
                st.code("SELECT SUM(number_of_discharges) AS Sum_of_Deaths_all_Hospitals \nFROM hosp_info.readmission_reduction")
                submit_code = st.form_submit_button("Execute") 
            
    if submit_code:

        with open('queries/functions/SUM.sql') as f:
                contents = f.read()
                df = pandas_gbq.read_gbq(contents, project_id, credentials=credentials)
                st.table(df)
 
    with col2:
            # this line is a shortcut to clicking the hamburger menu to refresh
                st.button(key='Refresh5', label='Refresh screen')

#------Query6------
    with st.container():

        col1, col2 = st.columns([5,1])
    
    with col1:
        with st.form(key='query6', clear_on_submit = True):
                st.write("This query rounds the infant mortality rate for the the state of Alabama. [ROUND]")
                st.code("SELECT ROUND(AVG(infant_mortality), 1) AS Infant_Mortality \nFROM hosp_info.measures_of_birth_and_death\nWHERE state_name = 'Alabama'")
                submit_code = st.form_submit_button("Execute") 
            
    if submit_code:

        with open('queries/functions/ROUND.sql') as f:
                contents = f.read()
                df = pandas_gbq.read_gbq(contents, project_id, credentials=credentials)
                st.table(df)

    with col2:
            # this line is a shortcut to clicking the hamburger menu to refresh
                st.button(key='Refresh6', label='Refresh screen')

#------Query7------
    with st.container():

        col1, col2 = st.columns([3,1])
    
    with col1:
        with st.form(key='query7', clear_on_submit = True):
                st.write("Returns the number of providers in each city and state, then groups by city and state. [GROUP BY] ")
                st.code("SELECT COUNT (DISTINCT(provider_name) AS Number_of_Providers, city, state\nFROM hosp_info.nursing_home_provider_info\nGROUP BY city, state\nLIMIT 25")
                submit_code = st.form_submit_button("Execute") 
            
    if submit_code:

        with open('queries/functions/GROUPBY.sql') as f:
                contents = f.read()
                df = pandas_gbq.read_gbq(contents, project_id, credentials=credentials)
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
                st.code("SELECT ROUND(AVG(number_of_readmissions), 2) as Avg_Number_of_Readmissions\nFROM hosp_info.readmission_reduction")
                submit_code = st.form_submit_button("Execute") 
            
    if submit_code:

        with open('queries/functions/AVG.sql') as f:
                contents = f.read()
                df = pandas_gbq.read_gbq(contents, project_id, credentials=credentials)
                st.table(df)

    with col2:
            # this line is a shortcut to clicking the hamburger menu to refresh
                st.button(key='Refresh8', label='Refresh screen')

#------Query9------
    with st.container():

        col1, col2 = st.columns([5,1])
    
    with col1:
        with st.form(key='query9', clear_on_submit = True):
                st.write("Returns all hospitals by state name with FIPS code over 10 [HAVING]")
                st.code("SELECT COUNT(infant_mortality), state_name\nFROM hosp_info.measures_of_birth_and_death\nGROUP BY state_name\nHAVING COUNT(infant_mortality) > 5\nORDER BY state_name;")
                submit_code = st.form_submit_button("Execute")
    if submit_code:

        with open('queries/functions//HAVING.sql') as f:
                contents = f.read()
                df = pandas_gbq.read_gbq(contents, project_id, credentials=credentials)
                st.table(df)
                #st.write(df)

    with col2:
            # this line is a shortcut to clicking the hamburger menu to refresh
                st.button(key='Refresh9', label='Refresh screen')
