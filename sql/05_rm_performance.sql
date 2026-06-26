SELECT 
    relationship_manager,
    COUNT(*) AS total_customers,
    SUM(CASE WHEN kyc_status = 'Completed' THEN 1 ELSE 0 END) AS kyc_completed,
    SUM(CASE WHEN kyc_status = 'Pending' THEN 1 ELSE 0 END) AS kyc_pending,
    SUM(CASE WHEN sla_breached = 'Yes' THEN 1 ELSE 0 END) AS sla_breached,
    ROUND(SUM(CASE WHEN kyc_status = 'Completed' THEN 1 ELSE 0 END) * 100.0 / COUNT(*), 2) AS kyc_completion_pct,
    ROUND(SUM(CASE WHEN sla_breached = 'Yes' THEN 1 ELSE 0 END) * 100.0 / COUNT(*), 2) AS sla_breach_pct
FROM bank_kyc_dataset
GROUP BY relationship_manager
ORDER BY kyc_completion_pct DESC;
