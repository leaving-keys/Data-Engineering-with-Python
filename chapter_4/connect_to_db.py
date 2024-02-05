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
    print("Connected!");
conn.close()
