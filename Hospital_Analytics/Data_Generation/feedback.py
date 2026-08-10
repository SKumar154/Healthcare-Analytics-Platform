"""
=========================================================
Healthcare Analytics Platform
Patient Feedback Data Generator
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
# Feedback Configuration
# -------------------------------------------------------

COMPLAINT_STATUS = [
    "Yes",
    "No"
]

FOLLOW_UP_STATUS = [
    "Yes",
    "No"
]


# -------------------------------------------------------
# Generate Feedback Data
# -------------------------------------------------------

def generate_feedback():

    feedback_records = []

    for i in range(1, NUM_PATIENTS + 1):

        patient_id = generate_patient_id(i)

        # -----------------------------------------------
        # Complaint
        # -----------------------------------------------

        complaints = random.choices(
            COMPLAINT_STATUS,
            weights=[15, 85],
            k=1
        )[0]

        # -----------------------------------------------
        # Satisfaction Rating
        # -----------------------------------------------

        if complaints == "Yes":

            satisfaction_rating = random.choices(
                [1, 2, 3, 4, 5],
                weights=[30, 35, 25, 8, 2],
                k=1
            )[0]

        else:

            satisfaction_rating = random.choices(
                [1, 2, 3, 4, 5],
                weights=[2, 5, 15, 38, 40],
                k=1
            )[0]

        # -----------------------------------------------
        # Follow-up
        # -----------------------------------------------

        if satisfaction_rating <= 2:

            follow_up_required = random.choices(
                FOLLOW_UP_STATUS,
                weights=[60, 40],
                k=1
            )[0]

        else:

            follow_up_required = random.choices(
                FOLLOW_UP_STATUS,
                weights=[15, 85],
                k=1
            )[0]

        # -----------------------------------------------
        # Recommendation Score
        # -----------------------------------------------

        if complaints == "Yes":

            recommendation_score = random.randint(
                1,
                6
            )

        else:

            recommendation_score = random.randint(
                6,
                10
            )

        # -----------------------------------------------
        # Create Record
        # -----------------------------------------------

        record = {

            "patient_id":
                patient_id,

            "satisfaction_rating":
                satisfaction_rating,

            "complaints":
                complaints,

            "follow_up_required":
                follow_up_required,

            "recommendation_score":
                recommendation_score
        }

        feedback_records.append(record)

    return pd.DataFrame(feedback_records)


# -------------------------------------------------------
# Run Individually
# -------------------------------------------------------

if __name__ == "__main__":

    df = generate_feedback()

    print(df.head())

    print("\nShape:")
    print(df.shape)

    print("\nSatisfaction Distribution:")
    print(
        df["satisfaction_rating"]
        .value_counts()
        .sort_index()
    )

    print("\nComplaint Distribution:")
    print(
        df["complaints"]
        .value_counts()
    )

    df.to_csv(
        "../data/feedback.csv",
        index=False
    )

    print(
        "\nFeedback dataset generated successfully!"
    )