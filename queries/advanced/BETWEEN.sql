SELECT hcahps_question, hcahps_answer_description, hcahps_answer_percent 
FROM hosp_info.hcahps_survey
WHERE hcahps_answer_percent BETWEEN 50 AND 90
LIMIT 25
