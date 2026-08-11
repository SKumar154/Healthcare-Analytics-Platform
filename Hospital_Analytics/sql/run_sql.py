import duckdb

connection = duckdb.connect(
    "../healthcare.duckdb"
)

with open("exploration.sql", "r") as file:

    sql_script = file.read()

statements = sql_script.split(";")

for statement in statements:

    statement = statement.strip()

    if statement:

        print("\n" + "=" * 60)

        result = connection.execute(
            statement
        ).fetchdf()

        print(result)

connection.close()