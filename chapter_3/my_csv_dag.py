"""
A simple Airflow DAG that converts a *.csv file into JSON.
"""
import datetime
from datetime import timedelta
import os

from airflow import DAG
from airflow.operators.bash_operator import BashOperator
from airflow.operators.python_operator import PythonOperator
from airflow.models import Variable

import pandas


def csv_to_json():
    # Import the PATH_TO_ROOT Airflow.
    path_to_root = Variable.get("PATH_TO_ROOT")

    # Read the *.csv file using pandas.
    df = pandas.read_csv(
        os.path.join(path_to_root, "chapter_3", "csv_files", "data.csv")
    )
    for index, row in df.iterrows():
        print(row["name"])
    
    # Convert data into JSON.
    df.to_json(
        os.path.join(path_to_root, "chapter_3", "json_files", "from_airflow.json"), 
        orient="records"
    )


default_args = {
    "owner": "debian_user",
    "start_date": datetime.datetime(2020, 3, 18),
    "retries": 1,
    "retry_delay": timedelta(minutes=5),
}
with DAG(
        "MyCsvDag",
        default_args=default_args,
        schedule_interval=timedelta(minutes=5)
) as dag:
    print_starting = BashOperator(
        task_id="starting",
        bash_command='echo "I am reading the CSV now..."',
    )
    csv_to_json = PythonOperator(
        task_id="convertCsvToJson",
        python_callable=csv_to_json
    )
    print_starting.set_downstream(csv_to_json)
