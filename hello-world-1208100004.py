from airflow.operators.bash_operator import BashOperator
from airflow import DAG
from airflow.utils.dates import days_ago


args = {
    "project_id": "hello-world-1208100004",
}

dag = DAG(
    "hello-world-1208100004",
    default_args=args,
    schedule_interval="@once",
    start_date=days_ago(1),
    description="Created with Elyra 3.2.2 pipeline editor using `untitled2.pipeline`.",
    is_paused_upon_creation=False,
)


# Operator source: https://raw.githubusercontent.com/apache/airflow/1.10.15/airflow/operators/bash_operator.py
op_917d8a2e_0cea_45b6_9337_c898ed053e30 = BashOperator(
    task_id="BashOperator",
    bash_command='echo "Hello World!!"',
    xcom_push=True,
    env={},
    output_encoding="utf-8",
    dag=dag,
)
