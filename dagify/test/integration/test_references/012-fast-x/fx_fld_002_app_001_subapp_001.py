# Apache Airflow Base Imports
from airflow import DAG
from airflow.decorators import task
from airflow.sensors.external_task import ExternalTaskMarker
import datetime
# Apache Airflow Custom & DAG/Task Specific Imports
from airflow.providers.ssh.operators.ssh import SSHOperator

default_args = {
    'owner': 'airflow',
}

with DAG(
    dag_id="fx_fld_002_app_001_subapp_001",
    start_date=datetime.datetime(2024, 1, 1),
    #schedule="@daily",
    schedule_interval='*/5 * * * *',
    catchup=False,
) as dag:

    # DAG Tasks
    fx_fld_002_app_001_subapp_001_job_001 = SSHOperator(
      task_id="fx_fld_002_app_001_subapp_001_job_001",
      command="",
      dag=dag,
    )

    fx_fld_002_app_001_subapp_001_job_002 = SSHOperator(
      task_id="fx_fld_002_app_001_subapp_001_job_002",
      command="",
      dag=dag,
    )

    fx_fld_002_app_001_subapp_001_job_003 = SSHOperator(
      task_id="fx_fld_002_app_001_subapp_001_job_003",
      command="",
      dag=dag,
    )


    
    # Airflow Task Internal Dependencies
    fx_fld_002_app_001_subapp_001_job_001 >> [fx_fld_002_app_001_subapp_001_job_002, fx_fld_002_app_001_subapp_001_job_003]
    fx_fld_002_app_001_subapp_001_job_002 >> [fx_fld_002_app_001_subapp_001_job_003]
    

    