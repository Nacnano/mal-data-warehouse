from datetime import datetime, timedelta
import os
# from dotenv import load_dotenv
# load_dotenv()
# Bug from python setup T_T

from airflow import DAG
from airflow.models import Variable
from airflow.operators.bash import BashOperator
from airflow.utils.dates import days_ago


default_args = {
    'owner': 'airflow',
    'depends_on_past': False,
    'retries': 4,
    'retry_delay': timedelta(seconds=15),
}
with DAG(
    'anime-data-warehouse',
    default_args=default_args,
    description='A request for anime database from API',
    schedule_interval=timedelta(minutes=1),
    start_date=days_ago(1),
    catchup=False,
    tags=['anime', 'myanimelist', 'mal', 'anilist']
) as dag:

    setup_folder = BashOperator(
        task_id = 'setup-folder-directory',
        # bash_command = f'cd {os.getenv("FOLDER_DIRECTORY")}'
        bash_command = 'cd Documents/github/mal-data-warehouse' # <-- Delete this after succesfully debug dotenv python setup - @Nacnano
    )
    fetch_static_api = BashOperator(
        task_id='fetch-static-api', 
        bash_command='python3 /dags/operators/temporary_data.py'
    )
    fetch_mal_api = BashOperator(
        task_id='fetch-mal-api',
        bash_command='python3 /dags/operators/fetch_api.py'
    )
    process_data= BashOperator(
        task_id='process_data',
        bash_command='python3 /dags/operators/process_data.py'
    )

setup_folder >> fetch_static_api >> process_data >> fetch_mal_api