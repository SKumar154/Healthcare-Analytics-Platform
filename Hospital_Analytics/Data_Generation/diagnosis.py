"""
=========================================================
Healthcare Analytics Platform
Diagnosis Data Generator
=========================================================
"""

import random

import pandas as pd

from config import (
    NUM_PATIENTS,
    NUM_DOCTORS,
    RANDOM_SEED
)

from helpers import generate_patient_id


# -------------------------------------------------------
# Initialization
# -------------------------------------------------------

random.seed(RANDOM_SEED)


# -------------------------------------------------------
# Disease Configuration
# -------------------------------------------------------

DISEASES = [
    "Diabetes",
    "Hypertension",
    "Heart Disease",
    "Asthma",
    "Pneumonia",
    "Migraine",
    "Arthritis",
    "Kidney Stone",
    "Liver Disease",
    "Gastritis",
    "Fracture",
    "Dengue",
    "Tuberculosis",
    "COPD",
    "Stroke",
    "Cancer"
]


# -------------------------------------------------------
# Disease Weights
# -------------------------------------------------------

DISEASE_WEIGHTS = [
    12,   # Diabetes
    12,   # Hypertension
    8,    # Heart Disease
    7,    # Asthma
    8,    # Pneumonia
    7,    # Migraine
    6,    # Arthritis
    5,    # Kidney Stone
    4,    # Liver Disease
    7,    # Gastritis
    5,    # Fracture
    5,    # Dengue
    3,    # Tuberculosis
    4,    # COPD
    3,    # Stroke
    4     # Cancer
]


# -------------------------------------------------------
# Other Reference Lists
# -------------------------------------------------------

SEVERITY_LEVELS = [
    "Mild",
    "Moderate",
    "Severe",
    "Critical"
]

SEVERITY_WEIGHTS = [
    45,
    35,
    15,
    5
]

ADMISSION_TYPES = [
    "OPD",
    "Emergency",
    "Referral",
    "Ambulance"
]

ADMISSION_WEIGHTS = [
    45,
    30,
    15,
    10
]

TREATMENT_TYPES = [
    "Medication",
    "Surgery",
    "Therapy",
    "Observation"
]


# -------------------------------------------------------
# Generate Diagnosis Data
# -------------------------------------------------------

def generate_diagnosis():

    diagnosis_records = []

    for i in range(1, NUM_PATIENTS + 1):

        patient_id = generate_patient_id(i)

        doctor_id = (
            f"DOC{random.randint(1, NUM_DOCTORS):04d}"
        )

        disease = random.choices(
            DISEASES,
            weights=DISEASE_WEIGHTS,
            k=1
        )[0]

        severity = random.choices(
            SEVERITY_LEVELS,
            weights=SEVERITY_WEIGHTS,
            k=1
        )[0]

        admission_type = random.choices(
            ADMISSION_TYPES,
            weights=ADMISSION_WEIGHTS,
            k=1
        )[0]

        # -----------------------------------------------
        # Treatment Logic
        # -----------------------------------------------

        if disease in [
            "Fracture",
            "Cancer",
            "Heart Disease",
            "Stroke"
        ]:

            treatment_type = random.choices(
                ["Medication", "Surgery", "Therapy"],
                weights=[40, 40, 20],
                k=1
            )[0]

        else:

            treatment_type = random.choices(
                TREATMENT_TYPES,
                weights=[60, 10, 15, 15],
                k=1
            )[0]

        # -----------------------------------------------
        # ICU Logic
        # -----------------------------------------------

        if severity == "Critical":

            icu_required = "Yes"

        elif severity == "Severe":

            icu_required = random.choices(
                ["Yes", "No"],
                weights=[50, 50],
                k=1
            )[0]

        else:

            icu_required = random.choices(
                ["Yes", "No"],
                weights=[5, 95],
                k=1
            )[0]

        # -----------------------------------------------
        # Length of Stay
        # -----------------------------------------------

        if severity == "Mild":

            length_of_stay = random.randint(1, 3)

        elif severity == "Moderate":

            length_of_stay = random.randint(2, 7)

        elif severity == "Severe":

            length_of_stay = random.randint(5, 14)

        else:

            length_of_stay = random.randint(10, 30)

        # -----------------------------------------------
        # Create Record
        # -----------------------------------------------

        record = {

            "patient_id":
                patient_id,

            "doctor_id":
                doctor_id,

            "primary_diagnosis":
                disease,

            "severity":
                severity,

            "admission_type":
                admission_type,

            "treatment_type":
                treatment_type,

            "icu_required":
                icu_required,

            "length_of_stay":
                length_of_stay
        }

        diagnosis_records.append(record)

    return pd.DataFrame(diagnosis_records)


# -------------------------------------------------------
# Run Individually
# -------------------------------------------------------

if __name__ == "__main__":

    df = generate_diagnosis()

    print(df.head())

    print("\nShape:")
    print(df.shape)

    print("\nDisease Distribution:")
    print(
        df["primary_diagnosis"]
        .value_counts()
    )
    print(df["severity"].value_counts())

    df.to_csv(
        "../data/diagnosis.csv",
        index=False
    )

    print(
        "\nDiagnosis dataset generated successfully!"
    )