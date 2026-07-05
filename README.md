# 🛡️ Internal Audit Risk Prioritization Dashboard

## 📌 Project Overview

This project presents an end-to-end Internal Audit Risk Prioritization solution developed using Python, SQL, and Power BI. The objective is to identify and prioritize high-risk branches for audit based on multiple risk factors and present actionable insights through an interactive dashboard.

---

## 🎯 Objectives

- Calculate branch-wise audit risk scores.
- Rank branches based on overall risk.
- Prioritize the Top 20 branches for audit.
- Analyze branch risk distribution.
- Monitor audit hours and estimated risk exposure.
- Support data-driven audit planning.

---

## 🛠️ Tools & Technologies

- Python (Pandas, NumPy)
- MySQL
- Power BI
- Excel

---

## 📊 Dashboard Features

### Page 1 – Executive Dashboard

- Total Branches
- Selected Branches
- Deferred Branches
- Average Risk Score
- Total Audit Hours
- Total Risk Exposure
- Average Risk Score by Branch Type
- Risk Tier Distribution
- Top 10 Audit Priority Branches
- City-wise Risk Exposure
- Interactive Slicers

### Page 2 – Branch Level Audit Analysis

- Branch Audit Details
- Risk Exposure by Branch Type
- Risk Score Calculation Methodology

---

## 📈 Risk Score Methodology

Risk Score is calculated using a weighted model:

- Days Since Last Audit – 25%
- Regulatory Sensitivity – 25%
- Past Findings Count – 20%
- Estimated Risk Exposure – 20%
- Staff Turnover – 10%

The final score is normalized and used to rank branches for audit prioritization.

---

## 📷 Dashboard Preview

### Executive Dashboard

![Executive Dashboard](Screenshot(134).png)

### Branch Level Audit Analysis

![Branch Level Audit Analysis](Screenshot(135).png)

---
## 🚀 Project Workflow

Raw Data
↓
Python Data Cleaning & Risk Score Calculation
↓
SQL Data Validation & Analysis
↓
Power BI Dashboard
↓
Audit Prioritization

---

## 📌 Key Insights

- Identified Top 20 branches requiring immediate audit.
- Retail Branches contribute the highest overall risk exposure.
- High-risk branches account for approximately 14% of total branches.
- Dashboard enables interactive audit planning and monitoring.

---

## 👤 Author

Atchaya ADR
