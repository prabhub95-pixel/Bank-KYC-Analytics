# 🏦 Bank Customer KYC & Operations Analytics

A end-to-end data analytics project simulating a real-world banking KYC 
and compliance reporting environment — built using Python, SQL, and Power BI.

---

## 📌 Project Objective

To analyse customer KYC compliance, SLA adherence, risk segmentation, 
and branch performance across a simulated banking dataset of 5,000 customers.

---

## 🛠 Tools & Technologies

| Tool        | Usage                                      |
|-------------|--------------------------------------------|
| Python      | Synthetic dataset generation (Pandas)      |
| SQL         | Data analysis & compliance reporting       |
| Power BI    | Interactive dashboard & KPI visualisation  |
| SQLite      | Local database to run SQL queries          |
| GitHub      | Version control & project showcase         |

---

## 📁 Project Structure

```
bank-kyc-analytics/
├── data_generator.py        # Python script to generate dataset
├── sql/
│   ├── 01_kyc_completion_analysis.sql
│   ├── 02_sla_breach_analysis.sql
│   ├── 03_risk_segmentation.sql
│   ├── 04_branch_performance.sql
│   └── 05_rm_performance.sql
├── dashboard/
│   └── 🔗 [View Live Dashboard] [https://public.tableau.com/app/profile/prabhu.b1145/viz/PJ_17829055060960/KYCComplianceDashboard?publish=yes]
└── README.md
```

---

## 📊 Dataset Overview

- **Records:** 5,000 customers
- **Date Range:** 2020 – 2024
- **Branches:** 10 across Chennai, Mumbai, Bengaluru, Hyderabad, Delhi

| Column               | Description                              |
|----------------------|------------------------------------------|
| customer_id          | Unique customer identifier               |
| account_number       | Bank account number                      |
| branch               | Branch name and city                     |
| account_type         | Savings / Current / NRI / Corporate / FD |
| kyc_status           | Completed / Pending / Rejected / Expired |
| sla_breached         | Whether KYC crossed 7-day SLA (Yes/No)   |
| risk_category        | Low / Medium / High / Very High          |
| relationship_manager | Assigned RM name                         |

---

## 🔍 Key Analysis Areas

1. KYC completion rate by branch
2. SLA breach analysis by branch & account type
3. High-risk customer segmentation
4. Month-on-month onboarding trends
5. Pending KYC ageing report
6. Relationship Manager performance
7. Risk vs SLA breach correlation

---

## 📈 Dashboard Preview

![Dashboard Preview](dashboard/screenshots/dashboard_preview.png)


---

## ▶️ How to Run

1. Clone the repository
2. Run `data_generator.py` to generate the dataset
3. Load `bank_kyc_dataset.csv` into SQLite using DB Browser
4. Run SQL files in the `sql/` folder sequentially
5. Open Power BI dashboard from the `dashboard/` folder

---

## 👤 Author

**Prabhu Bhadrinarayanan**  
Senior Data Analyst | SQL · Power BI · Tableau | Banking & KYC  
📧 prabhub95@gmail.com  
🔗 [LinkedIn](https://www.linkedin.com/in/prabhu-b-37a288b0)
