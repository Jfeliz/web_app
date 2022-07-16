SELECT provider_name, state, overall_rating, SUM(overall_rating)
  OVER (
    PARTITION BY state
    ORDER BY state
  ) AS Total_Rating
FROM hosp_info.nursing_home_provider_info
