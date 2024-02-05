import psycopg2
from dotenv import find_dotenv, dotenv_values


env_vars = dotenv_values(find_dotenv())
conn = psycopg2.connect(
    dbname=env_vars["DB_NAME"],
    host=env_vars["DB_HOST"],
    user=env_vars["DB_USER"],
    password=env_vars["DB_PASSWORD"],
)
with conn.cursor() as cursor:
    query = """
    SELECT
        *
    FROM
        users
    ORDER BY
        id
    """
    cursor.execute(query)
    for record in cursor:
        print(record)
conn.close()
