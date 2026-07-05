CREATE database Internal_audit;
USE Internal_audit;
SELECT *
FROM internal_audit_final;

SELECT COUNT(*)
FROM internal_audit_final;

SELECT BranchID,
       BranchName,
       City,
       BranchType,
       RiskScore,
       RiskTier
FROM internal_audit_final
WHERE AuditDecision = 'Selected for Audit'
ORDER BY RiskRank;

SELECT BranchName,
       City,
       RiskScore,
       RiskTier
FROM internal_audit_final
ORDER BY RiskScore DESC
LIMIT 10;

SELECT AuditDecision,
       COUNT(*) AS TotalBranches
FROM internal_audit_final
GROUP BY AuditDecision;

SELECT RiskTier,
       COUNT(*) AS TotalBranches
FROM internal_audit_final
GROUP BY RiskTier
ORDER BY TotalBranches DESC;

SELECT BranchType,
       ROUND(AVG(RiskScore),3) AS AverageRiskScore
FROM internal_audit_final
GROUP BY BranchType
ORDER BY AverageRiskScore DESC;

SELECT City,
       ROUND(AVG(RiskScore),3) AS AverageRiskScore
FROM internal_audit_final
GROUP BY City
ORDER BY AverageRiskScore DESC;

SELECT BranchName,
       City,
       BranchType,
       RiskScore
FROM internal_audit_final
WHERE RiskTier='High'
ORDER BY RiskScore DESC;

SELECT BranchName,
       City,
       RiskScore
FROM internal_audit_final
WHERE RiskTier='High'
AND AuditDecision='Selected for Audit'
ORDER BY RiskScore DESC;

SELECT BranchName,
       City,
       RiskScore,
       EstimatedRiskExposureCr
FROM internal_audit_final
WHERE AuditDecision='Deferred'
ORDER BY RiskScore DESC;

SELECT SUM(EstimatedRiskExposureCr) AS TotalRiskExposure
FROM internal_audit_final;

SELECT SUM(EstimatedRiskExposureCr) AS CoveredRiskExposure
FROM internal_audit_final
WHERE AuditDecision='Selected for Audit';

SELECT SUM(EstimatedRiskExposureCr) AS RemainingRiskExposure
FROM internal_audit_final
WHERE AuditDecision='Deferred';

SELECT SUM(EstimatedAuditHours) AS TotalAuditHours
FROM internal_audit_final
WHERE AuditDecision='Selected for Audit';

SELECT RiskTier,
       SUM(EstimatedAuditHours) AS AuditHours
FROM internal_audit_final
GROUP BY RiskTier;

SELECT RiskTier,
       ROUND(AVG(TransactionVolumeCr),2) AS AvgTransactionVolume
FROM internal_audit_final
GROUP BY RiskTier;

SELECT BranchName,
       TransactionVolumeCr
FROM internal_audit_final
ORDER BY TransactionVolumeCr DESC
LIMIT 10;

SELECT BranchName,
       DaysSinceLastAudit
FROM internal_audit_final
ORDER BY DaysSinceLastAudit DESC
LIMIT 10;

SELECT BranchName,
       PastFindingsCount
FROM internal_audit_final
ORDER BY PastFindingsCount DESC
LIMIT 10;

SELECT BranchName,
       ComplaintsLastYear
FROM internal_audit_final
ORDER BY ComplaintsLastYear DESC
LIMIT 10;

SELECT
COUNT(*) AS TotalBranches,

SUM(CASE
WHEN AuditDecision='Selected for Audit'
THEN 1
ELSE 0
END) AS SelectedForAudit,

SUM(CASE
WHEN AuditDecision='Deferred'
THEN 1
ELSE 0
END) AS DeferredBranches,

ROUND(AVG(RiskScore),3) AS AverageRiskScore,

SUM(EstimatedRiskExposureCr) AS TotalRiskExposure,

SUM(EstimatedAuditHours) AS TotalAuditHours

FROM internal_audit_final;