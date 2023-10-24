import mysql.connector
from config import HOST, USER, PASSWORD


class DbConnectionError(Exception):
    pass


# connecting with the DB
def _connect_to_db(db_name):
    cnx = mysql.connector.connect(
        host=HOST,
        user=USER,
        password=PASSWORD,
        auth_plugin="mysql_native_password",
        database=db_name
    )
    return cnx


# Getting shelter information
def db_shelter_overview():
    db_connection = None
    cur = None
    try:
        db_name = "PawsitiveAdoptions"
        db_connection = _connect_to_db(db_name)
        cur = db_connection.cursor()
        print("successfully connected to DB: %s" % db_name)

        query = """SELECT s.shelter_id, s.shelter_name, s.location, s.contact, COUNT(rd.rescued_dog_id) AS total_dogs 
        FROM shelter as s LEFT JOIN rescued_dogs as rd ON s.shelter_id = rd.shelter_id LEFT JOIN dog_details as dd ON 
        rd.details_id = dd.details_id GROUP BY s.shelter_id, s.shelter_name, s.location, s.contact"""
        cur.execute(query)
        result = cur.fetchall()
        shelter_data = []
        for i in result:
            shelter_id, shelter_name, location, contact, total_dogs = i
            shelter = {'shelter_id': shelter_id,
                       'shelter_name': shelter_name,
                       'location': location,
                       'contact_details': contact,
                       'total_dogs': total_dogs}
            shelter_data.append(shelter)
        return shelter_data

    except Exception:
        raise DbConnectionError("Failed to connect to the DB")

    finally:
        if cur:
            cur.close()
        if db_connection:
            db_connection.close()
        print("DB connection is closed")


# Adopting a dog
def db_adopt_dog(location, age, size, sex):
    db_connection = None
    cur = None

    try:
        db_name = "PawsitiveAdoptions"
        db_connection = _connect_to_db(db_name)
        cur = db_connection.cursor()
        shelter_id_query = None
        print("\nSuccessfully connected to DB: %s" % db_name)

        # finding shelter_id based on location of adoptee
        if location == "London":
            # shelter_id 1 = London
            shelter_id_query = """SELECT r.dog_name, d.breed 
            FROM shelter AS s RIGHT JOIN rescued_dogs AS r ON s.shelter_id = r.shelter_id 
            RIGHT JOIN dog_details AS d ON r.details_id = d.details_id 
            WHERE r.shelter_id = 1 AND d.age LIKE "{}%" AND d.size = "{}" AND d.sex = "{}";""".format(age, size, sex)
        elif location == "Belfast":
            # shelter_id 2 = Belfast
            shelter_id_query = """SELECT r.dog_name, d.breed 
            FROM shelter AS s RIGHT JOIN rescued_dogs AS r ON s.shelter_id = r.shelter_id 
            RIGHT JOIN dog_details AS d ON r.details_id = d.details_id
            WHERE r.shelter_id = 2 AND d.age LIKE "{}%" AND d.size = "{}" AND d.sex = "{}";""".format(age, size, sex)
        else:
            print("Invalid location. Please choose London or Belfast.")

        cur.execute(shelter_id_query)
        result = cur.fetchall()
        if result:
            possible_dogs = []
            for i in result:
                dog_name, breed = i
                dogs_list = {
                    'dog_name': dog_name,
                    'breed': breed,
                }
                possible_dogs.append(dogs_list)
            return possible_dogs
        else:
            return "No dogs that meets your criteria at the moment. Please try another time."

    except Exception:
        raise DbConnectionError("Failed to connect to the DB")

    finally:
        if cur:
            cur.close()
        if db_connection:
            db_connection.close()
            print("DB connection is closed")


# Insert details of new members
def db_insert_new_member(new_member):
    db_connection = None  # Initialise db_connection so can use in the finally block
    try:
        db_name = "PawsitiveAdoptions"
        db_connection = _connect_to_db(db_name)
        cur = db_connection.cursor()
        print("\nSuccessfully connected to DB: %s" % db_name)

        query = """INSERT INTO members ({}) VALUES ('{}', '{}')""".format(
            ', '.join(new_member.keys()),
            new_member['full_name'],
            new_member['email_address'],
        )
        cur.execute(query)
        db_connection.commit()
        cur.close()

    except Exception:
        raise DbConnectionError("Failed to connect to the DB")

    finally:
        if db_connection:
            db_connection.close()
            print("DB connection is closed")

# new member information:- mock data to test the  db_insert_new_member function
#new_member = {
    #'full_name': 'Eileen Allen',
   # 'email_address': 'eljallen@gmail.com'
   # }

# calling functions
def main():
    db_shelter_overview()  # overview of the shelter
    db_adopt_dog("Belfast", "adult", "medium", "male")  # calling function to find a dog that meets specific criteria
    db_insert_new_member(new_member) # where new_member argument is displayed just above def main(). uncomment to use with function


# defining main
if __name__ == "__main__":
    main()
