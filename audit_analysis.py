# ============================================
# INTERNAL AUDIT RISK PRIORITIZATION PROJECT
# Author : Atchaya ADR
# ============================================

# ============================================
# Step 1 : Import Libraries
# ============================================

import pandas as pd
import numpy as np

# ============================================
# Step 2 : Load Dataset
# ============================================

df = pd.read_excel("Internal audit dataset.xlsx")

# ============================================
# Step 3 : Preview Dataset
# ============================================

print("\nFirst 5 Rows")
print(df.head())

print("\nDataset Shape")
print(df.shape)

print("\nDataset Information")
print(df.info())

# ============================================
# Step 4 : Missing Values
# ============================================

print("\nMissing Values")
print(df.isnull().sum())

# ============================================
# Step 5 : Duplicate Records
# ============================================

print("\nDuplicate Records")
print(df.duplicated().sum())

# ============================================
# Step 6 : Statistical Summary
# ============================================

print("\nStatistical Summary")
print(df.describe())

# ============================================
# Step 7 : Unique Values
# ============================================

print("\nBranch Types")
print(df["BranchType"].unique())

print("\nRegulatory Sensitivity")
print(df["RegulatorySensitivity"].unique())

# ============================================
# Step 8 : Value Counts
# ============================================

print("\nBranch Type Count")
print(df["BranchType"].value_counts())

print("\nRegulatory Sensitivity Count")
print(df["RegulatorySensitivity"].value_counts())

# ============================================
# Step 9 : City-wise Branch Count
# ============================================

print("\nBranches by City")
print(df["City"].value_counts())

# ============================================
# Step 10 : Average Transaction Volume
# ============================================

print("\nAverage Transaction Volume")
print(
    df.groupby("BranchType")["TransactionVolumeCr"].mean()
)

# ============================================
# Step 11 : Average Days Since Last Audit
# ============================================

print("\nAverage Days Since Last Audit")
print(
    df.groupby("BranchType")["DaysSinceLastAudit"].mean()
)

# ============================================
# Step 12 : Average Staff Turnover
# ============================================

print("\nAverage Staff Turnover")
print(
    df.groupby("BranchType")["StaffTurnoverRate"].mean()
)

# ============================================
# Step 13 : Average Complaints
# ============================================

print("\nAverage Complaints")
print(
    df.groupby("BranchType")["ComplaintsLastYear"].mean()
)

# ============================================
# Step 14 : Top 10 Transaction Volume
# ============================================

print("\nTop 10 Transaction Volume Branches")
print(df.nlargest(10, "TransactionVolumeCr"))

# ============================================
# Step 15 : Top 10 Days Since Last Audit
# ============================================

print("\nLongest Time Since Last Audit")
print(df.nlargest(10, "DaysSinceLastAudit"))

# ============================================
# Step 16 : Top 10 Past Findings
# ============================================

print("\nHighest Audit Findings")
print(df.nlargest(10, "PastFindingsCount"))

# ============================================
# Step 17 : Top 10 Complaints
# ============================================

print("\nHighest Complaints")
print(df.nlargest(10, "ComplaintsLastYear"))

# ============================================
# Step 18 : Regulatory Score
# ============================================

regulatory_map = {
    "Low": 1,
    "Medium": 2,
    "High": 3
}

df["RegulatoryScore"] = df["RegulatorySensitivity"].map(regulatory_map)

# ============================================
# Step 19 : Normalize Regulatory Score
# ============================================

df["RegulatoryScore_Scaled"] = (
    (df["RegulatoryScore"] - df["RegulatoryScore"].min()) /
    (df["RegulatoryScore"].max() - df["RegulatoryScore"].min())
)

# ============================================
# Step 20 : Normalize Risk Factors
# ============================================

columns_to_scale = [
    "DaysSinceLastAudit",
    "PastFindingsCount",
    "TransactionVolumeCr",
    "StaffTurnoverRate",
    "ComplaintsLastYear"
]

for col in columns_to_scale:

    df[col + "_Scaled"] = (
        (df[col] - df[col].min()) /
        (df[col].max() - df[col].min())
    )

# ============================================
# Step 21 : Calculate Risk Score
# ============================================

df["RiskScore"] = (

    df["DaysSinceLastAudit_Scaled"] * 0.30 +

    df["PastFindingsCount_Scaled"] * 0.25 +

    df["TransactionVolumeCr_Scaled"] * 0.20 +

    df["RegulatoryScore_Scaled"] * 0.15 +

    df["StaffTurnoverRate_Scaled"] * 0.05 +

    df["ComplaintsLastYear_Scaled"] * 0.05

)

# ============================================
# Step 22 : Risk Rank
# ============================================

df["RiskRank"] = df["RiskScore"].rank(
    method="dense",
    ascending=False
)

# ============================================
# Step 23 : Audit Decision
# ============================================

df["AuditDecision"] = np.where(

    df["RiskRank"] <= 20,

    "Selected for Audit",

    "Deferred"

)

# ============================================
# Step 24 : Risk Tier
# ============================================

high = df["RiskScore"].quantile(0.67)

medium = df["RiskScore"].quantile(0.33)


def risk_tier(score):

    if score >= high:
        return "High"

    elif score >= medium:
        return "Medium"

    else:
        return "Low"


df["RiskTier"] = df["RiskScore"].apply(risk_tier)

# ============================================
# Step 25 : Model Validation
# ============================================

print("\nRisk Tier Distribution")
print(df["RiskTier"].value_counts())

print("\nAudit Decision Distribution")
print(df["AuditDecision"].value_counts())

# ============================================
# Step 26 : Final Top 20 Branches
# ============================================

print("\nTop 20 Branches Selected For Audit")

print(

    df[
        [
            "BranchID",
            "BranchName",
            "City",
            "BranchType",
            "RiskScore",
            "RiskRank",
            "RiskTier",
            "AuditDecision"
        ]
    ].sort_values("RiskRank").head(20)

)

# ============================================
# Step 27 : Export Final Dataset
# ============================================

df.to_csv(
    "Internal_Audit_Final.csv",
    index=False
)

print("\nFinal Dataset Exported Successfully")