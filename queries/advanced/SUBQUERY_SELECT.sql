SELECT provider_id, hospital_name, 
  (SELECT AVG(max_homicide) 
   FROM hosp_info.measures_of_birth_and_death) as avg_max_homicides
FROM hosp_info.hospital_general_information
LIMIT 25
