"""
=========================================================
Healthcare Analytics Platform
Patient Data Generator
=========================================================
"""

import random

import pandas as pd

from faker import Faker

from config import (
    NUM_PATIENTS,
    RANDOM_SEED,
    MIN_AGE,
    MAX_AGE,
    MIN_HEIGHT,
    MAX_HEIGHT,
    MIN_WEIGHT,
    MAX_WEIGHT
)

from helpers import (
    generate_patient_id,
    generate_name,
    calculate_bmi,
    generate_pincode
)


# -------------------------------------------------------
# Initialization
# -------------------------------------------------------

fake = Faker("en_IN")

random.seed(RANDOM_SEED)
Faker.seed(RANDOM_SEED)


# -------------------------------------------------------
# Reference Lists
# -------------------------------------------------------

GENDERS = [
    "Male",
    "Female"
]

BLOOD_GROUPS = [
    "A+",
    "A-",
    "B+",
    "B-",
    "AB+",
    "AB-",
    "O+",
    "O-"
]

MARITAL_STATUS = [
    "Single",
    "Married",
    "Divorced",
    "Widowed"
]


# -------------------------------------------------------
# Generate Patient Data
# -------------------------------------------------------

def generate_patients():

    patients = []

    for i in range(1, NUM_PATIENTS + 1):

        age = random.randint(
            MIN_AGE,
            MAX_AGE
        )

        height = round(
            random.uniform(
                MIN_HEIGHT,
                MAX_HEIGHT
            ),
            1
        )

        weight = round(
            random.uniform(
                MIN_WEIGHT,
                MAX_WEIGHT
            ),
            1
        )

        bmi = calculate_bmi(
            height,
            weight
        )

        patient = {

            "patient_id":
                generate_patient_id(i),

            "patient_name":
                generate_name(),

            "age":
                age,

            "gender":
                random.choice(GENDERS),

            "blood_group":
                random.choice(BLOOD_GROUPS),

            "height_cm":
                height,

            "weight_kg":
                weight,

            "bmi":
                bmi,

            "city":
                fake.city(),

            "state":
                fake.state(),

            "pincode":
                generate_pincode(),

            "marital_status":
                random.choice(
                    MARITAL_STATUS
                )
        }

        patients.append(patient)

    return pd.DataFrame(patients)


# -------------------------------------------------------
# Run Individually
# -------------------------------------------------------

if __name__ == "__main__":

    df = generate_patients()

    print(df.head())

    print("\nShape:")
    print(df.shape)

    df.to_csv(
        "../data/patients.csv",
        index=False
    )

    print(
        "\nPatient dataset generated successfully!"
    )