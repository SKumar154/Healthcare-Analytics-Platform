"""
=========================================================
Healthcare Analytics Platform
Database Inspection
=========================================================

This script inspects the DuckDB database to understand:

1. Available tables
2. Row counts
3. Table schemas
4. Primary analytical keys
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
# 1. SHOW AVAILABLE TABLES
# =======================================================

print("=" * 60)
print("AVAILABLE TABLES")
print("=" * 60)

tables = connection.execute(
    "SHOW TABLES"
).fetchall()

for table in tables:

    print(table[0])


# =======================================================
# 2. ROW COUNTS
# =======================================================

print("\n" + "=" * 60)
print("ROW COUNTS")
print("=" * 60)

for table in tables:

    table_name = table[0]

    result = connection.execute(
        f"""
        SELECT COUNT(*)
        FROM {table_name}
        """
    ).fetchone()

    print(
        f"{table_name:<15} "
        f"{result[0]:,} rows"
    )


# =======================================================
# 3. TABLE SCHEMAS
# =======================================================

print("\n" + "=" * 60)
print("TABLE SCHEMAS")
print("=" * 60)

for table in tables:

    table_name = table[0]

    print(
        f"\n--- {table_name.upper()} ---"
    )

    schema = connection.execute(
        f"""
        DESCRIBE {table_name}
        """
    ).fetchall()

    for column in schema:

        column_name = column[0]
        data_type = column[1]

        print(
            f"{column_name:<25} "
            f"{data_type}"
        )


# =======================================================
# 4. CLOSE CONNECTION
# =======================================================

connection.close()

print("\n" + "=" * 60)
print("DATABASE INSPECTION COMPLETED")
print("=" * 60)