"""
=========================================================
Healthcare Analytics Platform
DuckDB Data Loader
=========================================================

Loads the generated CSV datasets into a DuckDB database.
=========================================================
"""

import duckdb
import os


# -------------------------------------------------------
# Paths
# -------------------------------------------------------

DATA_FOLDER = "../data"

DATABASE_PATH = "../healthcare.duckdb"


# -------------------------------------------------------
# Dataset Configuration
# -------------------------------------------------------

DATASETS = {
    "hospitals": "hospitals.csv",
    "doctors": "doctors.csv",
    "patients": "patients.csv",
    "diagnosis": "diagnosis.csv",
    "billing": "billing.csv",
    "lifestyle": "lifestyle.csv",
    "feedback": "feedback.csv"
}


# -------------------------------------------------------
# Load Data
# -------------------------------------------------------

def load_data():

    print("=" * 60)
    print("HEALTHCARE ANALYTICS PLATFORM")
    print("DUCKDB DATA LOADING")
    print("=" * 60)

    # ---------------------------------------------------
    # Connect to DuckDB
    # ---------------------------------------------------

    connection = duckdb.connect(
        DATABASE_PATH
    )

    print(
        f"\nConnected to: {os.path.abspath(DATABASE_PATH)}"
    )

    # ---------------------------------------------------
    # Load Each CSV
    # ---------------------------------------------------

    for table_name, filename in DATASETS.items():

        filepath = os.path.join(
            DATA_FOLDER,
            filename
        )

        print(
            f"\nLoading {filename}..."
        )

        connection.execute(
            f"""
            CREATE OR REPLACE TABLE {table_name} AS
            SELECT *
            FROM read_csv_auto('{filepath}')
            """
        )

        row_count = connection.execute(
            f"""
            SELECT COUNT(*)
            FROM {table_name}
            """
        ).fetchone()[0]

        print(
            f"Created table: {table_name} "
            f"| Rows: {row_count:,}"
        )

    # ---------------------------------------------------
    # Close Connection
    # ---------------------------------------------------

    connection.close()

    print("\n" + "=" * 60)
    print("DATA LOADING COMPLETED")
    print("=" * 60)


# -------------------------------------------------------
# Entry Point
# -------------------------------------------------------

if __name__ == "__main__":

    load_data()