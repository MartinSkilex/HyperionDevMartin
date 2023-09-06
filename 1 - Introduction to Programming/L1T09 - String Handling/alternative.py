old_str = "Hello World"
array = ['', '']
new_str = ''

# Make each alternative character into an upper case

# Extract each individual character
for i in range(len(old_str)):
    if i % 2 == 0: # if i is even convert to uppercase
        str = old_str[i].upper()
    else: # if i is odd convert to lowercase
        str = old_str[i].lower()
    
    # Making the array list to join
    array[0] = new_str
    array[1] = str
    new_str = "".join(array)
#print(old_str)
print(new_str)

# Make each alternative word into an upper case
new_str = ''
array1 = ['', '']
array = old_str.split(" ")
for i in range (len(array)):
    if i % 2 == 0:
      str = array[i].upper()
    else:
       str = array[i].lower()

    array1[0] = new_str
    array1[1] = str
    if(i == 0):
        new_str = "".join(array1)
    else:
        new_str = " ".join(array1)

print(new_str)