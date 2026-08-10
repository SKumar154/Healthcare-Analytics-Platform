"""
=========================================================
Healthcare Analytics Platform
Relationship Validation
=========================================================

Validates the keys and relationships between the
healthcare database tables.
=========================================================
"""

import duckdb


# -------------------------------------------------------
# Database Connection
# -------------------------------------------------------

DATABASE_PATH = "../healthcare.duckdb"

connection = duckdb.connect(
    DATABASE_PATH
)


# =======================================================
# 1. PRIMARY KEY UNIQUENESS
# =======================================================

print("=" * 60)
print("PRIMARY KEY UNIQUENESS CHECK")
print("=" * 60)


primary_keys = {
    "hospitals": "hospital_id",
    "doctors": "doctor_id",
    "patients": "patient_id"
}


for table, column in primary_keys.items():

    total_rows = connection.execute(
        f"""
        SELECT COUNT(*)
        FROM {table}
        """
    ).fetchone()[0]

    unique_values = connection.execute(
        f"""
        SELECT COUNT(DISTINCT {column})
        FROM {table}
        """
    ).fetchone()[0]

    duplicate_count = (
        total_rows - unique_values
    )

    print(
        f"\n{table}.{column}"
    )

    print(
        f"Total rows      : {total_rows:,}"
    )

    print(
        f"Unique values   : {unique_values:,}"
    )

    print(
        f"Duplicate rows  : {duplicate_count:,}"
    )


# =======================================================
# 2. DOCTOR → HOSPITAL
# =======================================================

print("\n" + "=" * 60)
print("DOCTOR → HOSPITAL RELATIONSHIP")
print("=" * 60)


orphan_doctors = connection.execute(
    """
    SELECT COUNT(*)
    FROM doctors d
    LEFT JOIN hospitals h
        ON d.hospital_id = h.hospital_id
    WHERE h.hospital_id IS NULL
    """
).fetchone()[0]


print(
    f"\nDoctors with invalid hospital_id: "
    f"{orphan_doctors:,}"
)


# =======================================================
# 3. DIAGNOSIS → PATIENT
# =======================================================

print("\n" + "=" * 60)
print("DIAGNOSIS → PATIENT RELATIONSHIP")
print("=" * 60)


orphan_diagnosis_patients = connection.execute(
    """
    SELECT COUNT(*)
    FROM diagnosis d
    LEFT JOIN patients p
        ON d.patient_id = p.patient_id
    WHERE p.patient_id IS NULL
    """
).fetchone()[0]


print(
    f"\nDiagnosis records with invalid "
    f"patient_id: "
    f"{orphan_diagnosis_patients:,}"
)


# =======================================================
# 4. DIAGNOSIS → DOCTOR
# =======================================================

print("\n" + "=" * 60)
print("DIAGNOSIS → DOCTOR RELATIONSHIP")
print("=" * 60)


orphan_diagnosis_doctors = connection.execute(
    """
    SELECT COUNT(*)
    FROM diagnosis d
    LEFT JOIN doctors doc
        ON d.doctor_id = doc.doctor_id
    WHERE doc.doctor_id IS NULL
    """
).fetchone()[0]


print(
    f"\nDiagnosis records with invalid "
    f"doctor_id: "
    f"{orphan_diagnosis_doctors:,}"
)


# =======================================================
# 5. BILLING → PATIENT
# =======================================================

print("\n" + "=" * 60)
print("BILLING → PATIENT RELATIONSHIP")
print("=" * 60)


orphan_billing = connection.execute(
    """
    SELECT COUNT(*)
    FROM billing b
    LEFT JOIN patients p
        ON b.patient_id = p.patient_id
    WHERE p.patient_id IS NULL
    """
).fetchone()[0]


print(
    f"\nBilling records with invalid "
    f"patient_id: "
    f"{orphan_billing:,}"
)


# =======================================================
# 6. LIFESTYLE → PATIENT
# =======================================================

print("\n" + "=" * 60)
print("LIFESTYLE → PATIENT RELATIONSHIP")
print("=" * 60)


orphan_lifestyle = connection.execute(
    """
    SELECT COUNT(*)
    FROM lifestyle l
    LEFT JOIN patients p
        ON l.patient_id = p.patient_id
    WHERE p.patient_id IS NULL
    """
).fetchone()[0]


print(
    f"\nLifestyle records with invalid "
    f"patient_id: "
    f"{orphan_lifestyle:,}"
)


# =======================================================
# 7. FEEDBACK → PATIENT
# =======================================================

print("\n" + "=" * 60)
print("FEEDBACK → PATIENT RELATIONSHIP")
print("=" * 60)


orphan_feedback = connection.execute(
    """
    SELECT COUNT(*)
    FROM feedback f
    LEFT JOIN patients p
        ON f.patient_id = p.patient_id
    WHERE p.patient_id IS NULL
    """
).fetchone()[0]


print(
    f"\nFeedback records with invalid "
    f"patient_id: "
    f"{orphan_feedback:,}"
)


# =======================================================
# CLOSE CONNECTION
# =======================================================

connection.close()


print("\n" + "=" * 60)
print("RELATIONSHIP VALIDATION COMPLETED")
print("=" * 60)