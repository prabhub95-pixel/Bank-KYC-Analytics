SELECT 
    customer_id,
    customer_name,
    branch,
    account_type,
    risk_category,
    relationship_manager,
    onboarding_date,
    kyc_status,
    CAST(JULIANDAY('2025-01-01') - JULIANDAY(onboarding_date) AS INTEGER) AS days_since_onboarding
FROM bank_kyc_dataset
WHERE kyc_status IN ('Pending', 'Under Review', 'Expired')
ORDER BY days_since_onboarding DESC
LIMIT 20;
