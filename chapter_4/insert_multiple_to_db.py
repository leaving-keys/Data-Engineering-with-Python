import psycopg2
from faker import Faker
from dotenv import find_dotenv, dotenv_values


env_vars = dotenv_values(find_dotenv())
conn_string=f"""
dbname={env_vars["DB_NAME"]}
host='{env_vars["DB_HOST"]}'
user='{env_vars["DB_USER"]}'
password='{env_vars["DB_PASSWORD"]}'
"""
conn = psycopg2.connect(conn_string)
with conn.cursor() as cursor:
    query="""
    INSERT INTO users (id, name, street, city, zip)
    VALUES (%s, %s, %s, %s, %s)
    """
    faker = Faker()
    data = []

    for i in range(2, 1002):
        values = (
            i, faker.name(), faker.street_address(), faker.city(), faker.zipcode(),
        )
        data.append(values)
    data_for_db = tuple(data)
    cursor.executemany(query, data_for_db)
    conn.commit()
conn.close()
