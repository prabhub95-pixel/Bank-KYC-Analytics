SELECT 
    COUNT(*) AS total_customers,
    SUM(CASE WHEN kyc_status = 'Completed' THEN 1 ELSE 0 END) AS kyc_completed,
    SUM(CASE WHEN kyc_status = 'Pending' THEN 1 ELSE 0 END) AS kyc_pending,
    SUM(CASE WHEN kyc_status = 'Rejected' THEN 1 ELSE 0 END) AS kyc_rejected,
    SUM(CASE WHEN kyc_status = 'Expired' THEN 1 ELSE 0 END) AS kyc_expired,
    ROUND(SUM(CASE WHEN kyc_status = 'Completed' THEN 1 ELSE 0 END) * 100.0 / COUNT(*), 2) AS kyc_completion_rate_pct
FROM bank_kyc_dataset;
