SELECT COUNT(provider_id), state_name
FROM hosp_info.measures_of_birth_and_death
GROUP BY state_name
HAVING COUNT(state_fips_code) > 10 
