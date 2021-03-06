from datetime import datetime, timedelta
import os

from airflow import DAG
from airflow.models import Variable
from airflow.operators.bash import BashOperator
from airflow.operators.python_operator import PythonOperator
from airflow.utils.dates import days_ago

from operators.process_data import process_data
from operators.temporary_data import fetch_static_api


default_args = {
    'owner': 'nacnano',
    'depends_on_past': False,
    'retries': 5,
    'email': ['chotpisit080916c@gmail.com'],
    'email_on_failure': True,
    'email_on_retry': True,
    'retry_delay': timedelta(minutes=1),
}
with DAG(
    'anime-data-warehouse',
    default_args=default_args,
    description='A request for anime database from API',
    schedule_interval="0 * * * *",
    start_date=days_ago(0),
    catchup=False,
    tags=['anime', 'myanimelist', 'mal', 'anilist']
) as dag:

    # setup_folder = BashOperator(
    #     task_id = 'setup-folder-directory',
    #     # bash_command = f'cd {os.getenv("FOLDER_DIRECTORY")}'
    #     bash_command = 'cd Documents/github/mal-data-warehouse' # <-- Delete this after succesfully debug dotenv python setup - @Nacnano
    # )
    fetch_static_api = PythonOperator(
        task_id='fetch-static-api', 
        python_callable=fetch_static_api
        # bash_command='python3 /home/nacnano/Documents/github/mal-data-warehouse/dags/operators/temporary_data.py'
    )
    # fetch_mal_api = BashOperator(
    #     task_id='fetch-mal-api',
    #     bash_command='python3 /home/nacnano/Documents/github/mal-data-warehouse/dags/operators/fetch_api.py'
    # )
    process_data= PythonOperator(
        task_id='process_data',
        python_callable=process_data
        # bash_command='python3 /home/nacnano/Documents/github/mal-data-warehouse/dags/operators/process_data.py'
    )

fetch_static_api >> process_data