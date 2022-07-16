SELECT 
  CONCAT('CLABSI Lower Confidence Limit',';', ' ','HAI_1_CI_LOWER') 
  AS Concat
FROM hosp_info.hospital_associated_infection
LIMIT 10
