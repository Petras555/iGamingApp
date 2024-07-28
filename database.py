import mysql.connector
from mysql.connector import Error


def db_connection():               # Connector to MySQL database,
    connection = None
    try:
        connection = mysql.connector.connect(
            host="Localhost",
            user="root",
            password="root",
            database="mysqldatabase"
        )
        print("Connection Successful to DB")
    except Error as e:
        print(f"The error {e} occurred")
    return connection


def db_query(connection, query, data=None):      #Function for recreating cursor in database
    my_cursor = connection.cursor()
    try:
        my_cursor.execute(query, data)
        print("Operation executed")
    except Error as e:
        print(f"The error {e} occurred")
    return my_cursor


connection = db_connection()

