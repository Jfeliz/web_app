CREATE TEMP TABLE newtable1
(
  provider_npi INTEGER,
  provider_id INTEGER,
  hospital_name STRING,
  address STRING,
  city STRING,
  state STRING,
  state_code INTEGER,
  zipcode INTEGER,
  county_name STRING,
  phone_number STRING,
  hospital_type STRING,
  hospital_ownership STRING,
  emergency_services BOOLEAN,
);

INSERT INTO newtable
VALUES (9893458312, 1016, 'WASHINGTON MEDICAL CLINIC', '300 PARSONS STREET', 'PRESCOTT', 'AZ', 4, 86313, 'YAVAPAI', '(928)445-4734', 'ACUTE CARE - VETERANS ADMINISTRATION', 'Government Federal', false );

SELECT * FROM newtable1;
