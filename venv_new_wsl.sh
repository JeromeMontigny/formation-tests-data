#!/bin/bash

if ! command -v pip3 &> /dev/null
then
    echo "nameserver 8.8.8.8" | sudo tee /etc/resolv.conf > /dev/null
    apt-get update
    apt-get install python3-pip
fi

if ! command -v virtualenv --version &> /dev/null
then
    pip3 install virtualenv
    echo PATH="$PATH:/home/USER/.local/bin" >> ~/.bashrc
    source ~/.bashrc
fi

virtualenv venv_tests_data

source ./venv_tests_data/bin/activate

pip install pandas
pip install "psycopg[binary]"

pip install dbt-postgres

pip install great_expectations

pip install -U pytest

# TODO : créer la structure avec src, test, __init__, etc
