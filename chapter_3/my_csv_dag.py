"""
A simple Airflow DAG that reads a *.csv file then converts it to a *.json file.
"""

import datetime
from datetime import timedelta

from airflow import DAG
from airflow.operators.bash_operator import BashOperator
from airflow.operators.python_operator import PythonOperator

import pandas


def csv_to_json():
    df = pandas.read_csv(
        "~/data_engineering_with_python/chapter_3/csv_files/data.csv"
    )
    for index, row in df.iterrows():
        print(row["name"])
    df.to_json(
        "~/data_engineering_with_python/chapter_3/json_files/from_airflow.json",
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
