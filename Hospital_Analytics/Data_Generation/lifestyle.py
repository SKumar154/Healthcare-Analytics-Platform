"""
=========================================================
Healthcare Analytics Platform
Lifestyle Data Generator
=========================================================
"""

import random

import pandas as pd

from config import (
    NUM_PATIENTS,
    RANDOM_SEED
)

from helpers import generate_patient_id


# -------------------------------------------------------
# Initialization
# -------------------------------------------------------

random.seed(RANDOM_SEED)


# -------------------------------------------------------
# Lifestyle Categories
# -------------------------------------------------------

SMOKING_STATUS = [
    "Yes",
    "No"
]

ALCOHOL_CONSUMPTION = [
    "None",
    "Occasional",
    "Regular"
]

EXERCISE_FREQUENCY = [
    "Never",
    "Rarely",
    "1-2 times/week",
    "3-4 times/week",
    "Daily"
]

DIET_TYPES = [
    "Vegetarian",
    "Non-Vegetarian",
    "Vegan",
    "Jain"
]


# -------------------------------------------------------
# Generate Lifestyle Data
# -------------------------------------------------------

def generate_lifestyle():

    lifestyle_records = []

    for i in range(1, NUM_PATIENTS + 1):

        patient_id = generate_patient_id(i)

        smoker = random.choices(
            SMOKING_STATUS,
            weights=[20, 80],
            k=1
        )[0]

        alcohol_consumption = random.choices(
            ALCOHOL_CONSUMPTION,
            weights=[50, 35, 15],
            k=1
        )[0]

        exercise_frequency = random.choices(
            EXERCISE_FREQUENCY,
            weights=[15, 20, 25, 25, 15],
            k=1
        )[0]

        diet_type = random.choices(
            DIET_TYPES,
            weights=[55, 35, 5, 5],
            k=1
        )[0]

        sleep_hours = round(
            random.uniform(4, 9),
            1
        )

        record = {

            "patient_id":
                patient_id,

            "smoker":
                smoker,

            "alcohol_consumption":
                alcohol_consumption,

            "exercise_frequency":
                exercise_frequency,

            "diet_type":
                diet_type,

            "sleep_hours":
                sleep_hours
        }

        lifestyle_records.append(record)

    return pd.DataFrame(lifestyle_records)


# -------------------------------------------------------
# Run Individually
# -------------------------------------------------------

if __name__ == "__main__":

    df = generate_lifestyle()

    print(df.head())

    print("\nShape:")
    print(df.shape)

    print("\nSmoking Distribution:")
    print(
        df["smoker"]
        .value_counts()
    )

    print("\nExercise Distribution:")
    print(
        df["exercise_frequency"]
        .value_counts()
    )
    print(df["sleep_hours"].min())
    print(df["sleep_hours"].max())
    print(df["smoker"].value_counts(normalize=True))


    df.to_csv(
        "../data/lifestyle.csv",
        index=False
    )

    print(
        "\nLifestyle dataset generated successfully!"
    )