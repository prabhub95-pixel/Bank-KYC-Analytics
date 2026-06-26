SELECT 
    risk_category,
    COUNT(*) AS total_customers,
    SUM(CASE WHEN kyc_status = 'Completed' THEN 1 ELSE 0 END) AS kyc_completed,
    SUM(CASE WHEN kyc_status = 'Pending' THEN 1 ELSE 0 END) AS kyc_pending,
    SUM(CASE WHEN sla_breached = 'Yes' THEN 1 ELSE 0 END) AS sla_breached_count,
    ROUND(SUM(CASE WHEN kyc_status = 'Completed' THEN 1 ELSE 0 END) * 100.0 / COUNT(*), 2) AS kyc_completion_pct,
    ROUND(SUM(CASE WHEN sla_breached = 'Yes' THEN 1 ELSE 0 END) * 100.0 / COUNT(*), 2) AS sla_breach_pct
FROM bank_kyc_dataset
GROUP BY risk_category
ORDER BY 
    CASE risk_category 
        WHEN 'Very High' THEN 1 
        WHEN 'High' THEN 2 
        WHEN 'Medium' THEN 3 
        WHEN 'Low' THEN 4 
    END;
