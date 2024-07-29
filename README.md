# Introduction
- Add your project logo.
- Write a short introduction to the project.
- If you are using badges, add them here.

## Index

- [About](#about)
- [File Structure](#file-structure)
- [Requirements](#Requirements)
- [Instructions](#Instructions)
- [Author](#Author)


## About
Simple iGaming "application" which connects to MySQL database where user can create accounts and make transactions with them to virtual wallet. Database holds information about every account(userID, username, password) and every transaction that was made with each account(transaction ID, username, amount, transaction type:deposit or withdrawal and date). The project allows to build data within database which could be used for following tasks:

*List all users having 3 deposits or more

*List all users having only 1 withdrawal

*List 3 users that have made the highest deposits

*List all deposits for users. Display UserId, UserName, DepositDate, DepositAmount

*Calculate balances of all users


### File Structure


| No | File Name | Details 
|----|------------|-------|
| 1  | launcher.py      | a file which should be firstly used by user to navigate through project.
| 1  | createdatabase.py| file creates database and mandatory tables within database (1st selection within launcher.py).
| 1  | database.py      | has functions for connecting to database, which are used in other scripts.
| 1  | gamemenu.py      | game file for creating accounts, doing deposits and withdrawals, and checking list of all accounts within database(2nd selection within launcher.py).
| 1  | task.py          | file for operatings tasks from [About](#about) section. (3rd selection within launcher.py).
| 1  | classes.py       | separate file for classes, currently contains single class for user.
| 1  | requirements.txt | file for installing dependencies.

### Requirements 
Python 3

MySQL Database (Workbench preferred)


### Instructions
- MySQL database is mandatory. It can be downloaded via:
  
  * https://dev.mysql.com/downloads/workbench/ (Windows)
    
  * https://dev.mysql.com/downloads/mysql/ (Mac) https://dev.mysql.com/downloads/workbench/ (Workbench for Mac)
    
- Create connection within database
  
- Install requirements.txt (or just install mysql-connector-python library)
  
- After pulling project to device, launch it with launcher.py
 
- Select 1st option of launcher.py menu (it has to be done only once)
  
- Restart launcher.py and select 2 option for opening game file, there you can create accounts, make deposits/withdrawals for creating data
  
- Once data is built, restart launcher and select 3 options for operating task in MySQL database with generated data.



### Author

Petras Narijauskas
