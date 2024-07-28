import mysql.connector
from mysql.connector import Error


def db_connection():               # Connector to MySQL database,
    connection = None
    try:
        connection = mysql.connector.connect(
            host="db",
            user="root",
            password="root",
            database="db"
        )
        print("Connection Successful to DB")
    except Error as e:
        print(f"The error {e} occurred")
    return connection


def db_query(connection, query, data=None):
    my_cursor = connection.cursor()
    try:
        my_cursor.execute(query, data)
        print("Operation executed")
    except Error as e:
        print(f"The error {e} occurred")
    return my_cursor


create_table_query = "CREATE TABLE Clients (ClientID int, Username VARCHAR(50) PRIMARY KEY, Password VARCHAR(50))"
create_table2_query = "CREATE TABLE Transactions (TransactionID int PRIMARY KEY AUTO_INCREMENT,Username VARCHAR(255), DepositAmount int, DepositDate DATETIME, FOREIGN KEY (Username) REFERENCES clients(Username), TransactionType VARCHAR(50))"
#
# add_account_query = "INSERT INTO Clients (Username, Password) VALUES (%s, %s)"
# delete_table_query = "DROP TABLE Clients"
# delete_table2_query = "DROP TABLE transactions"zz
#
connection = db_connection()

db_query(connection, create_table_query)
db_query(connection, create_table2_query)

print("zdr")