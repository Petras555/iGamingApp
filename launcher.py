from mysql.connector import Error
import subprocess
def main_menu():
    print("Please select number for following process")
    print("1. Setup (creates database and tables in MySQL)")
    print("2. Launch game menu file")
    print("3. Open tasks")
    print("4. Exit")


def handle_choice(choice):
    if choice == "1":
        try:
            print("Setting up...")
            import createdatabase
            quit()
        except Error as e:
            print(f"The error {e} occurred")
    elif choice == "2":
        print("Launching game menu...")
        subprocess.run('python gamemenu.py', shell=True, check=False)
    elif choice == "3":
        print("Launching tasks...")
        subprocess.run('python task.py', shell=True, check=False)
    elif choice == "4":
        print("Bye...")
        quit()

    else:
        print("Invalid choice. Please select again")


if __name__ == "__main__":
    while True:
        main_menu()
        while True:
            try:
                user_choice = input("Enter your choice: ")
                handle_choice(user_choice)
            except EOFError:
                print('End of file reached unexpectedly.')
