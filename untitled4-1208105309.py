from airflow.contrib.operators.kubernetes_pod_operator import KubernetesPodOperator
from airflow.operators.bash_operator import BashOperator
from airflow import DAG
from airflow.utils.dates import days_ago


args = {
    "project_id": "untitled4-1208105309",
}

dag = DAG(
    "untitled4-1208105309",
    default_args=args,
    schedule_interval="@once",
    start_date=days_ago(1),
    description="Created with Elyra 3.2.2 pipeline editor using `untitled4.pipeline`.",
    is_paused_upon_creation=False,
)


# Operator source: https://raw.githubusercontent.com/apache/airflow/1.10.15/airflow/operators/bash_operator.py
op_35c41524_4878_461b_a85f_8e5ea2ca0354 = BashOperator(
    task_id="BashOperator",
    xcom_push=False,
    env={},
    output_encoding="utf-8",
    bash_command='echo "Hello World from Airflow"',
    dag=dag,
)


# Operator source: code-home/myjupter/HelloJulia.ipynb
op_98fe37b2_b803_4df8_b3a1_8238d68b271a = KubernetesPodOperator(
    name="HelloJulia",
    namespace="default",
    image="jupyter/datascience-notebook",
    cmds=["sh", "-c"],
    arguments=[
        "mkdir -p ./jupyter-work-dir/ && cd ./jupyter-work-dir/ && curl -H 'Cache-Control: no-cache' -L https://raw.githubusercontent.com/elyra-ai/elyra/v3.2.2/elyra/airflow/bootstrapper.py --output bootstrapper.py && curl -H 'Cache-Control: no-cache' -L https://raw.githubusercontent.com/elyra-ai/elyra/v3.2.2/etc/generic/requirements-elyra.txt --output requirements-elyra.txt && python3 -m pip install packaging && python3 -m pip freeze > requirements-current.txt && python3 bootstrapper.py --cos-endpoint http://10.8.0.106:9099 --cos-bucket elyra-test --cos-directory 'untitled4-1208105309' --cos-dependencies-archive 'HelloJulia-98fe37b2-b803-4df8-b3a1-8238d68b271a.tar.gz' --file 'code-home/myjupter/HelloJulia.ipynb' "
    ],
    task_id="HelloJulia",
    env_vars={
        "ELYRA_RUNTIME_ENV": "airflow",
        "AWS_ACCESS_KEY_ID": "admin",
        "AWS_SECRET_ACCESS_KEY": "password",
        "ELYRA_ENABLE_PIPELINE_INFO": "True",
        "ELYRA_RUN_NAME": "untitled4-1208105309-{{ ts_nodash }}",
    },
    in_cluster=True,
    config_file="None",
    dag=dag,
)

op_98fe37b2_b803_4df8_b3a1_8238d68b271a << op_35c41524_4878_461b_a85f_8e5ea2ca0354
