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



def get_adoption_info(location, age, size, sex):
    try:
        db_name = "PawsitiveAdoptions"
        db_connection = _connect_to_db(db_name)
        cur = db_connection.cursor()
        print("\nSucessfully connected to DB: %s" % db_name)
        print(f"The dogs available for adoption that meet your criteria in {location} are:")

        # commented out inputs from main.py (uncomment and delete arguments from get_adoption_info() in main() function to activate in console)
        #location = input("Where are you looking to adopt from? London or Belfast?")
        #age = input("What age group of dog are you looking for? (Puppy, Adult, Senior): ")
        #size = input("What size of dog are you looking for? (Small, Medium, Large): ")
        #sex = input("What gender of dog are you looking for? (Male, Female): ")

        # finding shelter_id based on location of adoptee
        if location == "London":
            # shelter_id 1 = London
            shelter_id_query = """SELECT r.dog_name, d.breed 
            FROM shelter AS s RIGHT JOIN rescued_dogs AS r ON s.shelter_id = r.shelter_id 
            RIGHT JOIN dog_details AS d ON r.details_id = d.details_id 
            WHERE r.shelter_id = 1 AND d.age = "{}" AND d.size = "{}" AND d.sex = "{}";""".format(age, size, sex)
        elif location == "Belfast":
            # shelter_id 2 = Belfast
            shelter_id_query = """SELECT r.dog_name, d.breed 
            FROM shelter AS s RIGHT JOIN rescued_dogs AS r ON s.shelter_id = r.shelter_id 
            RIGHT JOIN dog_details AS d ON r.details_id = d.details_id
            WHERE r.shelter_id = 2 AND d.age = "{}" AND d.size = "{}" AND d.sex = "{}";""".format(age, size, sex)
        else:
            print("Invalid location. Please choose London or Belfast.")

        cur.execute(shelter_id_query)
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
def insert_new_dog_info():
    try:
        db_name = "PawsitiveAdoptions"
        db_connection = _connect_to_db(db_name)
        cur = db_connection.cursor()
        print("\nSucessfully connected to DB: %s" % db_name)


        # First query finds the amount of existing dogs in the database to assign new dog_id and detail_id
        number_of_dogs_query = """SELECT COUNT(rescued_dog_id) AS no_of_dogs FROM rescued_dogs;"""

        cur.execute(number_of_dogs_query)
        result = cur.fetchall()

        # converting number_of_dogs into list from tuple to access value
        for i in result:
            list_number_of_dogs = list(i)

        # new variables to give new dogs their rescued_dog_id and dog_details_id
        new_rescued_dog_id = list_number_of_dogs[0] + 1
        new_rescued_dog_detail_id = list_number_of_dogs[0] + 1


        # dictionaries for new dogs here. Stored inside function to find correct rescued_dog_id and dog_details_id
        # rescued dog information goes here
        dog_information = {
            'rescued_dog_id': new_rescued_dog_id,
            'dog_name': 'Mabel',
            'temperament': 'calm'
        }

        # rescued dog details go here
        dog_details = {
            'details_id': new_rescued_dog_detail_id,
            # for age: Puppy (<1 year) OR Adult (1-7 years) OR Senior (7< years)
            'age': 'Adult (1-7 years)',
            # for size: Small OR Medium OR Large OR Giant
            'size': 'Medium',
            'sex': 'Female',
            'breed': 'Mixed breed'
        }

        dog_information_query = """INSERT INTO rescued_dogs ({}) VALUES ('{}', '{}', '{}')""".format(
            ', '.join(dog_information.keys()),
            dog_information['rescued_dog_id'],
            dog_information['dog_name'],
            dog_information['temperament']
        )

        dog_details_query = """INSERT INTO dog_details ({}) VALUES ('{}', '{}', '{}', '{}', '{}')""".format(
            ', '.join(dog_details.keys()),
            dog_details['details_id'],
            dog_details['age'],
            dog_details['size'],
            dog_details['sex'],
            dog_details['breed']
        )

        cur.execute(dog_information_query)
        cur.execute(dog_details_query)

        db_connection.commit()
        cur.close()
        print("Dog information and details added to DB")

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
   insert_new_dog_info()


#defining main 
if __name__ == "__main__":
    main()
