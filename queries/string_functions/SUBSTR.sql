SELECT
  SUBSTR(footnote, 4, 7) AS Returned_word
FROM hosp_info.hospital_associated_infection
WHERE footnote IS NOT NULL
LIMIT 10
