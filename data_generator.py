"""
Bank Customer KYC & Operations Dataset Generator
Project: Bank Customer KYC & Operations Analytics
Author: Prabhu Bhadrinarayanan
"""

import pandas as pd
import random
from datetime import datetime, timedelta

random.seed(42)

# ── Config ──────────────────────────────────────────────
NUM_RECORDS = 5000

BRANCHES = [
    "Chennai - Anna Nagar", "Chennai - T Nagar", "Chennai - Ambattur",
    "Chennai - Adyar", "Mumbai - Andheri", "Mumbai - Bandra",
    "Bengaluru - Koramangala", "Bengaluru - Whitefield",
    "Hyderabad - Hitech City", "Delhi - Connaught Place"
]

ACCOUNT_TYPES = ["Savings", "Current", "NRI", "Corporate", "Fixed Deposit"]

KYC_STATUSES = ["Completed", "Pending", "Rejected", "Under Review", "Expired"]
KYC_WEIGHTS  = [0.60, 0.18, 0.07, 0.10, 0.05]

RISK_CATEGORIES = ["Low", "Medium", "High", "Very High"]
RISK_WEIGHTS    = [0.50, 0.30, 0.15, 0.05]

RELATIONSHIP_MANAGERS = [
    "Anitha R", "Suresh K", "Divya M", "Ramesh P",
    "Priya S", "Karthik V", "Meena T", "Vijay N"
]

DOCUMENT_TYPES = ["Aadhaar + PAN", "Passport + PAN", "Voter ID + PAN", "Driving Licence + PAN"]

SLA_DAYS = 7   # KYC must be completed within 7 days of onboarding

# ── Helpers ─────────────────────────────────────────────
def random_date(start_year=2020, end_year=2024):
    start = datetime(start_year, 1, 1)
    end   = datetime(end_year, 12, 31)
    return start + timedelta(days=random.randint(0, (end - start).days))

def kyc_completion_date(onboarding_date, kyc_status):
    if kyc_status in ["Completed", "Rejected"]:
        days_taken = random.randint(1, 15)
        return onboarding_date + timedelta(days=days_taken)
    return None

def sla_breached(onboarding_date, completion_date, kyc_status):
    if kyc_status == "Pending" or kyc_status == "Under Review":
        # Check if more than SLA_DAYS have passed since onboarding
        days_open = (datetime(2025, 1, 1) - onboarding_date).days
        return "Yes" if days_open > SLA_DAYS else "No"
    if completion_date:
        return "Yes" if (completion_date - onboarding_date).days > SLA_DAYS else "No"
    return "No"

def generate_customer_id(i):
    return f"CUST{str(i+1).zfill(5)}"

def generate_account_number(i):
    return f"ACC{str(random.randint(1000000000, 9999999999))}"

# ── Generate Data ────────────────────────────────────────
first_names = [
    "Arjun", "Priya", "Karthik", "Deepa", "Suresh", "Anitha", "Ramesh", "Kavya",
    "Vijay", "Meena", "Arun", "Divya", "Sathish", "Nithya", "Ganesh", "Lakshmi",
    "Murugan", "Sangeetha", "Bala", "Revathi", "Senthil", "Bhavani", "Dinesh",
    "Saranya", "Manoj", "Geetha", "Praveen", "Sindhu", "Rajesh", "Uma"
]

last_names = [
    "Kumar", "Sharma", "Raj", "Patel", "Iyer", "Nair", "Reddy", "Singh",
    "Pillai", "Menon", "Venkat", "Bala", "Murthy", "Das", "Rao", "Krishnan",
    "Sundaram", "Rajan", "Natarajan", "Subramaniam"
]

records = []
for i in range(NUM_RECORDS):
    first     = random.choice(first_names)
    last      = random.choice(last_names)
    full_name = f"{first} {last}"

    onboarding_date = random_date(2020, 2024)
    kyc_status      = random.choices(KYC_STATUSES, weights=KYC_WEIGHTS)[0]
    completion_date = kyc_completion_date(onboarding_date, kyc_status)
    breach          = sla_breached(onboarding_date, completion_date, kyc_status)
    days_to_complete = (completion_date - onboarding_date).days if completion_date else None

    account_type    = random.choice(ACCOUNT_TYPES)
    risk_category   = random.choices(RISK_CATEGORIES, weights=RISK_WEIGHTS)[0]
    branch          = random.choice(BRANCHES)
    rm              = random.choice(RELATIONSHIP_MANAGERS)
    doc_type        = random.choice(DOCUMENT_TYPES)

    # Account balance (varies by account type)
    if account_type == "Corporate":
        balance = round(random.uniform(500000, 50000000), 2)
    elif account_type == "NRI":
        balance = round(random.uniform(100000, 5000000), 2)
    elif account_type == "Fixed Deposit":
        balance = round(random.uniform(50000, 2000000), 2)
    else:
        balance = round(random.uniform(1000, 500000), 2)

    records.append({
        "customer_id":          generate_customer_id(i),
        "account_number":       generate_account_number(i),
        "customer_name":        full_name,
        "branch":               branch,
        "account_type":         account_type,
        "onboarding_date":      onboarding_date.strftime("%Y-%m-%d"),
        "kyc_status":           kyc_status,
        "kyc_completion_date":  completion_date.strftime("%Y-%m-%d") if completion_date else None,
        "days_to_complete_kyc": days_to_complete,
        "sla_breached":         breach,
        "risk_category":        risk_category,
        "document_type":        doc_type,
        "relationship_manager": rm,
        "account_balance":      balance,
        "onboarding_year":      onboarding_date.year,
        "onboarding_month":     onboarding_date.strftime("%b"),
        "onboarding_quarter":   f"Q{((onboarding_date.month - 1) // 3) + 1}",
    })

df = pd.DataFrame(records)

# ── Save ─────────────────────────────────────────────────
output_path = "/mnt/user-data/outputs/bank_kyc_dataset.csv"
df.to_csv(output_path, index=False)

# ── Summary ──────────────────────────────────────────────
print("=" * 55)
print("  Bank KYC Dataset Generated Successfully!")
print("=" * 55)
print(f"  Total Records      : {len(df):,}")
print(f"  Columns            : {len(df.columns)}")
print(f"  Date Range         : 2020 – 2024")
print(f"  Saved to           : {output_path}")
print()
print("  KYC Status Breakdown:")
for status, count in df["kyc_status"].value_counts().items():
    pct = count / len(df) * 100
    print(f"    {status:<15} {count:>5,}  ({pct:.1f}%)")
print()
print("  SLA Breach Summary:")
for val, count in df["sla_breached"].value_counts().items():
    pct = count / len(df) * 100
    print(f"    Breached = {val:<5} {count:>5,}  ({pct:.1f}%)")
print()
print("  Risk Category Breakdown:")
for risk, count in df["risk_category"].value_counts().items():
    pct = count / len(df) * 100
    print(f"    {risk:<12} {count:>5,}  ({pct:.1f}%)")
print("=" * 55)
