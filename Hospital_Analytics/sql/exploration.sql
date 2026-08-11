-- =====================================================
-- Healthcare Analytics Platform
-- SQL Exploration
-- =====================================================


-- =====================================================
-- 1. Inspect Patients
-- =====================================================

SELECT *
FROM patients
LIMIT 10;


-- =====================================================
-- 2. Count Patients
-- =====================================================

SELECT COUNT(*) AS total_patient_records
FROM patients;


-- =====================================================
-- 3. Count Unique Patients
-- =====================================================

SELECT COUNT(DISTINCT patient_id) AS unique_patients
FROM patients;


-- =====================================================
-- 4. Patient Age Summary
-- =====================================================

SELECT
    MIN(age) AS minimum_age,
    MAX(age) AS maximum_age,
    AVG(age) AS average_age
FROM patients;


-- =====================================================
-- 5. Gender Distribution
-- =====================================================

SELECT
    gender,
    COUNT(*) AS patient_count
FROM patients
GROUP BY gender
ORDER BY patient_count DESC;
