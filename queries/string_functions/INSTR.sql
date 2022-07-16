SELECT measure_name,
INSTR(measure_name, 's') AS First_occurence_of_s
FROM hosp_info.hospital_associated_infection
LIMIT 10
