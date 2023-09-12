#askingt user to input their name
full_name = input("Please enter your full name: ")

#check if user did not enter anything
if len(full_name) == 0 :
    print("You haven't entered anything. Please enter your full name.")

#check if user entered anything less than 4 characters
elif len(full_name) < 4 :
    print("You have entered less than 4 characters. Please make sure that you have entered your name and surname.")

#check if users enter anything more than 25 characters
elif len(full_name) > 25:
    print('''You have entered more than 25 characters. Please make sure that
you have only entered your full name''')

#user entered the correct name
else:
    print("Thank you for entering your name.")