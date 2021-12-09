from airflow.contrib.operators.kubernetes_pod_operator import KubernetesPodOperator
from airflow.operators.bash_operator import BashOperator
from airflow import DAG
from airflow.utils.dates import days_ago


args = {
    "project_id": "test-dag-1208205833",
}

dag = DAG(
    "test-dag-1208205833",
    default_args=args,
    schedule_interval="@once",
    start_date=days_ago(1),
    description="Created with Elyra 3.2.2 pipeline editor using `test-dag.pipeline`.",
    is_paused_upon_creation=False,
)


# Operator source: https://raw.githubusercontent.com/apache/airflow/1.10.15/airflow/operators/bash_operator.py
op_9403efb0_ba2e_46f8_a760_fc9f3d1a112c = BashOperator(
    task_id="Hello_World_from_Bash",
    bash_command='echo "Hello World"',
    xcom_push=False,
    env={},
    output_encoding="utf-8",
    dag=dag,
)


# Operator source: code-home/myjupter/HelloJulia.ipynb
op_f63afc8b_0c43_459d_8472_04725c0b2589 = KubernetesPodOperator(
    name="Julia_Test",
    namespace="default",
    image="jupyter/datascience-notebook",
    cmds=["sh", "-c"],
    arguments=[
        "mkdir -p ./jupyter-work-dir/ && cd ./jupyter-work-dir/ && curl -H 'Cache-Control: no-cache' -L https://raw.githubusercontent.com/elyra-ai/elyra/v3.2.2/elyra/airflow/bootstrapper.py --output bootstrapper.py && curl -H 'Cache-Control: no-cache' -L https://raw.githubusercontent.com/elyra-ai/elyra/v3.2.2/etc/generic/requirements-elyra.txt --output requirements-elyra.txt && python3 -m pip install packaging && python3 -m pip freeze > requirements-current.txt && python3 bootstrapper.py --cos-endpoint http://10.8.0.106:9099 --cos-bucket elyra-test --cos-directory 'test-dag-1208205833' --cos-dependencies-archive 'HelloJulia-f63afc8b-0c43-459d-8472-04725c0b2589.tar.gz' --file 'code-home/myjupter/HelloJulia.ipynb' "
    ],
    task_id="Julia_Test",
    env_vars={
        "ELYRA_RUNTIME_ENV": "airflow",
        "AWS_ACCESS_KEY_ID": "admin",
        "AWS_SECRET_ACCESS_KEY": "password",
        "ELYRA_ENABLE_PIPELINE_INFO": "True",
        "ELYRA_RUN_NAME": "test-dag-1208205833-{{ ts_nodash }}",
    },
    in_cluster=True,
    config_file="None",
    dag=dag,
)

op_f63afc8b_0c43_459d_8472_04725c0b2589 << op_9403efb0_ba2e_46f8_a760_fc9f3d1a112c
