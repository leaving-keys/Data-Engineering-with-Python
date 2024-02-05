import psycopg2
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
    data = (1, "Big Bird", "Sesame Street", "Fakeville", "12345")
    print(cursor.mogrify(query, data))
    cursor.execute(query, data)
    conn.commit()
conn.close()
