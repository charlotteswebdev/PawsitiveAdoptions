import mysql.connector

def connect_to_database():
    connection = mysql.connector.connect(
        host='localhost',
        user='root',
        password='1234!',  # Replace with your MySQL password
        database='wondermap'  # Replace with your WonderMap database name
    )
    return connection

def test_connection():
    db_connection = connect_to_database()
    cur = db_connection.cursor()
    print('Connected to DB')


def select_category(category):
    try:
        db_connection = connect_to_database()
        cur = db_connection.cursor()
        print('Connected to DB')

        if not category:
            query = f'SELECT * FROM events'
            cur.execute(query)
            result = cur.fetchall()
            for i in result:
                print(i)

        else:
            query = f'SELECT * FROM events WHERE category = "{category}"'
            cur.execute(query)
            result = cur.fetchall()
            for i in result:
                print(i)

        cur.close()

    except:
        print('Something went wrong')

    finally:
        if db_connection:
            db_connection.close()
            print('DB connection closed')

def get_all_categories():
    try:
        db_connection = connect_to_database()
        cur = db_connection.cursor()
        print('Connected to DB')

        query = 'SELECT DISTINCT category FROM events'
        cur.execute(query)
        categories = cur.fetchall()
        for i in categories:
            print(i)

        cur.close()

    except:
        print('Something went wrong')

    finally:
        if db_connection:
            db_connection.close()
            print('DB connection closed')
