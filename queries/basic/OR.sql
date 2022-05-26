SELECT hospital_name, city, state, county_name, hospital_type, hospital_ownership
FROM hosp_info.hospital_general_information 
WHERE (state='CA' OR state='CO') AND hospital_type='ACUTE CARE - VETERANS ADMINISTRATION'
