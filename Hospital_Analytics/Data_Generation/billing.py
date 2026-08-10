"""
=========================================================
Healthcare Analytics Platform
Billing Data Generator
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
# Insurance Configuration
# -------------------------------------------------------

INSURANCE_PROVIDERS = [
    "Star Health",
    "HDFC Ergo",
    "ICICI Lombard",
    "Niva Bupa",
    "Care Health",
    "None"
]

INSURANCE_WEIGHTS = [
    18,
    15,
    15,
    12,
    10,
    30
]


# -------------------------------------------------------
# Payment Configuration
# -------------------------------------------------------

PAYMENT_METHODS = [
    "Cash",
    "Credit Card",
    "Debit Card",
    "UPI",
    "Net Banking"
]

PAYMENT_STATUSES = [
    "Paid",
    "Pending",
    "Partially Paid"
]


# -------------------------------------------------------
# Generate Billing Data
# -------------------------------------------------------

def generate_billing():

    billing_records = []

    for i in range(1, NUM_PATIENTS + 1):

        patient_id = generate_patient_id(i)

        # -----------------------------------------------
        # Individual Cost Components
        # -----------------------------------------------

        medicine_cost = round(
            random.uniform(500, 50000),
            2
        )

        lab_cost = round(
            random.uniform(300, 30000),
            2
        )

        room_cost = round(
            random.uniform(1000, 100000),
            2
        )

        doctor_fee = round(
            random.uniform(500, 25000),
            2
        )

        other_charges = round(
            random.uniform(100, 15000),
            2
        )

        # -----------------------------------------------
        # Total Bill
        # -----------------------------------------------

        bill_amount = round(
            medicine_cost
            + lab_cost
            + room_cost
            + doctor_fee
            + other_charges,
            2
        )

        # -----------------------------------------------
        # Insurance
        # -----------------------------------------------

        insurance_provider = random.choices(
            INSURANCE_PROVIDERS,
            weights=INSURANCE_WEIGHTS,
            k=1
        )[0]

        if insurance_provider == "None":

            insurance_coverage = 0

        else:

            coverage_percentage = random.uniform(
                0.50,
                0.90
            )

            insurance_coverage = round(
                bill_amount * coverage_percentage,
                2
            )

        # -----------------------------------------------
        # Patient Payment
        # -----------------------------------------------

        patient_paid = round(
            bill_amount - insurance_coverage,
            2
        )

        # -----------------------------------------------
        # Payment Method
        # -----------------------------------------------

        payment_method = random.choice(
            PAYMENT_METHODS
        )

        # -----------------------------------------------
        # Payment Status
        # -----------------------------------------------

        if patient_paid == 0:

            payment_status = "Paid"

        else:

            payment_status = random.choices(
                PAYMENT_STATUSES,
                weights=[70, 10, 20],
                k=1
            )[0]

        # -----------------------------------------------
        # Create Record
        # -----------------------------------------------

        record = {

            "patient_id":
                patient_id,

            "medicine_cost":
                medicine_cost,

            "lab_cost":
                lab_cost,

            "room_cost":
                room_cost,

            "doctor_fee":
                doctor_fee,

            "other_charges":
                other_charges,

            "insurance_provider":
                insurance_provider,

            "insurance_coverage":
                insurance_coverage,

            "bill_amount":
                bill_amount,

            "patient_paid":
                patient_paid,

            "payment_method":
                payment_method,

            "payment_status":
                payment_status
        }

        billing_records.append(record)

    return pd.DataFrame(billing_records)


# -------------------------------------------------------
# Run Individually
# -------------------------------------------------------

if __name__ == "__main__":

    df = generate_billing()

    print(df.head())

    print("\nShape:")
    print(df.shape)

    print("\nAverage Bill:")
    print(
        round(
            df["bill_amount"].mean(),
            2
        )
    )
    print("Checking medical bill")
    print(
        (
                df["medicine_cost"]
                + df["lab_cost"]
                + df["room_cost"]
                + df["doctor_fee"]
                + df["other_charges"]
                - df["bill_amount"]
        ).abs().max()
    )

    print("\nInsurance Distribution:")
    print(
        df["insurance_provider"]
        .value_counts()
    )

    df.to_csv(
        "../data/billing.csv",
        index=False
    )

    print(
        "\nBilling dataset generated successfully!"
    )