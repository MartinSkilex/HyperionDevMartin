#initailising variables
sum  = 0
counter = 0

#geting user input as an integer
user_input = int(input("Please enter a number(-1 to quit): "))

# setting loop to execute until -1 is entered
while user_input != -1:

    #adding previously entered number to sum
    sum += user_input
    #increament counter
    counter += 1
    #asking for second input from user
    user_input = int(input("Please enter a number(-1 to quit): "))

  
#calculating the average  
if user_input == -1:
        
    average = sum/counter
    print("The average of the entered values is: ",average)
else:
    print("No value was entered")
    

    
