SELECT 
    branch,
    COUNT(*) AS total_customers,
    SUM(CASE WHEN sla_breached = 'Yes' THEN 1 ELSE 0 END) AS sla_breached_count,
    SUM(CASE WHEN sla_breached = 'No' THEN 1 ELSE 0 END) AS sla_met_count,
    ROUND(SUM(CASE WHEN sla_breached = 'Yes' THEN 1 ELSE 0 END) * 100.0 / COUNT(*), 2) AS breach_rate_pct
FROM bank_kyc_dataset
GROUP BY branch
ORDER BY breach_rate_pct DESC;
