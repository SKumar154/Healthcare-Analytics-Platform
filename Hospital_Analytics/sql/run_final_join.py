import duckdb


DATABASE_PATH = "../healthcare.duckdb"


connection = duckdb.connect(
    DATABASE_PATH
)


with open(
    "final_join.sql",
    "r"
) as file:

    sql_script = file.read()


connection.execute(
    sql_script
)


print(
    "Final analytical dataset created successfully."
)


result = connection.execute(
    """
    SELECT
        COUNT(*) AS total_rows,
        COUNT(DISTINCT patient_id) AS unique_patients
    FROM raw_analytical_dataset
    """
).fetchdf()


print("\nDataset validation:")
print(result)


connection.close()