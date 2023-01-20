@ECHO OFF

pip3 install virtualenv

virtualenv venv_tests_data

pip install pandas
pip install "psycopg[binary]"

pip install dbt-postgres

pip install great_expectations

pip install -U pytest

PAUSE