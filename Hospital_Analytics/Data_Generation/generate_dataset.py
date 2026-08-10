"""
=========================================================
Healthcare Analytics Platform
Master Dataset Generator
=========================================================

This script orchestrates the complete synthetic dataset
generation process.

Running this file will:

1. Generate hospitals
2. Generate doctors
3. Generate patients
4. Generate diagnosis records
5. Generate billing records
6. Generate lifestyle records
7. Generate feedback records
8. Apply realistic data quality issues

The final CSV files will be stored in the data/ folder.
=========================================================
"""

import os
import time

from hospitals import generate_hospitals
from doctors import generate_doctors
from patients import generate_patients
from diagnosis import generate_diagnosis
from billing import generate_billing
from lifestyle import generate_lifestyle
from feedback import generate_feedback
from dirty_data import (
    dirty_patients,
    dirty_diagnosis,
    dirty_billing,
    dirty_lifestyle,
    dirty_feedback
)


# =======================================================
# Configuration
# =======================================================

OUTPUT_FOLDER = "../data"


# =======================================================
# Utility Function
# =======================================================

def save_dataset(df, filename):

    filepath = os.path.join(
        OUTPUT_FOLDER,
        filename
    )

    df.to_csv(
        filepath,
        index=False
    )

    print(
        f"Saved: {filename} | Rows: {len(df):,}"
    )


# =======================================================
# Main Dataset Generation
# =======================================================

def generate_all_datasets():

    start_time = time.time()

    print("=" * 60)
    print("HEALTHCARE ANALYTICS PLATFORM")
    print("DATASET GENERATION STARTED")
    print("=" * 60)

    # ---------------------------------------------------
    # Create output folder if it doesn't exist
    # ---------------------------------------------------

    os.makedirs(
        OUTPUT_FOLDER,
        exist_ok=True
    )

    # ===================================================
    # STEP 1 — Generate Hospitals
    # ===================================================

    print("\n[1/8] Generating hospitals...")

    hospitals = generate_hospitals()

    save_dataset(
        hospitals,
        "hospitals.csv"
    )

    # ===================================================
    # STEP 2 — Generate Doctors
    # ===================================================

    print("\n[2/8] Generating doctors...")

    doctors = generate_doctors()

    save_dataset(
        doctors,
        "doctors.csv"
    )

    # ===================================================
    # STEP 3 — Generate Patients
    # ===================================================

    print("\n[3/8] Generating patients...")

    patients = generate_patients()

    save_dataset(
        patients,
        "patients.csv"
    )

    # ===================================================
    # STEP 4 — Generate Diagnosis
    # ===================================================

    print("\n[4/8] Generating diagnosis records...")

    diagnosis = generate_diagnosis()

    save_dataset(
        diagnosis,
        "diagnosis.csv"
    )

    # ===================================================
    # STEP 5 — Generate Billing
    # ===================================================

    print("\n[5/8] Generating billing records...")

    billing = generate_billing()

    save_dataset(
        billing,
        "billing.csv"
    )

    # ===================================================
    # STEP 6 — Generate Lifestyle
    # ===================================================

    print("\n[6/8] Generating lifestyle records...")

    lifestyle = generate_lifestyle()

    save_dataset(
        lifestyle,
        "lifestyle.csv"
    )

    # ===================================================
    # STEP 7 — Generate Feedback
    # ===================================================

    print("\n[7/8] Generating feedback records...")

    feedback = generate_feedback()

    save_dataset(
        feedback,
        "feedback.csv"
    )

    # ===================================================
    # STEP 8 — Apply Data Quality Issues
    # ===================================================

    print("\n[8/8] Applying data quality issues...")

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

    # ---------------------------------------------------
    # Overwrite clean files with dirty versions
    # ---------------------------------------------------

    save_dataset(
        patients,
        "patients.csv"
    )

    save_dataset(
        diagnosis,
        "diagnosis.csv"
    )

    save_dataset(
        billing,
        "billing.csv"
    )

    save_dataset(
        lifestyle,
        "lifestyle.csv"
    )

    save_dataset(
        feedback,
        "feedback.csv"
    )

    # ===================================================
    # Completion
    # ===================================================

    end_time = time.time()

    elapsed_time = end_time - start_time

    print("\n" + "=" * 60)
    print("DATASET GENERATION COMPLETED")
    print("=" * 60)

    print(
        f"\nTotal execution time: "
        f"{elapsed_time / 60:.2f} minutes"
    )

    print(
        "\nAll datasets are available in:"
    )

    print(
        os.path.abspath(OUTPUT_FOLDER)
    )

    print("\nGenerated files:")

    print("  ✓ hospitals.csv")
    print("  ✓ doctors.csv")
    print("  ✓ patients.csv")
    print("  ✓ diagnosis.csv")
    print("  ✓ billing.csv")
    print("  ✓ lifestyle.csv")
    print("  ✓ feedback.csv")

    print("\nYour raw healthcare dataset is ready! 🚀")


# =======================================================
# Entry Point
# =======================================================

if __name__ == "__main__":

    generate_all_datasets()