SELECT provider_name, provider_state, calc_payment_amt,
 NTH_VALUE(provider_name, 3) OVER(
   PARTITION BY provider_state 
   ORDER BY calc_payment_amt DESC) AS Third_Highest_Payment
 FROM hosp_info.ep_provider_paid_ehr_subset
