"""
=========================================================
Healthcare Analytics Platform
Doctor Data Generator
=========================================================
"""

import random

import pandas as pd

from faker import Faker

from config import (
    NUM_DOCTORS,
    NUM_HOSPITALS,
    RANDOM_SEED
)

from helpers import generate_doctor_id


# -------------------------------------------------------
# Initialization
# -------------------------------------------------------

fake = Faker("en_IN")

random.seed(RANDOM_SEED)
Faker.seed(RANDOM_SEED)


# -------------------------------------------------------
# Department Configuration
# -------------------------------------------------------

DEPARTMENTS = [
    "General Medicine",
    "Cardiology",
    "Neurology",
    "Orthopedics",
    "Oncology",
    "Pulmonology",
    "Nephrology",
    "Gastroenterology",
    "Dermatology",
    "ENT",
    "Gynecology",
    "Urology",
    "Psychiatry",
    "Radiology",
    "Emergency Medicine"
]


# -------------------------------------------------------
# Qualification Configuration
# -------------------------------------------------------

QUALIFICATIONS = [
    "MBBS",
    "MBBS, MD",
    "MBBS, MS",
    "MBBS, DNB",
    "MBBS, DM",
    "MBBS, MCh"
]


# -------------------------------------------------------
# Generate Doctors
# -------------------------------------------------------

def generate_doctors():

    doctors = []

    for i in range(1, NUM_DOCTORS + 1):

        doctor = {

            "doctor_id": generate_doctor_id(i),

            "doctor_name": fake.name(),

            "department": random.choice(DEPARTMENTS),

            "experience_years": random.randint(1, 35),

            "qualification": random.choice(QUALIFICATIONS),

            "hospital_id": f"HOS{random.randint(1, NUM_HOSPITALS):03d}"
        }

        doctors.append(doctor)

    return pd.DataFrame(doctors)


# -------------------------------------------------------
# Run Individually
# -------------------------------------------------------

if __name__ == "__main__":

    df = generate_doctors()

    print(df.head())

    df.to_csv("../data/doctors.csv", index=False)

    print("\nDoctor dataset generated successfully!")