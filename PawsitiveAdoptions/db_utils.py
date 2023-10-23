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
            print(shelter)
        return shelter_data

    except Exception:
        raise DbConnectionError("Failed to connect to the DB")

    finally:
        if cur:
            cur.close()
        if db_connection:
            db_connection.close()
        print("DB connection is closed")


def db_adopt_dog(location, age, size, sex):
    try:
        db_name = "PawsitiveAdoptions"
        db_connection = _connect_to_db(db_name)
        cur = db_connection.cursor()
        print("\nSucessfully connected to DB: %s" % db_name)
        print(f"The dogs available for adoption that meet your criteria in {location} are:")

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
                breed, dog_name = i
                dogs_list = {
                    'breed': breed,
                    'dog_name': dog_name,
                }
                possible_dogs.append(dogs_list)
                print(dogs_list)
            return possible_dogs
        else:
            return 'Sorry, No dogs meet your criteria'

    except Exception:
        raise DbConnectionError("Failed to connect to the DB")

    finally:
        if cur:
            cur.close()
        if db_connection:
            db_connection.close()
            print("DB connection is closed")


def insert_new_member():
    try:
        db_name = "PawsitiveAdoptions"
        db_connection = _connect_to_db(db_name)
        cur = db_connection.cursor()
        print("\nSucessfully connected to DB: %s" % db_name)


        query = """INSERT INTO members ({}) VALUES ('{}', '{}')""".format(
            ', '.join(new_member.keys()),
            new_member['full_name'],
            new_member['email_address'],
        )

        cur.execute(query)

        db_connection.commit()
        cur.close()
        print("New member name and email added to DB")

    except Exception:
        raise DbConnectionError("Failed to connect to the DB")

    else:
        if db_connection:
            db_connection.close()
            print("DB connection is closed")


#new member information to enter into db goes here:
new_member = {
    'full_name': 'Eileen Allen',
    'email_address': 'eljallen@gmail.com'
    }


# calling functions
def main():
    # db_shelter_overview()
    # calling function to find a dog that meets specific criteria
    db_adopt_dog("Belfast", "Adult", "medium", "male")
    insert_new_member()


# defining main
if __name__ == "__main__":
    main()

