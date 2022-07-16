SELECT provider_name, calc_payment_amt, 
LEAD(calc_payment_amt, 1) OVER(
  PARTITION BY provider_name ORDER BY calc_payment_amt) as next_calc_pmt_amt
FROM hosp_info.ep_provider_paid_ehr_subset
