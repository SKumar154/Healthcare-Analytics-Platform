"""

Healthcare Analytics Platform
Configuration File

This file stores every configurable parameter
used throughout the dataset generation process.

Changing values here automatically affects the
entire project.
"""
import os.path

# =======================================================
# DATASET SIZE
# =======================================================

NUM_PATIENTS = 500_000
NUM_DOCTORS = 2_000
NUM_HOSPITALS = 120

# =======================================================
# RANDOMNESS
# =======================================================

RANDOM_SEED = 42

# =======================================================
# DATA QUALITY SETTINGS
# =======================================================

MISSING_VALUE_RATE = 0.05       # 5%

DUPLICATE_RATE = 0.01           # 1%

OUTLIER_RATE = 0.002            # 0.2%

INVALID_VALUE_RATE = 0.005      # 0.5%

# =======================================================
# PATIENT SETTINGS
# =======================================================

MIN_AGE = 1
MAX_AGE = 100

MIN_HEIGHT = 120
MAX_HEIGHT = 200

MIN_WEIGHT = 25
MAX_WEIGHT = 150

# =======================================================
# BILL SETTINGS
# =======================================================

MIN_BILL = 500

MAX_BILL = 500000

# =======================================================
# SATISFACTION
# =======================================================

MIN_RATING = 1

MAX_RATING = 5

# =======================================================
# OUTPUT FOLDER
# =======================================================

OUTPUT_FOLDER = "../data"

# if os.path.exists(OUTPUT_FOLDER):
#     print("Success")
# else:
#     print("Error")