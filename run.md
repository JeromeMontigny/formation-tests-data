docker run . --mount source=./data,target=/? -p 5432:5432

//créer le venv
pip install virtualenv
virtualenv tests_data

//pour linux : 
source tests_data/bin/activate

//pour windows :
myenv\Scripts\activate

pip install EL/src/requirements.txt
pip install "psycopg[binary]"

pip install dbt-postgres

python3 -m pip install great_expectations

docker run -d \
	--name postgres-db \
	-e POSTGRES_PASSWORD=pg_password \
    -e POSTGRES_USER=my_pg_user \
	-v /pg_data:/var/lib/postgresql/data \
    -p 5432:5432 \
	postgres:15

docker run -d --name postgres-db -e POSTGRES_PASSWORD=pg_password -e POSTGRES_USER=my_pg_user -v /pg_data:/var/lib/postgresql/data -p 5432:5432 postgres:15