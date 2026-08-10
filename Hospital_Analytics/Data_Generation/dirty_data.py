"""
=========================================================
Healthcare Analytics Platform
Data Quality Issue Generator
=========================================================

This module intentionally introduces realistic data
quality problems into the generated datasets.

The purpose is to simulate raw operational data that
requires cleaning before analysis.
=========================================================
"""

import random

import numpy as np
import pandas as pd

from config import (
    RANDOM_SEED,
    MISSING_VALUE_RATE,
    DUPLICATE_RATE,
    OUTLIER_RATE,
    INVALID_VALUE_RATE
)


# -------------------------------------------------------
# Initialization
# -------------------------------------------------------

random.seed(RANDOM_SEED)
np.random.seed(RANDOM_SEED)


# -------------------------------------------------------
# Helper: Random Row Indices
# -------------------------------------------------------

def get_random_indices(df, rate):

    number_of_rows = len(df)

    number_of_indices = int(
        number_of_rows * rate
    )

    return np.random.choice(
        df.index,
        size=number_of_indices,
        replace=False
    )


# =======================================================
# PATIENT DATA ISSUES
# =======================================================

def dirty_patients(df):

    df = df.copy()

    # ---------------------------------------------------
    # Missing Values
    # ---------------------------------------------------

    missing_columns = [
        "gender",
        "blood_group",
        "height_cm",
        "weight_kg",
        "marital_status"
    ]

    for column in missing_columns:

        indices = get_random_indices(
            df,
            MISSING_VALUE_RATE
        )

        df.loc[
            indices,
            column
        ] = np.nan

    # ---------------------------------------------------
    # Gender Inconsistencies
    # ---------------------------------------------------

    indices = get_random_indices(
        df,
        INVALID_VALUE_RATE
    )

    df.loc[
        indices,
        "gender"
    ] = np.random.choice(
        ["male", "M", "MALE", "female", "F"]
        ,
        size=len(indices)
    )

    # ---------------------------------------------------
    # Blood Group Inconsistencies
    # ---------------------------------------------------

    indices = get_random_indices(
        df,
        INVALID_VALUE_RATE
    )

    df.loc[
        indices,
        "blood_group"
    ] = np.random.choice(
        ["A Plus", "A positive", "a+",
         "B Plus", "O positive", "AB Plus"],
        size=len(indices)
    )

    # ---------------------------------------------------
    # City Spelling Issues
    # ---------------------------------------------------

    city_replacements = {
        "Mumbai": "Bombay",
        "Bengaluru": "Bangalore",
        "Chennai": "Madras",
        "Hyderabad": "Hydrabad",
        "Pune": "Poona"
    }

    for original, incorrect in city_replacements.items():

        indices = df[
            df["city"] == original
        ].index

        if len(indices) > 0:

            sample_size = min(
                len(indices),
                max(1, int(len(indices) * 0.02))
            )

            selected = np.random.choice(
                indices,
                size=sample_size,
                replace=False
            )

            df.loc[
                selected,
                "city"
            ] = incorrect

    # ---------------------------------------------------
    # Age Outliers
    # ---------------------------------------------------

    indices = get_random_indices(
        df,
        OUTLIER_RATE
    )

    df.loc[
        indices,
        "age"
    ] = np.random.randint(
        120,
        151,
        size=len(indices)
    )

    # ---------------------------------------------------
    # Height Outliers
    # ---------------------------------------------------

    indices = get_random_indices(
        df,
        OUTLIER_RATE
    )

    df.loc[
        indices,
        "height_cm"
    ] = np.random.choice(
        [40, 250, 280, 300],
        size=len(indices)
    )

    # ---------------------------------------------------
    # Weight Outliers
    # ---------------------------------------------------

    indices = get_random_indices(
        df,
        OUTLIER_RATE
    )

    df.loc[
        indices,
        "weight_kg"
    ] = np.random.choice(
        [2, 250, 300, 400],
        size=len(indices)
    )

    # ---------------------------------------------------
    # Duplicate Records
    # ---------------------------------------------------

    number_of_duplicates = int(
        len(df) * DUPLICATE_RATE
    )

    duplicate_rows = df.sample(
        n=number_of_duplicates,
        random_state=RANDOM_SEED
    )

    df = pd.concat(
        [df, duplicate_rows],
        ignore_index=True
    )

    return df


# =======================================================
# BILLING DATA ISSUES
# =======================================================

def dirty_billing(df):

    df = df.copy()

    # ---------------------------------------------------
    # Missing Insurance Provider
    # ---------------------------------------------------

    indices = get_random_indices(
        df,
        MISSING_VALUE_RATE
    )

    df.loc[
        indices,
        "insurance_provider"
    ] = np.nan

    # ---------------------------------------------------
    # Negative Bills
    # ---------------------------------------------------

    indices = get_random_indices(
        df,
        INVALID_VALUE_RATE
    )

    df.loc[
        indices,
        "bill_amount"
    ] = -np.abs(
        df.loc[
            indices,
            "bill_amount"
        ]
    )

    # ---------------------------------------------------
    # Negative Patient Payments
    # ---------------------------------------------------

    indices = get_random_indices(
        df,
        INVALID_VALUE_RATE
    )

    df.loc[
        indices,
        "patient_paid"
    ] = -np.abs(
        df.loc[
            indices,
            "patient_paid"
        ]
    )

    # ---------------------------------------------------
    # Insurance Coverage Greater Than Bill
    # ---------------------------------------------------

    indices = get_random_indices(
        df,
        INVALID_VALUE_RATE
    )

    df.loc[
        indices,
        "insurance_coverage"
    ] = (
        df.loc[
            indices,
            "bill_amount"
        ].abs()
        * 1.20
    )

    # ---------------------------------------------------
    # Duplicate Billing Records
    # ---------------------------------------------------

    number_of_duplicates = int(
        len(df) * DUPLICATE_RATE
    )

    duplicate_rows = df.sample(
        n=number_of_duplicates,
        random_state=RANDOM_SEED
    )

    df = pd.concat(
        [df, duplicate_rows],
        ignore_index=True
    )

    return df


# =======================================================
# DIAGNOSIS DATA ISSUES
# =======================================================

def dirty_diagnosis(df):

    df = df.copy()

    # ---------------------------------------------------
    # Missing Severity
    # ---------------------------------------------------

    indices = get_random_indices(
        df,
        MISSING_VALUE_RATE
    )

    df.loc[
        indices,
        "severity"
    ] = np.nan

    # ---------------------------------------------------
    # Invalid Length of Stay
    # ---------------------------------------------------

    indices = get_random_indices(
        df,
        OUTLIER_RATE
    )

    df.loc[
        indices,
        "length_of_stay"
    ] = np.random.choice(
        [-10, -5, 100, 200],
        size=len(indices)
    )

    # ---------------------------------------------------
    # Duplicate Records
    # ---------------------------------------------------

    number_of_duplicates = int(
        len(df) * DUPLICATE_RATE
    )

    duplicate_rows = df.sample(
        n=number_of_duplicates,
        random_state=RANDOM_SEED
    )

    df = pd.concat(
        [df, duplicate_rows],
        ignore_index=True
    )

    return df


# =======================================================
# LIFESTYLE DATA ISSUES
# =======================================================

def dirty_lifestyle(df):

    df = df.copy()

    # ---------------------------------------------------
    # Missing Values
    # ---------------------------------------------------

    columns = [
        "smoker",
        "alcohol_consumption",
        "exercise_frequency",
        "diet_type",
        "sleep_hours"
    ]

    for column in columns:

        indices = get_random_indices(
            df,
            MISSING_VALUE_RATE
        )

        df.loc[
            indices,
            column
        ] = np.nan

    # ---------------------------------------------------
    # Invalid Sleep Hours
    # ---------------------------------------------------

    indices = get_random_indices(
        df,
        INVALID_VALUE_RATE
    )

    df.loc[
        indices,
        "sleep_hours"
    ] = np.random.choice(
        [-5, 0, 20, 25],
        size=len(indices)
    )

    return df


# =======================================================
# FEEDBACK DATA ISSUES
# =======================================================

def dirty_feedback(df):

    df = df.copy()

    # ---------------------------------------------------
    # Missing Ratings
    # ---------------------------------------------------

    indices = get_random_indices(
        df,
        MISSING_VALUE_RATE
    )

    df.loc[
        indices,
        "satisfaction_rating"
    ] = np.nan

    # ---------------------------------------------------
    # Invalid Ratings
    # ---------------------------------------------------

    indices = get_random_indices(
        df,
        INVALID_VALUE_RATE
    )

    df.loc[
        indices,
        "satisfaction_rating"
    ] = np.random.choice(
        [-2, 0, 6, 7, 8],
        size=len(indices)
    )

    # ---------------------------------------------------
    # Invalid Recommendation Scores
    # ---------------------------------------------------

    indices = get_random_indices(
        df,
        INVALID_VALUE_RATE
    )

    df.loc[
        indices,
        "recommendation_score"
    ] = np.random.choice(
        [-5, 0, 11, 15],
        size=len(indices)
    )

    # ---------------------------------------------------
    # Duplicate Feedback Records
    # ---------------------------------------------------

    number_of_duplicates = int(
        len(df) * DUPLICATE_RATE
    )

    duplicate_rows = df.sample(
        n=number_of_duplicates,
        random_state=RANDOM_SEED
    )

    df = pd.concat(
        [df, duplicate_rows],
        ignore_index=True
    )

    return df


# =======================================================
# MAIN FUNCTION
# =======================================================

def apply_data_quality_issues():

    print("\nLoading generated datasets...")

    patients = pd.read_csv(
        "../data/patients.csv"
    )

    diagnosis = pd.read_csv(
        "../data/diagnosis.csv"
    )

    billing = pd.read_csv(
        "../data/billing.csv"
    )

    lifestyle = pd.read_csv(
        "../data/lifestyle.csv"
    )

    feedback = pd.read_csv(
        "../data/feedback.csv"
    )

    print("Applying data quality issues...")

    patients = dirty_patients(
        patients
    )

    diagnosis = dirty_diagnosis(
        diagnosis
    )

    billing = dirty_billing(
        billing
    )

    lifestyle = dirty_lifestyle(
        lifestyle
    )

    feedback = dirty_feedback(
        feedback
    )

    print("Saving dirty datasets...")

    patients.to_csv(
        "../data/patients.csv",
        index=False
    )

    diagnosis.to_csv(
        "../data/diagnosis.csv",
        index=False
    )

    billing.to_csv(
        "../data/billing.csv",
        index=False
    )

    lifestyle.to_csv(
        "../data/lifestyle.csv",
        index=False
    )

    feedback.to_csv(
        "../data/feedback.csv",
        index=False
    )

    print(
        "\nData quality issues applied successfully!"
    )


# -------------------------------------------------------
# Run Individually
# -------------------------------------------------------

if __name__ == "__main__":

    apply_data_quality_issues()