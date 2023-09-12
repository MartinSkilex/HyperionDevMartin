#setting the number of rows of stars
rows= 9

#iterating loop over the rows from 0 to 8
for i in range (rows):
    #printing the first 5 rows increasing number of stars by 1 in each row
    if i < 5:
        i += 1
        print("*"*i)
    #printing remaining 4 rows, decreasing number of stars by 1 in each row 
    else:
        i = rows - i
        print("*"*i)