# This example program is meant to demonstrate errors.
 
# There are some errors in this program. Run the program, look at the error messages, and find and fix the errors.

print ("Welcome to the error program") #SyntaxError:missing brackets on print(...)
print ("\n") #Compilation error; incorrect space indentation, need to be inline with print above and #SyntaxError:missing brackets on print(...)

# Variables declaring the user's age, casting the str to an int, and printing the result
age_Str = "24 years old" #SyntaxError: space indent & Logical error: age_Str declared incorrectly with double == instead of 1 =
age = int(''.join(filter(str.isdigit, age_Str))) #Runtime error: using filter to extract digits from string and ''.join to join the string characters then int to cast string character to an integer
print("I'm ", age, "years old") # Syntax error; fullMessage does not have appropriate spacing requiring: + " " + & repetition of "years old"

# Variables declaring additional years and printing the total years of age
years_from_now = 3 #IndentationError: unexpected indent
total_years = age + years_from_now ##Compilation error; incorrect space indentation, need to be inline with years_from_now

print ("The total number of years:" ,total_years) #SyntaxError:missing brackets on print(...) & Logical error: outputing a string instead of total number of years

# Variable to calculate the total amount of months from the total amount of years and printing the result
total_months = total_years * 12 #Syntax Error: wrong naming of variable total years as total
print ("In 3 years and 6 months, I'll be " + str(total_months+6) + " months old") #SyntaxError: Missing parentheses in call to 'print' ... missing brackets on print(...) and logical error: answer was wrong because the 6 month was not added

#HINT, 330 months is the correct answer

