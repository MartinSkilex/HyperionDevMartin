#=====importing libraries===========
'''This is the section where you will import libraries'''
from datetime import datetime
import os
#====Login Section====
'''Here you will write code that will allow a user to login.
    - Your code must read usernames and password from the user.txt file
    - You can use a list or dictionary to store a list of usernames and passwords from the file
    - Use a while loop to validate your user name and password
'''
# Prompts the user to log in
def login():
    user_file_path = "user.txt"
    credentials = read_user_credentials(user_file_path)
    while True:
        #Prompts the user to enter their username and password.
        username = input("Enter your username: ")
        password = input("Enter your password: ")

        if username in credentials and credentials[username] == password:
            print("Login successful. Welcome, {}!".format(username))
            return username
        else:
            print("Invalid username or password. Please try again.")

def add_new_user():
    """
    Add a new user to the user.txt file.
    """
    credentials_file = "user.txt"
    user_credentials = read_user_credentials(credentials_file)

    while True:
        new_username = input("Enter a new username: ").lower()

        if new_username in user_credentials:
            print("Username already exists. Please choose a different username.")
        else:
            new_password = input("Enter a new password: ")
            confirm_password = input("Confirm the password: ")

            if new_password == confirm_password:
                write_user_credentials(credentials_file, new_username, new_password)
                print("New user added successfully!")
                break
            else:
                print("Passwords do not match. Please try again.")

def add_new_task():
    """
    Add a new task to the task.txt file.
    """
    task_file = "tasks.txt"
    assigned_to = input("Enter the username of the person the task is assigned to: ").lower()
    task_title = input("Enter the title of the task: ")
    task_description = input("Enter the description of the task: ")
    due_date = input("Enter the due date of the task (YYYY-MM-DD): ")

    current_date = datetime.now().strftime("%Y-%m-%d")
    task_data = f"\n{assigned_to}, {task_title}, {task_description}, {current_date}, {due_date}, No"

    with open(task_file, "a") as file:
        file.write(task_data)
    print("New task added successfully!")

def view_all_tasks():
    """
    Read and print all tasks from the task.txt file in an easy-to-read format.
    """
    task_file = "tasks.txt"

    with open(task_file, "r") as file:
        for line in file:
            task_data = line.strip().split(", ")
            assigned_to, task_title, task_description, date_assigned, due_date, task_status = task_data
            print(f"Assigned to: {assigned_to}")
            print(f"Title: {task_title}")
            print(f"Description: {task_description}")
            print(f"Date Assigned: {date_assigned}")
            print(f"Due Date: {due_date}")
            print(f"Task Status: {task_status}")
            print("-" * 50)

def view_my_tasks(username):
    """
    Read and print tasks assigned to the currently logged-in user from the task.txt file in an easy-to-read format.
    """
    task_file = "tasks.txt"
    

    with open(task_file, "r") as file:
        for line in file:
            task_data = line.strip().split(", ")
            assigned_to, task_title, task_description, date_assigned, due_date, task_status = task_data
            if assigned_to.lower() == username.lower():
                print(f"Assigned to: {assigned_to}")
                print(f"Title: {task_title}")
                print(f"Description: {task_description}")
                print(f"Date Assigned: {date_assigned}")
                print(f"Due Date: {due_date}")
                print(f"Task Status: {task_status}")
                print("-" * 50)

def read_user_credentials(file_path):
    """
    Read the list of valid usernames and passwords from a text file.
    Each line of the file should contain a username and password separated by a space.
    Returns a dictionary where keys are usernames and values are passwords.
    """
    credentials = {}
    with open(file_path, "r") as file:
        for line in file:
            # Handling incorrect formatting by skipping lines without both username and password
            try:
                username, password = line.strip().split(", ")
                credentials[username] = password
            except ValueError:
                continue
    return credentials

def write_user_credentials(file_path, username, password):
    """
    Write the new username and password to the text file.
    """
    with open(file_path, "a") as file:
        file.write(f"\n{username}, {password}")

def is_admin_user(username):
    """
    Check if the given username is 'admin'.
    """
    return username.lower() == 'admin'


def display_statistics():
    """
    Display statistics including the total number of tasks and users in a user-friendly manner.
    """
    user_file = "user.txt"
    task_file = "tasks.txt"

    total_users = sum(1 for _ in open(user_file))
    total_tasks = sum(1 for _ in open(task_file))

    print(f"Total number of users: {total_users}")
    print(f"Total number of tasks: {total_tasks}")
# Clears the console screen
def clear_screen():
    """
    Clears the console screen.
    """
   
    os.system("cls" if os.name == "nt" else "clear")



def main():
    # Clear the console screen to improve readability
    clear_screen()

    # Define the path to the user.txt file
    user_file_path = "user.txt"

    # Prompt the user to log in and retrieve the logged-in username
    username = login()

    # If the logged-in user is the admin, display a special message
    if username == "admin":
        print("You are logged in as the admin user.")

    while True:
        # Display the main menu options
        print("\nMenu:")
        print("a - Add a task")
        print("va - View all tasks")
        print("vm - View my tasks")
        print("r - Register a user")
        print("ds - Display statistics")
        print("e - Exit")

        # Prompt the user to enter their choice and convert it to lowercase
        menu = input("Enter your choice: ").lower()

        if menu == "a":
            # Add a new task if the user chose 'a'
            add_new_task()

        elif menu == "va":
            # View all tasks if the user chose 'va'
            view_all_tasks()

        elif menu == "vm":
            # View tasks assigned to the current user if the user chose 'vm'
            view_my_tasks(username)

        elif menu == "r" and username == "admin":
            # If the user is the admin, allow user registration
            new_username = input("Enter a new username: ")
            new_password = input("Enter a new password: ")
            confirm_password = input("Confirm the password: ")

            if new_password == confirm_password:
                # Register the new user if the passwords match
                write_user_credentials(user_file_path, new_username, new_password)
                print("User registered successfully!")
            else:
                # Show an error message if the passwords do not match
                print("Passwords do not match. User registration failed.")

        elif menu == "ds" and username == "admin":
            # If the user is the admin, display statistics
            display_statistics()

        elif menu == "e":
            # Exit the program if the user chose 'e'
            print("Exiting the program. Goodbye!")
            break

        else:
            # Show an error message for an invalid choice
            print("Invalid choice. Please try again.")


# Start the Program
if __name__ == "__main__":
    main()