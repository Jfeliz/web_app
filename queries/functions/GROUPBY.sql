SELECT COUNT(provnum) provider_name, city, state
FROM hosp_info.nursing_home_provider_info
GROUP BY city, state
LIMIT 10
