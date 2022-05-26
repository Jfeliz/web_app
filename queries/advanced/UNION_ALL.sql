SELECT average_medicare_payments FROM hosp_info.ipps_2011
UNION ALL
SELECT average_medicare_payments FROM hosp_info.ipps_2012
ORDER BY average_medicare_payments ASC
LIMIT 25
