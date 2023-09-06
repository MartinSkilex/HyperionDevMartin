# Logical Error:  Incorrect sum,difference and division calculation

# Asking the user to enter three different integers
num1 = int(input("Enter the first integer: "))
num2 = int(input("Enter the second integer: "))
num3 = int(input("Enter the third integer: "))

# Calculating and printing the required values
sum = num1 + num2 - num3
print("The sum of all the numbers:", sum)

difference = num1 + num2
print("The first number minus the second number:",difference)

division = sum*num3
print("Sum of all three numbers divided by third number:",division)
    