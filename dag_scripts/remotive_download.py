from datetime import datetime, timedelta
import airflow
import requests
import requests.exceptions as requests_exceptions
from airflow import DAG
from airflow.operators.bash import BashOperator
from airflow.operators.python import PythonOperator
from airflow.providers.http.operators.http import SimpleHttpOperator
from airflow.utils.dates import days_ago

# Default arguments for the DAG
default_args = {
    'owner': 'airflow',
    'depends_on_past': False,
    'start_date': pendulum.today('UTC').add(days=-1),
    'email_on_failure': False,
    'email_on_retry': False,
    'retries': 1,
    'retry_delay': timedelta(minutes=5),
}

# Instantiate the DAG
dag = DAG(
    'api_query_dag',
    default_args=default_args,
    description='DAG to query an API',
    schedule = timedelta(days=1),  # Run the DAG daily
)
 # Function to process the API response
def process_api_response(response):
    # Implement your processing logic here
    print(response.text)

    
# Task to query the API using SimpleHttpOperator
query_api_task = SimpleHttpOperator(
    task_id='query_api',
    http_conn_id='my_api_connection',  # Set up the connection details in the Airflow UI
    endpoint='https://remotive.com/api/remote-jobs',       # The API endpoint to query
    method='GET',                      # HTTP method (GET, POST, etc.)
    headers={},                        # Optional headers for the API request
    response_check=lambda response: True,  # Custom response check, you can implement your own
    log_response=True,                # Log the API response
    on_failure_callback=None,          # Optional callback on failure
    on_success_callback=None,          # Optional callback on success
    python_callable=process_api_response,  # Function to process the API response
    dag=dag,
)

# Set task dependencies
query_api_task

if __name__ == "__main__":
    dag.cli()




