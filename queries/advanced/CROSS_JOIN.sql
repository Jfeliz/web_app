SELECT H.hospital_name, H.state, M.max_lbw, M.min_lbw
FROM hosp_info.hospital_general_information H
CROSS JOIN hosp_info.measures_of_birth_and_death M
WHERE H.provider_id = M.provider_id
ORDER BY H.state ASC
LIMIT 25
