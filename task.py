from database import db_query, connection


def users_with_3_deposits():
    function = "SELECT username FROM Transactions WHERE TransactionType = 'Deposit' GROUP BY username HAVING COUNT(TransactionID) >= 3 "
    for x in db_query(connection, function):
        print(x)


def user_with_1_withdrawal():
    function = "SELECT username FROM Transactions WHERE TransactionType = 'Withdrawal' GROUP BY username HAVING COUNT(TransactionID) = 1 "
    for x in db_query(connection, function):
        print(x)


def top3_deposited_users():
    function = "SELECT username, DepositAmount FROM Transactions WHERE TransactionType = 'Deposit' ORDER BY DepositAmount DESC LIMIT 3 "
    for x in db_query(connection, function):
        print(x)


def list_all_deposits():
    function = "SELECT Clients.ClientID, Clients.Username, Transactions.DepositDate, Transactions.DepositAmount FROM Clients JOIN Transactions ON Clients.Username = Transactions.Username WHERE TransactionType = 'Deposit' "
    for x in db_query(connection, function):
        print(x)


def calculate_balance():
    function = "SELECT Clients.Username, SUM(Transactions.DepositAmount) AS TotalDeposits FROM Clients INNER JOIN Transactions ON Clients.Username = Transactions.Username GROUP BY Username ORDER BY TotalDeposits DESC "
    for x in db_query(connection, function):
        print(x)


def main_menu():
    print("Please select number for following process")
    print("1. List all users having 3 deposits or more")
    print("2. List all users having only 1 withdrawal")
    print("3. List 3 users that have made the highest deposits")
    print("4. List all deposits for users. Display UserId, UserName, DepositDate, DepositAmount")
    print("5. Calculate balances of all users")
    print("6. Exit the program")


def handle_choice(choice):
    if choice == "1":
        print("Task number 1")
        users_with_3_deposits()
    elif choice == "2":
        print("Task number 2")
        user_with_1_withdrawal()
    elif choice == "3":
        print("Task number 3")
        top3_deposited_users()
    elif choice == "4":
        print("Task number 4")
        list_all_deposits()
    elif choice == "5":
        print("Task number 5")
        calculate_balance()
    elif choice == "6":
        print("Exiting the program.")
        quit()

    else:
        print("Invalid choice. Please select again.")


if __name__ == "__main__":
    while True:
        main_menu()
        user_choice = input("Enter your choice: ")
        handle_choice(user_choice)
