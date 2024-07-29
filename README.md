# Introduction
![_b739b877-bfda-4663-af61-b2daa5caf528 (1)](https://github.com/user-attachments/assets/0eac3c6e-86af-45f0-be56-de6d8962e48b)



## Index

- [About](#about)
- [File Structure](#file-structure)
- [Requirements](#Requirements)
- [Instructions](#Instructions)
- [Author](#Author)


## About
Simple iGaming "application" that connects to MySQL database where users can create accounts and make transactions with them in a virtual wallet. Database holds information about every account (userID, username, password) and every transaction that was made with each account(transaction ID, username, amount, transaction type:deposit or withdrawal and date). The project allows to build data within a database which could be used for the following tasks:

*List all users having 3 deposits or more.

*List all users having only 1 withdrawal.

*List 3 users that have made the highest deposits.

*List all deposits for users. Display UserId, UserName, DepositDate, DepositAmount.

*Calculate balances of all users.


### File Structure


| No | File Name | Details 
|----|------------|-------|
| 1  | launcher.py      | a file which should be first used by users to navigate through the project.
| 2  | createdatabase.py| file creates database and mandatory tables within database (1st selection within launcher.py).
| 3  | database.py      | has functions for connecting to databases, that are used in other scripts.
| 4  | gamemenu.py      | game file for creating accounts, doing deposits and withdrawals, and checking the list of all accounts within database (2nd selection within launcher.py).
| 5  | task.py          | file for operating tasks from [About] (#about) section. (3rd selection within launcher.py).
| 6  | classes.py       | separate file for classes, currently contains single a class for the user.
| 7  | requirements.txt | file for installing dependencies.

### Requirements 
Python 3

MySQL Database (Workbench preferred)


### Instructions
- MySQL database is mandatory. It can be downloaded via:
  
  * https://dev.mysql.com/downloads/workbench/ (Windows)
    
  * https://dev.mysql.com/downloads/mysql/ (Mac) https://dev.mysql.com/downloads/workbench/ (Workbench for Mac)
    
- Create connection within database
  
- Make sure that the connection settings are:

            host="Localhost",
  
            user="root",
  
            password="root",
  
    Otherwise, these details should be altered in createdatabase.py and database.py files.        
  
- Install requirements.txt (or just install mysql-connector-python library).
  
- After pulling the project to device, launch it with launcher.py.
 
- Select 1st option im the launcher.py menu (it has to be done only once).
  
- Restart launcher.py and select the 2nd option for opening game file. There you can create accounts, make deposits/withdrawals for creating data.
  
- Once data is built, restart launcher and select the 3rd option for operating task in MySQL database with generated data.



### Author

Petras Narijauskas
