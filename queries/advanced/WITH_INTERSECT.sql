WITH a AS (
SELECT total_discharges
FROM hosp_info.ipps_2011 AS n
), b AS (
SELECT total_discharges AS n
FROM hosp_info.ipps_2012
)
 
SELECT * FROM a
 
INTERSECT DISTINCT
 
SELECT * FROM b
 
ORDER BY total_discharges ASC
LIMIT 25
