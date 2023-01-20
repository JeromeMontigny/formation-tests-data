//sur linux
./create_venv_wsl.sh

//ou sur windows, double cliquez sur le fichier create_venv_windows

//pour linux : 
source tests_data/bin/activate

//pour windows :
myenv\Scripts\activate

//docker run -d \
//	--name postgres-db \
//	-e POSTGRES_PASSWORD=pg_password \
//  -e POSTGRES_USER=my_pg_user \
//	-v /pg_data:/var/lib/postgresql/data \
//  -p 5432:5432 \
//	postgres:15

// lancez cette commande pour créer le docker pour pgsql
docker run -d --name postgres-db -e POSTGRES_PASSWORD=pg_password -e POSTGRES_USER=my_pg_user -v /pg_data:/var/lib/postgresql/data -p 5432:5432 postgres:15

//pour arrêter le container
docker stop postgres-db

// pour relancer le container
docker run postgres-db 