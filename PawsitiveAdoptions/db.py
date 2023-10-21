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




# Finding a dog to match criteria
def get_adoption_info(location, age, size, sex):
    try:
        db_name = "PawsitiveAdoptions"
        db_connection = _connect_to_db(db_name)
        cur = db_connection.cursor()
        print("\nSucessfully connected to DB: %s" % db_name)
        print(f"The dogs available for adoption that meet your criteria in {location} are:")

        # commented out inputs from main.py... uncomment and delete arguments from get_adoption_info() in main() function to activate in console
        #location = input("Where are you looking to adopt from? London or Belfast?")
        #age = input("What age group of dog are you looking for? (Puppy, Adult, Senior): ")
        #size = input("What size of dog are you looking for? (Small, Medium, Large): ")
        #sex = input("What gender of dog are you looking for? (Male, Female): ")

        if location == "London":
            # shelter_id 1 = London
            query = """SELECT r.dog_name, d.breed 
            FROM shelter AS s RIGHT JOIN rescued_dogs AS r ON s.shelter_id = r.shelter_id 
            RIGHT JOIN dog_details AS d ON r.details_id = d.details_id 
            WHERE r.shelter_id = 1 AND d.age = "{}" AND d.size = "{}" AND d.sex = "{}";""".format(age, size, sex)
        elif location == "Belfast":
            # shelter_id 2 = Belfast
            query = """SELECT r.dog_name, d.breed 
            FROM shelter AS s RIGHT JOIN rescued_dogs AS r ON s.shelter_id = r.shelter_id 
            RIGHT JOIN dog_details AS d ON r.details_id = d.details_id
            WHERE r.shelter_id = 2 AND d.age = "{}" AND d.size = "{}" AND d.sex = "{}";""".format(age, size, sex)
        else:
            print("Invalid location. Please choose London or Belfast.")

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
    # calling function to find a dog that meets specific criteria
   get_adoption_info("Belfast", "Adult (1-7 years)", "medium", "male")


#defining main 
if __name__ == "__main__":
    main()
