from airflow import DAG
from airflow.operators.postgres_operator import PostgresOperator

from datetime import datetime, timedelta

default_args = {
    "owner": "airflow",
    "email_on_failure": False,
    "email_on_retry": False,
    "email": "admin@localhost.com",
    "retries": 1,
    "retry_delay": timedelta(minutes=5)
}

with DAG("trips_data_pipeline", start_date=datetime(2022, 8, 1), \
    schedule_interval="@monthly", default_args=default_args, catchup=False) as dag:

    create_total_trips_table = PostgresOperator(
        task_id='create_total_trips_table',
        postgres_conn_id='postgres_conn',
        sql='sql/create_table/create_total_trips_table.sql'
    )

    create_total_distance_table = PostgresOperator(
        task_id='create_total_distance_table',
        postgres_conn_id='postgres_conn',
        sql='sql/create_table/create_total_distance_table.sql'
    )

    create_total_moving_time_table = PostgresOperator(
        task_id='create_total_moving_time_table',
        postgres_conn_id='postgres_conn',
        sql='sql/create_table/create_total_moving_time_table.sql'
    )

    create_total_idle_time_table = PostgresOperator(
        task_id='create_total_idle_time_table',
        postgres_conn_id='postgres_conn',
        sql='sql/create_table/create_total_idle_time_table.sql'
    )

    insert_total_trips_data = PostgresOperator(
        task_id='insert_total_trips_data',
        postgres_conn_id='postgres_conn',
        sql='sql/insert/insert_total_trips_data.sql'
    )

    insert_total_distance_data = PostgresOperator(
        task_id='insert_total_distance_data',
        postgres_conn_id='postgres_conn',
        sql='sql/insert/insert_total_distance_data.sql'
    )

    insert_total_moving_time_data = PostgresOperator(
        task_id='insert_total_moving_time_data',
        postgres_conn_id='postgres_conn',
        sql='sql/insert/insert_total_moving_time_data.sql'
    )

    insert_total_idle_time_data = PostgresOperator(
        task_id='insert_total_idle_time_data',
        postgres_conn_id='postgres_conn',
        sql='sql/insert/insert_total_idle_time_data.sql'
    )

    create_report = PostgresOperator(
        task_id='create_report',
        postgres_conn_id='postgres_conn',
        sql='sql/report.sql'
    )

    create_total_trips_table >> insert_total_trips_data
    create_total_distance_table >> insert_total_distance_data
    create_total_moving_time_table >> insert_total_moving_time_data
    create_total_idle_time_table >> insert_total_idle_time_data