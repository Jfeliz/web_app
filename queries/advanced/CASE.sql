SELECT provider_id, number_of_readmissions,
CASE
    WHEN number_of_readmissions > 50 THEN 'Urgent need to assess current resources for optimal patient care'
    WHEN number_of_readmissions = 50 THEN 'Resources should be adequate to provide optimal care for patients'
    ELSE 'Readmission rate should not jeopardize hospital resources' 
END AS ReadmissionAssessment
FROM `web-app-341703.hosp_info.readmission_reduction`
WHERE number_of_readmissions NOT IN (0)
LIMIT 25
