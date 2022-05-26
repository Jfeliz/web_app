SELECT hospital_general_information.hospital_name, measures_of_birth_and_death.state_name, measures_of_birth_and_death.lbw
FROM hosp_info.hospital_general_information
RIGHT JOIN hosp_info.measures_of_birth_and_death
ON hospital_general_information.provider_id = measures_of_birth_and_death.provider_id
WHERE state_name = 'California' AND lbw BETWEEN 6.2 AND 7.1
