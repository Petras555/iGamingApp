import mysql.connector


db = mysql.connector.connect(
    host="Localhost",
    user="root",
    password="root",
)

mycursor = db.cursor()

mycursor.execute("CREATE DATABASE mysqldatabase")

from database import db_query, connection

create_table_query = "CREATE TABLE Clients (ClientID int, Username VARCHAR(50) PRIMARY KEY, Password VARCHAR(50))"
create_table2_query = "CREATE TABLE Transactions (TransactionID int PRIMARY KEY AUTO_INCREMENT,Username VARCHAR(255), DepositAmount int, DepositDate DATETIME, FOREIGN KEY (Username) REFERENCES clients(Username), TransactionType VARCHAR(50))"


db_query(connection, create_table_query)
db_query(connection, create_table2_query)
