import psycopg
import pandas as pd
import numpy as np

def write_file(file_path : str) -> None:
    records = pd.read_csv(file_path, index_col=0, squeeze=True).replace({np.nan: "NULL"}).to_dict("list")
    for key, value in records.items() :
        print(key)
    with psycopg.connect("dbname=postgres user=my_pg_user host='localhost' password='pg_password'") as connection :
        with connection.cursor() as cur:
            cur.execute("DROP TABLE IF EXISTS races")
            connection.commit()
            cur.execute("""
                CREATE TABLE races (
                    year INTEGER,
                    round INTEGER,
                    circuitId INTEGER,
                    name VARCHAR,
                    date DATE,
                    time TIME,
                    url VARCHAR,
                    fp1_date DATE,
                    fp1_time TIME,
                    fp2_date DATE,
                    fp2_time TIME,
                    fp3_date DATE,
                    fp3_time TIME,
                    quali_date DATE,
                    quali_time TIME,
                    sprint_date DATE,
                    sprint_time TIME
                )
            """)
            connection.commit()

            
                
            for i in range(len(records)) :
                cur.execute("""INSERT INTO races 
                   (year,
                    round,
                    circuitId,
                    name,
                    date,
                    time,
                    url,
                    fp1_date,
                    fp1_time,
                    fp2_date,
                    fp2_time,
                    fp3_date,
                    fp3_time,
                    quali_date,
                    quali_time,
                    sprint_date,
                    sprint_time) 
                    VALUES ({}, {}, {}, \'{}\', \'{}\', \'{}\', \'{}\', \'{}\', \'{}\', \'{}\', \'{}\', \'{}\', \'{}\', \'{}\', \'{}\', \'{}\', \'{}\')""".format
                (
                    records["year"][i],
                    records["round"][i],
                    records["circuitId"][i],
                    records["name"][i],
                    records["date"][i],
                    records["time"][i],
                    records["url"][i],
                    records["fp1_date"][i],
                    records["fp1_time"][i],
                    records["fp2_date"][i],
                    records["fp2_time"][i],
                    records["fp3_date"][i],
                    records["fp3_time"][i],
                    records["quali_date"][i],
                    records["quali_time"][i],
                    records["sprint_date"][i],
                    records["sprint_time"][i]
                ).replace("'NULL'", "NULL"))
            connection.commit()


if __name__ == "__main__" :
    write_file("../tests_data/races.csv")