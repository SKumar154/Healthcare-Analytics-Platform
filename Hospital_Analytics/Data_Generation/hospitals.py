"""
=========================================================
Healthcare Analytics Platform
Hospital Generator
=========================================================
"""

import random

import pandas as pd

from faker import Faker

from config import (
    NUM_HOSPITALS,
    RANDOM_SEED
)

from helpers import generate_hospital_id

# -------------------------------------------------------
# Initialization
# -------------------------------------------------------

fake = Faker("en_IN")

random.seed(RANDOM_SEED)
Faker.seed(RANDOM_SEED)

# -------------------------------------------------------
# Static Lists
# -------------------------------------------------------

OWNERSHIP_TYPES = [
    "Private",
    "Government",
    "Trust"
]

HOSPITAL_TYPES = [
    "Multi Specialty",
    "Specialty"
]

# -------------------------------------------------------
# Generate Hospital Data
# -------------------------------------------------------

def generate_hospitals():

    hospitals = []

    for i in range(1, NUM_HOSPITALS + 1):

        hospital = {

            "hospital_id": generate_hospital_id(i),

            "hospital_name": fake.company() + " Hospital",

            "city": fake.city(),

            "state": fake.state(),

            "bed_capacity": random.randint(50, 1000),

            "ownership": random.choice(OWNERSHIP_TYPES),

            "hospital_type": random.choice(HOSPITAL_TYPES),

            "nabh_accredited": random.choice(["Yes", "No"])

        }

        hospitals.append(hospital)

    return pd.DataFrame(hospitals)


# -------------------------------------------------------
# Run Individually
# -------------------------------------------------------

if __name__ == "__main__":

    df = generate_hospitals()

    print(df.head())

    df.to_csv("../data/hospitals.csv", index=False)

    print("\nHospital dataset generated successfully!")