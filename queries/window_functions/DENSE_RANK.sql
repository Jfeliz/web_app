SELECT provider_name, provider_state, calc_payment_amt, 
    ROW_NUMBER() OVER(PARTITION BY provider_name 
                ORDER BY calc_payment_amt) AS Row,
    RANK() OVER(PARTITION BY provider_name 
                ORDER BY calc_payment_amt) AS Rank,
    DENSE_RANK() OVER(PARTITION BY provider_name 
                ORDER BY calc_payment_amt) AS Dense_Rank
FROM hosp_info.ep_provider_paid_ehr_subset
