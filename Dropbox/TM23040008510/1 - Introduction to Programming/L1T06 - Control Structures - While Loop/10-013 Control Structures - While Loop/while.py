def get_user_input():
    try:
        return int(input("Please enter a number (-1 to quit): "))
    except ValueError:
        print("Invalid input. Please enter a valid number.")
        return get_user_input()

def main():
    # Initializing variables
    sum = 0
    counter = 0

    # Getting user input using the function
    user_input = get_user_input()

    # Setting up a loop to execute until -1 is entered
    while user_input != -1:
        # Adding the previously entered number to sum
        sum += user_input
        # Incrementing the counter
        counter += 1
        # Asking for the next input from the user
        user_input = get_user_input()

    # Calculating the average if values were entered
    if counter > 0:
        average = sum / counter
        print("The average of the entered values is:", average)
    else:
        print("No value was entered")

if __name__ == "__main__":
    main()


    
