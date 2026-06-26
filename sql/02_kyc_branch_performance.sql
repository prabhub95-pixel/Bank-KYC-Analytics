SELECT 
    branch,
    COUNT(*) AS total_customers,
    SUM(CASE WHEN kyc_status = 'Completed' THEN 1 ELSE 0 END) AS kyc_completed,
    SUM(CASE WHEN kyc_status = 'Pending' THEN 1 ELSE 0 END) AS kyc_pending,
    ROUND(SUM(CASE WHEN kyc_status = 'Completed' THEN 1 ELSE 0 END) * 100.0 / COUNT(*), 2) AS completion_rate_pct
FROM bank_kyc_dataset
GROUP BY branch
ORDER BY completion_rate_pct DESC;
