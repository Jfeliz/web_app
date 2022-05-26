SELECT hospital_name
FROM hosp_info.hospital_general_information
WHERE EXISTS
    (SELECT expected_readmission_rate 
    FROM hosp_info.readmission_reduction
    WHERE hospital_general_information.provider_id = readmission_reduction.provider_id AND expected_readmission_rate > 25.0)
