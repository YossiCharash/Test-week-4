import psycopg2

from db import get_db_connection


def normalize_db():
    source_conn = get_db_connection()
    target_conn = psycopg2.connect(
        dbname="missions_wwii",
        user="postgres",
        password="1234",
        host="localhost",
        port="5432"
    )

    try :
        query1 = """
            CREATE TABLE  target_country (
                    target_country_id SERIAL PRIMARY KEY,
                    country_name VARCHAR(100),
            )
        """

        query2 = """
            CREATE TABLE  target_city(
                    target_city_id SERIAL PRIMARY KEY,
                    city_name VARCHAR(100),
                    country_id int references target_country(target_country_id),
            )
        """
        query3 = """
            CREATE TABLE  target_type (
                    target_type_id SERIAL PRIMARY KEY,
                    type_name VARCHAR(100),
                    target_city_id int references target_city(target_city_id),
            )
        """

        # query4 = """
        #     CREATE TABLE  target_industry(
        #             target_industry_id SERIAL PRIMARY KEY,
        #             industry_name VARCHAR(100),
        #     )
        # """
        query4 = """
            CREATE TABLE  target_location(
                    target_location_id SERIAL PRIMARY KEY,
                    target_latitude float,
                    target_longitude float,
            )
        """

        query5 = """
             CREATE TABLE  target_details(
                     target_details_id SERIAL PRIMARY KEY,
                     target_type_and_city_id int references target_type(target_type_id),
                     target_location_id int references target_location(target_location_id),
             )
         """
        query6 = """
             alter table mission
             add location_and_city_id int references target_details (target_details_id),
             )
         """




        # execute the queries
        cur = target_conn.cursor()
        cur.executemany([query1, query2,query4, query3, query5, query6])
        target_conn.commit()

        s_cur = source_conn.cursor()
        s_cur.execute("SELECT * FROM mission")
        while True:
            mission_row = s_cur.fetchone()
            if mission_row is None:
                break

            country_name = mission_row[14]
            city_name = mission_row[15]
            type_name = mission_row[16]
            target_latitude = mission_row[19]
            target_longitude = mission_row[20]

            cur.execute(f"INSERT INTO target_country (country_name) VALUES ('{country_name}') RETURNING target_country_id")
            country_id = cur.fetchone()[0]

            cur.execute(f"INSERT INTO target_city (city_name,country_id) VALUES ('{city_name}',{country_id}) RETURNING target_city_id")
            city_id = cur.fetchone()[0]

            cur.execute(f"INSERT INTO target_type (type_name,target_city_id) VALUES ('{type_name}',{city_id}) RETURNING target_type_id")
            type_id = cur.fetchone()[0]

            cur.execute(f"INSERT INTO target_type (target_latitude, target_longitude) VALUES ({target_latitude},{target_longitude}) RETURNING target_location_id")
            location_id = cur.fetchone()[0]

            cur.execute(f"INSERT INTO target_details (target_type_and_city_id,target_location_id) VALUES ({type_id},{location_id}) RETURNING target_location_id")
            location_and_city_id = cur.fetchone()[0]

            cur.execute(f"UPDATE mission SET  location_and_city_id = {location_and_city_id} WHERE city_name = '{city_name}'"
                        f"and type_name = '{type_name}' and target_latitude = {target_latitude} and target_longitude = {target_longitude}")



    except Exception as e:
        print(e)
    finally:
        target_conn.close()


