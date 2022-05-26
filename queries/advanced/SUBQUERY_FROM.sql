SELECT hospital_name, AVG(num_hospitals) FROM
  (SELECT provider_id, hospital_name, COUNT(*) AS num_hospitals
  FROM hosp_info.hospital_general_information
  GROUP BY 1, 2) sub
GROUP BY 1 
LIMIT 25
