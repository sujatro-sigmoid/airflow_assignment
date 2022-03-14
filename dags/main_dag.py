from airflow import DAG
from airflow.providers.postgres.operators.postgres import PostgresOperator
from airflow.operators.python import PythonOperator
from pendulum import datetime
from datetime import timedelta
from python_scripts.get_current_weather_data import get_current_weather_data
 
with DAG(
    dag_id="main_dag",
    default_args={
            "retries": 1,
            "retry_delay": timedelta(seconds=30),
        },
    start_date=datetime(year=2022, month=3, day=1),
    schedule_interval="0 6 * * *",
    catchup=False
) as dag:

    task_fetch_weather_data = PythonOperator(
        task_id="fetch_weather_data", 
        python_callable=get_current_weather_data
        )

    task_create_weather_table = PostgresOperator(
        task_id="create_weather_table",
        postgres_conn_id="postgres_default",
        sql="sql/create_weather_table.sql"
    )

    task_populate_weather_table = PostgresOperator(
    task_id="populate_weather_table",
    postgres_conn_id="postgres_default",
    sql="sql/create_weather_table.sql",
    )

    task_fetch_weather_data >> task_create_weather_table >> task_populate_weather_table

    
