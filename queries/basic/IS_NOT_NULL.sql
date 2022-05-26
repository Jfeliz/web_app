SELECT measure_name, score
FROM hosp_info.hospital_associated_infection
WHERE score IS NOT NULL
LIMIT 10;
