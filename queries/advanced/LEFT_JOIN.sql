SELECT max_homicide, state_name, hospital_name FROM hosp_info.measures_of_birth_and_death
LEFT JOIN hosp_info.hospital_general_information
ON measures_of_birth_and_death.provider_id = hospital_general_information.provider_id
WHERE max_homicide BETWEEN 15.0 AND 18.0
LIMIT 25
