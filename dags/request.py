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

    t1 = BashOperator(
        task_id='fetch-api',
        bash_command='python /dags/operators/fetch_api.py'
    )