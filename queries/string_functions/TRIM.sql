SELECT
  TRIM(measure_id, '_1') as Trimmed_ID
FROM hosp_info.medicare_hospital_spending_per_patient
LIMIT 10;
