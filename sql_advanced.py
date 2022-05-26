#app2.py
import streamlit as st
import pandas_gbq
import os

os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = '/home/mark/Documents/Data_Projects/web-app/web-app-341703-626adddc7d5a.json'
project_id = 'web-app-341703'

def app():
    st.subheader('SQL - Advanced')
    st.write("Here are the advanced SQL queries that I created.")
    
#------Query1------
    with st.container():

        col1, col2 = st.columns([5,1])
    
    with col1:
        with st.form(key='query1', clear_on_submit = True):
                st.write("Return all records but limit results to 5 [LIMIT]")
                st.code("SELECT * \nFROM hosp_info.hospital_general_information \nLIMIT 5")
                submit_code = st.form_submit_button("Execute") 
            
    if submit_code:

        with open('queries/advanced/LIMIT.sql') as f:
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
                st.write("Return all records for hospitals with the name that starts with A [LIKE]")
                st.code("SELECT *\nFROM hosp_info.hospital_general_information\nWHERE state LIKE 'A%'\nLIMIT 10")
                submit_code = st.form_submit_button("Execute") 
            
    if submit_code:

        with open('queries/advanced/LIKE.sql') as f:
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
                st.write("Return all hospital names and the number of characters in each [LENGTH with alias AS]")
                st.code("SELECT hospital_name, LENGTH(hospital_name) as number_of_characters\nFROM hosp_info.hospital_general_information\nLIMIT 10")
                submit_code = st.form_submit_button("Execute") 
            
    if submit_code:

        with open('queries/functions/LENGTH.sql') as f:
                contents = f.read()
                df = pandas_gbq.read_gbq(contents, project_id)
                st.table(df)

    with col2:
            # this line is a shortcut to clicking the hamburger menu to refresh
                st.button(key='Refresh3', label='Refresh screen')

            
#------Query4------
    with st.container():

        col1, col2 = st.columns([5,1])
    
    with col1:
        with st.form(key='query4', clear_on_submit = True):
                st.write("Returns the count of hospitals in CA [COUNT]")
                st.code("SELECT COUNT(*) AS Number_of_Hospitals_in_Calif\nFROM hosp_info.hospital_general_information\nWHERE state = 'CA'")
                submit_code = st.form_submit_button("Execute") 
            
    if submit_code:

        with open('queries/functions/COUNT.sql') as f:
                contents = f.read()
                df = pandas_gbq.read_gbq(contents, project_id)
                st.table(df)

    with col2:
            # this line is a shortcut to clicking the hamburger menu to refresh
                st.button(key='Refresh4', label='Refresh screen')


#------Query4------
    with st.container():

        col1, col2 = st.columns([5,1])
    
    with col1:
        with st.form(key='query5', clear_on_submit = True):
                st.write("Return all records where condition was heart failure. [IN]")
                st.code("SELECT *\nFROM hosp_info.timely_and_effective_care\nWHERE condition IN\nLIMIT 10 ('Heart Failure')")
                submit_code = st.form_submit_button("Execute") 
            
    if submit_code:

        with open('queries/advanced/IN.sql') as f:
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
                st.write("Returns the percentage of survey answers between 50 and 90 [BETWEEN]")
                st.code("SELECT hcahps_question, hcahps_answer_description, hcahps_answer_percent\nFROM hosp_info.hcahps_survey\nWHERE hcahps_answer_percent BETWEEN 50 AND 90\nLIMIT 25")
                submit_code = st.form_submit_button("Execute") 
            
    if submit_code:

        with open('queries/advanced/BETWEEN.sql') as f:
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
                st.write("Returns all records like 'readmission' from readmissions, complications, deaths [Wildcards]")
                st.code("SELECT *\nFROM hosp_info.readmissions_complications_deaths\nWHERE measure_name LIKE '%readmission%'\nLIMIT 25")
                submit_code = st.form_submit_button("Execute") 
            
    if submit_code:

        with open('queries/advanced/WILDCARDS.sql') as f:
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
                st.write("Returns the similar payment weights between 2011 and 2012 IPPS [WITH and INTERSECT]")
                st.markdown("NOTE: This query includes the use of the WITH clause and DISTINCT statement to complete.")
                st.code("WITH a AS (\nSELECT total_discharges\nFROM hosp_info.ipps_2011 AS n\n), b AS (\nSELECT total_discharges AS n\nFROM hosp_info.ipps_2012\n)\nSELECT * FROM a\nINTERSECT DISTINCT\nSELECT * FROM b\nORDER BY total_discharges ASC\nLIMIT 25")
                submit_code = st.form_submit_button("Execute") 
            
    if submit_code:

        with open('queries/advanced/WITH_INTERSECT.sql') as f:
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
                st.write("Returns all number of readmissions equal to or greter than 50, ordered by state [INNER JOIN]")
                st.code("SELECT hospital_general_information.hospital_name,\nhospital_general_information.city,\nhospital_general_information.state,\nreadmission_reduction.number_of_readmissions\nFROM hosp_info.hospital_general_information\nINNER JOIN hosp_info.readmission_reduction\nON readmission_reduction.provider_id = hospital_general_information.provider_id\nWHERE number_of_readmissions >= 50\nORDER BY state\nLIMIT 25")
                submit_code = st.form_submit_button("Execute") 
            
    if submit_code:

        with open('queries/advanced/INNER_JOIN.sql') as f:
                contents = f.read()
                df = pandas_gbq.read_gbq(contents, project_id)
                st.table(df)

    with col2:
            # this line is a shortcut to clicking the hamburger menu to refresh
                st.button(key='Refresh9', label='Refresh screen')

#------Query10------
    with st.container():

        col1, col2 = st.columns([5,1])
    
    with col1:
        with st.form(key='query10', clear_on_submit = True):
                st.write("Returns low birth weights (between 6.2 and 7.1) across all hospitals in California [RIGHT JOIN]")
                st.code("SELECT hospital_general_information.hospital_name, measures_of_birth_and_death.state_name, measures_of_birth_and_death.lbw \nFROM hosp_info.hospital_general_information \nRIGHT JOIN hosp_info.measures_of_birth_and_death \nON hospital_general_information.provider_id = measures_of_birth_and_death.provider_id \nWHERE state_name = 'California' AND lbw BETWEEN 6.2 AND 7.1")
                submit_code = st.form_submit_button("Execute") 
            
    if submit_code:

        with open('queries/advanced/RIGHT_JOIN.sql') as f:
                contents = f.read()
                df = pandas_gbq.read_gbq(contents, project_id)
                st.table(df)

    with col2:
            # this line is a shortcut to clicking the hamburger menu to refresh
                st.button(key='Refresh10', label='Refresh screen')

#------Query11------
    with st.container():

        col1, col2 = st.columns([5,1])
    
    with col1:
        with st.form(key='query11', clear_on_submit = True):
                st.write("Returns patients presented to hospitals as homicides with the rate between 15.0 and 18.0 (LEFT JOIN]")
                st.markdown("This query has additional statements to represent the join and display null values.")
                st.code("SELECT max_homicide, state_name, hospital_name \nFROM hosp_info.measures_of_birth_and_death \nLEFT JOIN hosp_info.hospital_general_information \nON measures_of_birth_and_death.provider_id = hospital_general_information.provider_id \nWHERE max_homicide BETWEEN 15.0 AND 18.0 \nLIMIT 25")
                submit_code = st.form_submit_button("Execute") 
            
    if submit_code:

        with open('queries/advanced/LEFT_JOIN.sql') as f:
                contents = f.read()
                df = pandas_gbq.read_gbq(contents, project_id)
                st.table(df)

    with col2:
            # this line is a shortcut to clicking the hamburger menu to refresh
                st.button(key='Refresh11', label='Refresh screen')

#------Query12------
    with st.container():

        col1, col2 = st.columns([5,1])
    
    with col1:
        with st.form(key='query12', clear_on_submit = True):
                st.write("Returns the maximum low birth rate compared to the minimum low birth weight for each hospital [CROSS JOIN]")
                st.code("SELECT H.hospital_name, H.state, M.max_lbw, M.min_lbw \nFROM hosp_info.hospital_general_information H \nCROSS JOIN hosp_info.measures_of_birth_and_death M \nWHERE H.provider_id = M.provider_id \nORDER BY H.state ASC\nLIMIT 25")
                submit_code = st.form_submit_button("Execute") 
            
    if submit_code:

        with open('queries/advanced/CROSS_JOIN.sql') as f:
                contents = f.read()
                df = pandas_gbq.read_gbq(contents, project_id)
                st.table(df)

    with col2:
            # this line is a shortcut to clicking the hamburger menu to refresh
                st.button(key='Refresh12', label='Refresh screen')

#------Query13------
    with st.container():

        col1, col2 = st.columns([5,1])
    
    with col1:
        with st.form(key='query13', clear_on_submit = True):
                st.write("Returns all average medicare payments for 2011 and 2012 [UNION ALL]")
                st.code("SELECT average_medicare_payments FROM hosp_info.ipps_2011 \nUNION ALL \nSELECT average_medicare_payments FROM hosp_info.ipps_2012 \nORDER BY average_medicare_payments ASC\LIMIT 25")
                submit_code = st.form_submit_button("Execute") 
            
    if submit_code:

        with open('queries/advanced/UNION_ALL.sql') as f:
                contents = f.read()
                df = pandas_gbq.read_gbq(contents, project_id)
                st.table(df)

    with col2:
            # this line is a shortcut to clicking the hamburger menu to refresh
                st.button(key='Refresh13', label='Refresh screen')

#------Query14------
    with st.container():

        col1, col2 = st.columns([5,1])
    
    with col1:
        with st.form(key='query14', clear_on_submit = True):
                st.write("Returns all hospitals with a expected readmission rate of 25 percent or higher [WHERE EXISTS]")
                st.code("SELECT hospital_name \nFROM hosp_info.hospital_general_information \nWHERE EXISTS \n    (SELECT expected_readmission_rate\n    FROM hosp_info.readmission_reduction \n    WHERE hospital_general_information.provider_id = readmission_reduction.provider_id AND expected_readmission_rate > 25.0)")
                submit_code = st.form_submit_button("Execute") 
            
    if submit_code:

        with open('queries/advanced/WHERE_EXISTS.sql') as f:
                contents = f.read()
                df = pandas_gbq.read_gbq(contents, project_id)
                st.table(df)
                #st.write(df)

    with col2:
            # this line is a shortcut to clicking the hamburger menu to refresh
                st.button(key='Refresh14', label='Refresh screen')

#------Query15------
    with st.container():

        col1, col2 = st.columns([5,1])
    
    with col1:
        with st.form(key='query15', clear_on_submit = True):
                st.write("Returns readmission rates based on two conditions and recommendations: those with 50 or more readmissions and those with less than 50 readmissions [CASE]")
                st.code("SELECT provider_id, number_of_readmissions, \nCASE\n    WHEN number_of_readmissions > 50 THEN 'Urgent need to assess current resources for optimal patient care'\n    WHEN number_of_readmissions = 50 THEN 'Resources should be adequate to provide optimal care for patients'    \nELSE 'Readmission rate should not jeopardize hospital resources' \nEND AS ReadmissionAssessment\nFROM readmission_reduction\nWHERE number_of_readmissions NOT IN (0)\nLIMIT 25")
                submit_code = st.form_submit_button("Execute") 
            
    if submit_code:

        with open('queries/advanced/CASE.sql') as f:
                contents = f.read()
                df = pandas_gbq.read_gbq(contents, project_id)
                st.table(df)
                #st.write(df)

    with col2:
            # this line is a shortcut to clicking the hamburger menu to refresh
                st.button(key='Refresh15', label='Refresh screen')

#------Query16------
    with st.container():

        col1, col2 = st.columns([5,1])
    
    with col1:
        with st.form(key='<query16', clear_on_submit = True):
                st.write("The inner query returns the average number of homicides from the measures and deaths table. The outer query returns the hospitals that have those average maximum of homicdes. [SUBQUERY_SELECT and AVG]")
                st.code("SELECT provider_id, hospital_name, \n  (SELECT AVG(max_homicide) \n   FROM hosp_info.measures_of_birth_and_death) as avg_max_homicides \nFROM hosp_info.hospital_general_information")
                submit_code = st.form_submit_button("Execute") 
            
    if submit_code:

        with open('queries/advanced/SUBQUERY_SELECT.sql') as f:
                contents = f.read()
                df = pandas_gbq.read_gbq(contents, project_id)
                st.table(df)
                #st.write(df)

    with col2:
            # this line is a shortcut to clicking the hamburger menu to refresh
                st.button(key='Refresh16', label='Refresh screen')

#------Query17------
    with st.container():

        col1, col2 = st.columns([5,1])
    
    with col1:
        with st.form(key='query17', clear_on_submit = True):
                st.write("The inner query returns a count of all hospitals by provider ID and Hospital Name; the outer query returns the average number of hospitals by hospital name [SUBQUERY_FROM]")
                st.code("SELECT hospital_name, AVG(num_hospitals) FROM \n  (SELECT provider_id, hospital_name, COUNT(*) AS num_hospitals \n  FROM hosp_info.hospital_general_information \n  GROUP BY 1, 2) sub \nGROUP BY 1\nLIMIT 25")
                st.markdown('This query performs an aggregate of an aggreagte (i.e. average of the count)')
                submit_code = st.form_submit_button("Execute") 
            
    if submit_code:

        with open('queries/advanced/SUBQUERY_FROM.sql') as f:
                contents = f.read()
                df = pandas_gbq.read_gbq(contents, project_id)
                st.table(df)
                #st.write(df)

    with col2:
            # this line is a shortcut to clicking the hamburger menu to refresh
                st.button(key='Refresh17', label='Refresh screen')

#------Query18------
    with st.container():

        col1, col2 = st.columns([5,1])
    
    with col1:
        with st.form(key='query18', clear_on_submit = True):
                st.write("The inner query returns all the hospitals that were part of a survey and patient replied that the room was always clean. The outer query returns all records from the hospital general information table. [SUBQUERY_WHERE]")
                st.code("SELECT * \nFROM hosp_info.hospital_general_information \nWHERE provider_id IN (SELECT provider_id FROM hosp_info.hcahps_survey WHERE hcahps_answer_description \nLIKE ('%Room was%'))\nLIMIT 25")
                submit_code = st.form_submit_button("Execute") 
            
    if submit_code:

        with open('queries/advanced/SUBQUERY_WHERE.sql') as f:
                contents = f.read()
                df = pandas_gbq.read_gbq(contents, project_id)
                st.table(df)
                #st.write(df)

    with col2:
            # this line is a shortcut to clicking the hamburger menu to refresh
                st.button(key='Refresh18', label='Refresh screen')