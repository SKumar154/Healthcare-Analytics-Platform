-- =========================================================
-- HEALTHCARE ANALYTICS PLATFORM
-- FINAL SQL INTEGRATION
-- =========================================================
--
-- Grain:
-- One row = one unique patient
--
-- Sources:
-- patients
-- diagnosis
-- billing
-- lifestyle
-- feedback
-- doctors
-- hospitals
--
-- =========================================================


-- =========================================================
-- STEP 1: CREATE DEDUPLICATED SOURCE CTEs
-- =========================================================

CREATE OR REPLACE TABLE raw_analytical_dataset AS

WITH

-- ---------------------------------------------------------
-- Patients
-- ---------------------------------------------------------

patients_dedup AS (

    SELECT DISTINCT
        patient_id,
        patient_name,
        age,
        gender,
        blood_group,
        height_cm,
        weight_kg,
        bmi,
        city,
        state,
        pincode,
        marital_status

    FROM patients
),


-- ---------------------------------------------------------
-- Diagnosis
-- ---------------------------------------------------------

diagnosis_dedup AS (

    SELECT DISTINCT
        patient_id,
        doctor_id,
        primary_diagnosis,
        severity,
        admission_type,
        treatment_type,
        icu_required,
        length_of_stay

    FROM diagnosis
),


-- ---------------------------------------------------------
-- Billing
-- ---------------------------------------------------------

billing_dedup AS (

    SELECT DISTINCT
        patient_id,
        medicine_cost,
        lab_cost,
        room_cost,
        doctor_fee,
        other_charges,
        insurance_provider,
        insurance_coverage,
        bill_amount,
        patient_paid,
        payment_method,
        payment_status

    FROM billing
),


-- ---------------------------------------------------------
-- Lifestyle
-- ---------------------------------------------------------

lifestyle_dedup AS (

    SELECT DISTINCT
        patient_id,
        smoker,
        alcohol_consumption,
        exercise_frequency,
        diet_type,
        sleep_hours

    FROM lifestyle
),


-- ---------------------------------------------------------
-- Feedback
-- ---------------------------------------------------------

feedback_dedup AS (

    SELECT DISTINCT
        patient_id,
        satisfaction_rating,
        complaints,
        follow_up_required,
        recommendation_score

    FROM feedback
)


-- =========================================================
-- STEP 2: JOIN EVERYTHING
-- =========================================================

SELECT

    -- -----------------------------------------------------
    -- Patient Information
    -- -----------------------------------------------------

    p.patient_id,
    p.patient_name,
    p.age,
    p.gender,
    p.blood_group,
    p.height_cm,
    p.weight_kg,
    p.bmi,
    p.city AS patient_city,
    p.state AS patient_state,
    p.pincode,
    p.marital_status,


    -- -----------------------------------------------------
    -- Diagnosis Information
    -- -----------------------------------------------------

    d.primary_diagnosis,
    d.severity,
    d.admission_type,
    d.treatment_type,
    d.icu_required,
    d.length_of_stay,


    -- -----------------------------------------------------
    -- Doctor Information
    -- -----------------------------------------------------

    doc.doctor_id,
    doc.doctor_name,
    doc.department,
    doc.experience_years,
    doc.qualification,


    -- -----------------------------------------------------
    -- Hospital Information
    -- -----------------------------------------------------

    h.hospital_id,
    h.hospital_name,
    h.city AS hospital_city,
    h.state AS hospital_state,
    h.bed_capacity,
    h.ownership,
    h.hospital_type,
    h.nabh_accredited,


    -- -----------------------------------------------------
    -- Billing Information
    -- -----------------------------------------------------

    b.medicine_cost,
    b.lab_cost,
    b.room_cost,
    b.doctor_fee,
    b.other_charges,
    b.insurance_provider,
    b.insurance_coverage,
    b.bill_amount,
    b.patient_paid,
    b.payment_method,
    b.payment_status,


    -- -----------------------------------------------------
    -- Lifestyle Information
    -- -----------------------------------------------------

    l.smoker,
    l.alcohol_consumption,
    l.exercise_frequency,
    l.diet_type,
    l.sleep_hours,


    -- -----------------------------------------------------
    -- Feedback Information
    -- -----------------------------------------------------

    f.satisfaction_rating,
    f.complaints,
    f.follow_up_required,
    f.recommendation_score


FROM patients_dedup AS p


-- =========================================================
-- Patient → Diagnosis
-- =========================================================

LEFT JOIN diagnosis_dedup AS d
    ON p.patient_id = d.patient_id


-- =========================================================
-- Diagnosis → Doctor
-- =========================================================

LEFT JOIN doctors AS doc
    ON d.doctor_id = doc.doctor_id


-- =========================================================
-- Doctor → Hospital
-- =========================================================

LEFT JOIN hospitals AS h
    ON doc.hospital_id = h.hospital_id


-- =========================================================
-- Patient → Billing
-- =========================================================

LEFT JOIN billing_dedup AS b
    ON p.patient_id = b.patient_id


-- =========================================================
-- Patient → Lifestyle
-- =========================================================

LEFT JOIN lifestyle_dedup AS l
    ON p.patient_id = l.patient_id


-- =========================================================
-- Patient → Feedback
-- =========================================================

LEFT JOIN feedback_dedup AS f
    ON p.patient_id = f.patient_id;



-- =========================================================
-- VALIDATION
-- =========================================================


-- Total rows

SELECT
    COUNT(*) AS total_rows
FROM raw_analytical_dataset;


-- Unique patients

SELECT
    COUNT(DISTINCT patient_id) AS unique_patients
FROM raw_analytical_dataset;


-- Check for duplicate patient IDs

SELECT
    patient_id,
    COUNT(*) AS record_count

FROM raw_analytical_dataset

GROUP BY patient_id

HAVING COUNT(*) > 1

ORDER BY record_count DESC

LIMIT 20;