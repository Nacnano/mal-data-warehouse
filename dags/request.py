from datetime import datetime, timedelta
import os
from dotenv import load_dotenv
load_dotenv()

from airflow import DAG
from airflow.models import Variable
from airflow.operators.bash import BashOperator


default_args = {
    'owner': 'airflow',
    'depends_on_past': False,
    'retries': 4,
    'retry_delay': timedelta(seconds=15),
}
with DAG(
    'myanimelist-fetch-api',
    default_args=default_args,
    description='Request myanimelist data from API',
    schedule_interval="@once",
    start_date=datetime.strptime("2022-07-01", '%Y-%m-%d'),
    catchup=False
) as dag:

    setup = BashOperator(
        task_id = 'setup-folder-directory',
        bash_command = f'cd {os.getenv("FOLDER_DIRECTORY")}'
    )
    fetch_static_api = BashOperator(
        task_id='fetch-static-api', 
        bash_command='python3 /home/nacnano/Documents/github/mal-data-warehouse/dags/operators/temporary_data.py'
    )
    fetch_mal_api = BashOperator(
        task_id='fetch-mal-api',
        bash_command='python3 /home/nacnano/Documents/github/mal-data-warehouse/dags/operators/fetch_api.py'
    )
    process_data= BashOperator(
        task_id='process_data',
        bash_command='python3 /dags/operators/process_data.py'
    )

setup >> fetch_static_api >> process_data >> fetch_mal_api