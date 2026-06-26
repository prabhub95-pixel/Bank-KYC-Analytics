SELECT 
    account_type,
    COUNT(*) AS total_customers,
    SUM(CASE WHEN kyc_status = 'Completed' THEN 1 ELSE 0 END) AS kyc_completed,
    SUM(CASE WHEN kyc_status = 'Pending' THEN 1 ELSE 0 END) AS kyc_pending,
    SUM(CASE WHEN sla_breached = 'Yes' THEN 1 ELSE 0 END) AS sla_breached,
    ROUND(AVG(account_balance), 2) AS avg_balance,
    ROUND(SUM(CASE WHEN kyc_status = 'Completed' THEN 1 ELSE 0 END) * 100.0 / COUNT(*), 2) AS kyc_completion_pct
FROM bank_kyc_dataset
GROUP BY account_type
ORDER BY avg_balance DESC;
