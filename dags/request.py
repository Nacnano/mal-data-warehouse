from datetime import datetime, timedelta

from airflow import DAG
from airflow.models import Variable
from airflow.operators.bash import BashOperator

default_args = {
    'owner': 'airflow',
    'depends_on_past': False,
    'retries': 1,
    'retry_delay': timedelta(minutes=5),
}
with DAG(
    'myanimelist-fetch-api',
    default_args=default_args,
    description='Request myanimelist data from API',
    schedule_interval="@once",
    start_date=datetime.strptime("2022-07-01", '%Y-%m-%d'),
    catchup=False
) as dag:

    temporary_data = BashOperator(
        task_id='fetch-static-api',
        bash_command='python /dags/operators/temporary_data.py'
    )
    fetch_api = BashOperator(
        task_id='fetch-mal-api',
        bash_command='python /dags/operators/fetch_api.py'
    )
    process_data= BashOperator(
        task_id='process_data',
        bash_command='python /dags/operators/process_data.py'
    )

temporary_data >> process_data