"""
=========================================================
Healthcare Analytics Platform
Helper Functions
=========================================================

Reusable utility functions used throughout the
dataset generation process.
"""

import random
import string
from datetime import datetime, timedelta

import numpy as np

from faker import Faker

from config import RANDOM_SEED

# -------------------------------------------------------
# Initialisation
# -------------------------------------------------------

fake = Faker("en_IN")

random.seed(RANDOM_SEED)
np.random.seed(RANDOM_SEED)
Faker.seed(RANDOM_SEED)

# -------------------------------------------------------
# ID Generators
# -------------------------------------------------------

def generate_patient_id(number):
    """
    Example:
    PAT000001
    """

    return f"PAT{number:06d}"


def generate_doctor_id(number):
    """
    Example:
    DOC0001
    """

    return f"DOC{number:04d}"


def generate_hospital_id(number):
    """
    Example:
    HOS001
    """

    return f"HOS{number:03d}"


# -------------------------------------------------------
# Name Generator
# -------------------------------------------------------

def generate_name():

    return fake.name()


# -------------------------------------------------------
# BMI
# -------------------------------------------------------

def calculate_bmi(height_cm, weight_kg):

    height_m = height_cm / 100

    bmi = weight_kg / (height_m ** 2)

    return round(bmi, 1)


# -------------------------------------------------------
# Random Date
# -------------------------------------------------------

def random_date(start_year=2022, end_year=2025):

    start = datetime(start_year, 1, 1)

    end = datetime(end_year, 12, 31)

    difference = (end - start).days

    random_days = random.randint(0, difference)

    return (start + timedelta(days=random_days)).date()


# -------------------------------------------------------
# Weighted Choice
# -------------------------------------------------------

def weighted_choice(options, weights):

    return random.choices(
        population=options,
        weights=weights,
        k=1
    )[0]


# -------------------------------------------------------
# Random Pincode
# -------------------------------------------------------

def generate_pincode():

    return random.randint(100000, 999999)


# -------------------------------------------------------
# Random Phone Number
# -------------------------------------------------------

def generate_phone():

    return "9" + "".join(random.choices(string.digits, k=9))


# -------------------------------------------------------
# Random Email
# -------------------------------------------------------

def generate_email(name):

    username = name.lower().replace(" ", ".")

    domains = [
        "gmail.com",
        "yahoo.com",
        "outlook.com"
    ]

    return f"{username}@{random.choice(domains)}"