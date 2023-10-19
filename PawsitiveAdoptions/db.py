import mysql.connector
from config import HOST, USER, PASSWORD

#connecting with the DB 

def _connect_to_db(db_name):
    cnx = mysql.connector.connect(
        host = HOST,
        user = USER,
        password = PASSWORD,
        auth_plugin = "mysql_native_password",
        database = db_name
    )
    return cnx

#Getting shelter information 
def get_shelter_info():
    try: 
        db_name = "PawsitiveAdoptions"
        db_connection = _connect_to_db(db_name)
        cur = db_connection.cursor()
        print("sucessfully connected to DB: %s" % db_name)

        query = """SELECT s.shelter_id, s.shelter_name, s.location, s.contact, COUNT(rd.rescued_dog_id) AS total_dogs FROM shelter as s LEFT JOIN rescued_dogs as rd ON s.shelter_id = rd.shelter_id LEFT JOIN dog_details as dd ON rd.details_id = dd.details_id GROUP BY s.shelter_id, s.shelter_name, s.location, s.contact"""
        cur.execute(query)
        result = cur.fetchall()

        for i in result:
            print(i)
        cur.close()

    except Exception:
        raise DbConnectionError("Failed to connect to the DB")

    else:
        if db_connection:
            db_connection.close()
            print("DB connection is closed")


#calling functions 
def main():
   get_shelter_info()


#defining main 
if __name__ == "__main__":
    main()