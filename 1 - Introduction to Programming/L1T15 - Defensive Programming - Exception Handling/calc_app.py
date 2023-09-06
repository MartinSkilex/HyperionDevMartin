# Online Python compiler (interpreter) to run Python online.
# Write Python 3 code in this online editor and run it.
import os.path

#calculator file path
path_to_file = 'equation.txt'
new_line = '\n'

def calc(num1, num2, operation):
    if(operation == '+'):
        ans = num1 + num2
    elif(operation == '-'):
        ans = num1 - num2
    elif(operation == '/'):
        try:
            ans = num1 / num2
        except ZeroDivisionError:
            print("Error: Division by zero is not allowed.")
            return 'Undefined'
        
    elif(operation == '*'):
        ans = num1 * num2
    return ans
        
    
ask_user = ''

while(ask_user != 'A' or ask_user != 'B'):
    ask_user = input("Please enter 'A' to perform a calculation or enter 'B' to print previous calculations: ")
    ask_user = ask_user.upper()
    
    #does the calcutor file exist
    file_exist = os.path.exists(path_to_file)
    
    if(ask_user == 'A'):
        
        #ask the user to enter the first integer
        while True:
            try:
                num1 = int(input("Please enter your first interger: "))
                break
            except ValueError:
                print("Oops! That was not a valid entry. Try again...")
                
        #ask the user to enter the second integer
        while True:
            try:
                num2 = int(input("Please enter your second interger: "))
                break
            except ValueError:
                print("Oops! That was not a valid entry. Try again...")



        #ask the user for the operation
        while True:
            operation = input("Please enter the operation you want to perform (+-/*): ")
            if(operation == '+'):
                break
            elif(operation == '-'):
                break
            elif(operation == '/'):
                break
            elif(operation == '*'):
                break
            else:
                print("Oops! That was not a valid entry. Try again...")        
        
        ans = calc(num1, num2, operation)
        ans_string = f"{num1} {operation} {num2} = {ans}{new_line}"
        print(ans_string)
        
        if(file_exist == True): #save operation to existing file
            f = open(path_to_file, "a")
            f.write(ans_string)
            f.close()
        
        else: #create file
            f = open(path_to_file, "w")
            f.write(ans_string)
            f.close()
        
    elif(ask_user == 'B'):
        if(file_exist == True): #open and read the file after the overwriting:
            f = open(path_to_file, "r")
            print(f.read())
            f.close()
        else:
            print("The file that you are trying to open does not exist")
            
    else:
        print("Oops! That was not a valid entry. Try again...")
        