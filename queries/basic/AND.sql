SELECT hospital_name, city, state, county_name, hospital_type, hospital_ownership 
FROM hosp_info.hospital_general_information 
WHERE state='FL' AND city='Orlando' AND hospital_type = 'Acute Care Hospitals'
