#asking user to enter number of students to be registered
num_students = int(input("How many students are registering:"))

# creating a file using the 'w' access mode
with open('reg_form.txt', 'w') as f:

    #creating a for loop that runs for the number of students
    for stud_num in range(num_students):
        
        #asking user to enter the student id number
        stud_num  = input("Enter the next student num:")

        #writing each student id number to the text file
        f.write(stud_num+"\n")
        f.write("------------------------\n") # dotted line after each student id number 