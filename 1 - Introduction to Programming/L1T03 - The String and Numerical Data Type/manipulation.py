#*asking user to enter sentence and store it as str_manip
str_manip = input("PLease enter a sentence: ")

#calculating and displaying the length of str_manip
print(len(str_manip))

#finding last letter in str_manip. Replace every occurrence of this letter in str_manip with ‘@’.
char1 = str_manip[-1]
new_str_manip = str_manip.replace(char1,'@')
print(new_str_manip) 

#printing the last 3 characters in str_manip backwards
print(str_manip[-1:-4:-1])

#Creating a five-letter word that is made up of the first three characters and the last two characters in str_manip
new_word = str_manip[:3] + str_manip[-2:]
print(new_word)