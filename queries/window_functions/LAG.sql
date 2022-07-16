SELECT provider_name, calc_payment_amt,
LAG(calc_payment_amt, 1) OVER(
  PARTITION BY provider_name ORDER BY calc_payment_amt) as previous_calc_pmt_amt,
calc_payment_amt - LAG(calc_payment_amt, 1) OVER(
  PARTITION BY provider_name ORDER BY calc_payment_amt) AS diff_calc_paymnet_amt
FROM hosp_info.ep_provider_paid_ehr_subset
