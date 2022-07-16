#sql_window_functions

#load necessary modules
import pandas_gbq
import streamlit as st
from google.cloud import bigquery
from google.oauth2 import service_account

#read credentails for BigQuery access
credentials = service_account.Credentials.from_service_account_info(
    st.secrets["gcp_service_account"]
)
client = bigquery.Client(credentials=credentials)
project_id = 'web-app-341703'

#define the function
def app():
    st.subheader('SQL - Window Functions')
    
#------Query1------

    with st.container():

        col1, col2 = st.columns([5,1])
    
    with col1:
        with st.form(key='query1', clear_on_submit = True):
                st.write("Returns the calculated payment amount for earch row, then returns a running total each provider's calculated payment anount. [SUM, OVER, PARTITION BY]")
                st.code("SELECT provider_name, provider_state, calc_payment_amt,\nSUM(calc_payment_amt) OVER(\n  PARTITION BY provider_name\n  ORDER BY calc_payment_amt) AS Salary_Sum\nFROM hosp_info.ep_provider_paid_ehr_subset ")
                submit_code = st.form_submit_button("Execute") 
            
    if submit_code:

        with open('queries/window_functions/SUM.sql') as f:
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
                st.write("Returns each provider's calculated payment amounts, ranks the number of times the amounts appear, and then displays them in descending order. [ROW_NUMBER and RANK]")
                st.code("SELECT provider_name, provider_state, calc_payment_amt, \n   ROW_NUMBER() OVER(PARTITION BY provider_name \n                ORDER BY calc_payment_amt) AS Row,\n   RANK() OVER(PARTITION BY provider_name \n                ORDER BY calc_payment_amt) AS Rank\nFROM hosp_info.ep_provider_paid_ehr_subset")
                submit_code = st.form_submit_button("Execute") 
            
    if submit_code:

        with open('queries/window_functions/ROW_RANK.sql') as f:
                contents = f.read()
                df = pandas_gbq.read_gbq(contents, project_id, credentials=credentials)
                st.table(df)

    with col2:
                st.button(key='Refresh2', label='Refresh screen')

#------Query3------
#create containers and columns for the form contents
    with st.container():

        col1, col2 = st.columns([5,1])
    
    with col1:
        with st.form(key='query3', clear_on_submit = True):
                st.write("Returns the quartile for the providers n the state of Maryland based on the calculated payment amount. [NTILE]")
                st.write("The window function was used in this subquery to isolate the results to a smaller subset of the state of Maryland, which doesn't allow the use of WHERE in it.")
                st.code("SELECT t.*\nFROM (SELECT provider_name, provider_state, calc_payment_amt,\nNTILE (14) OVER(\n  ORDER BY provider_state, calc_payment_amt\n) AS Quartile\nFROM hosp_info.ep_provider_paid_ehr_subset) AS t\nWHERE provider_state = 'Maryland'")
                submit_code = st.form_submit_button("Execute") 
            
    if submit_code:

        with open('queries/window_functions/NTILE.sql') as f:
                contents = f.read()
                df = pandas_gbq.read_gbq(contents, project_id, credentials=credentials)
                st.table(df)

    with col2:
            # this line is a shortcut to clicking the hamburger menu to refresh
                st.button(key='Refresh3', label='Refresh screen')

#------Query4------
#create containers and columns for the form contents
    with st.container():

        col1, col2 = st.columns([5,1])
    
    with col1:
        with st.form(key='query4', clear_on_submit = True):
                st.write("Returns providers that have the second highest calculated payment amount [NTH VALUE]")
                st.code("SELECT provider_name, provider_state, calc_payment_amt,\n NTH_VALUE(provider_name, 3) OVER(\n   PARTITION BY provider_state \n   ORDER BY calc_payment_amt DESC) AS Third_Highest_Payment\n FROM hosp_info.ep_provider_paid_ehr_subset")
                submit_code = st.form_submit_button("Execute") 
            
    if submit_code:

        with open('queries/window_functions/NTH_VALUE.sql') as f:
                contents = f.read()
                df = pandas_gbq.read_gbq(contents, project_id, credentials=credentials)
                st.table(df)

    with col2:
            # this line is a shortcut to clicking the hamburger menu to refresh
                st.button(key='Refresh4', label='Refresh screen')

#------Query5------
#create containers and columns for the form contents
    with st.container():

        col1, col2 = st.columns([5,1])
    
    with col1:
        with st.form(key='query5', clear_on_submit = True):
                st.write("Returns the distinct rank for each ranked row for each provider's calculated payment amount. [DENSE RANK]")
                st.code("SELECT provider_name, provider_state, calc_payment_amt, \n    ROW_NUMBER() OVER(PARTITION BY provider_name \n                ORDER BY calc_payment_amt) AS Row,\n    RANK() OVER(PARTITION BY provider_name \n                ORDER BY calc_payment_amt) AS Rank,\n    DENSE_RANK() OVER(PARTITION BY provider_name \n                ORDER BY calc_payment_amt) AS Dense_Rank\nFROM hosp_info.ep_provider_paid_ehr_subset")
                submit_code = st.form_submit_button("Execute") 
            
    if submit_code:

        with open('queries/window_functions/DENSE_RANK.sql') as f:
                contents = f.read()
                df = pandas_gbq.read_gbq(contents, project_id, credentials=credentials)
                st.table(df)

    with col2:
            # this line is a shortcut to clicking the hamburger menu to refresh
                st.button(key='Refresh5', label='Refresh screen')

#------Query6------
#create containers and columns for the form contents
    with st.container():

        col1, col2 = st.columns([5,1])
    
    with col1:
        with st.form(key='query6', clear_on_submit = True):
                st.write("Returns the difference of the previous calc payment amounts for each provider, where applicable. [LAG]")
                st.code("SELECT provider_name, calc_payment_amt,\nLAG(calc_payment_amt, 1) OVER(\n  PARTITION BY provider_name ORDER BY calc_payment_amt) as previous_calc_pmt_amt,\ncalc_payment_amt - LAG(calc_payment_amt, 1) OVER(\n  PARTITION BY provider_name ORDER BY calc_payment_amt) AS diff_calc_paymnet_amt\nFROM hosp_info.ep_provider_paid_ehr_subset")
                submit_code = st.form_submit_button("Execute") 
            
    if submit_code:

        with open('queries/window_functions/LAG.sql') as f:
                contents = f.read()
                df = pandas_gbq.read_gbq(contents, project_id, credentials=credentials)
                st.table(df)

    with col2:
            # this line is a shortcut to clicking the hamburger menu to refresh
                st.button(key='Refresh6', label='Refresh screen')

#------Query7------
#create containers and columns for the form contents
    with st.container():

        col1, col2 = st.columns([5,1])
    
    with col1:
        with st.form(key='query7', clear_on_submit = True):
                st.write("Returns succeeding calculated payment amounts for each provider, where applicable. [LEAD]")
                st.code("SELECT provider_name, calc_payment_amt, \nLEAD(calc_payment_amt, 1) OVER(\n  PARTITION BY provider_name ORDER BY calc_payment_amt) as next_calc_pmt_amt\nFROM hosp_info.ep_provider_paid_ehr_subset")
                submit_code = st.form_submit_button("Execute") 
            
    if submit_code:

        with open('queries/window_functions/LEAD.sql') as f:
                contents = f.read()
                df = pandas_gbq.read_gbq(contents, project_id, credentials=credentials)
                st.table(df)

    with col2:
            # this line is a shortcut to clicking the hamburger menu to refresh
                st.button(key='Refresh7', label='Refresh screen')