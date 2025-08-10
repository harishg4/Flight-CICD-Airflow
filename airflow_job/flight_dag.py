from airflow import DAG
from airflow.operators.empty import EmptyOperator
from airflow.operators.python import PythonOperator
from airflow.utils.dates import days_ago
import subprocess


def run_spark_job():
    script_path = "/opt/airflow/spark_job/flight_process.py"
    subprocess.run(["spark-submit", script_path], check=True)


with DAG(
    dag_id="flight_pipeline",
    start_date=days_ago(1),
    schedule_interval="@daily",
    catchup=False,
) as dag:

    start = EmptyOperator(task_id="start")

    run_spark = PythonOperator(
        task_id="spark_process",
        python_callable=run_spark_job,
    )

    validate = EmptyOperator(task_id="validate_output")

    start >> run_spark >> validate
