from db import get_db_connection
from model import Mission


def get_all_mission():
    con = get_db_connection()
    try:
        cur = con.cursor()
        query = ("SELECT * FROM mission limit 20")
        cur.execute(query)
        rows = cur.fetchall()

        #create new

        # mission_list = []
        # for row in rows:
        #     new_mission = Mission(name=row[15], mission_date=row[2])
        #     mission_list.append(new_mission)
        return True,rows
    except Exception as e:
        print(e)
        return False

