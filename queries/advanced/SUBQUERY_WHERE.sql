SELECT *
FROM hosp_info.hospital_general_information
WHERE provider_id IN (SELECT provider_id FROM hosp_info.hcahps_survey WHERE hcahps_answer_description LIKE ('%Room was%'))
LIMIT 25
