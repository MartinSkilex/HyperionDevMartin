with open("DOB.txt", "r") as file:
    lines = file.readlines()
    
# Split the lines into names and birthdates
names = []
birthdates = []

for line in lines:
    parts = line.rsplit(maxsplit=3)
    names.append(parts[0])

# Print the names section
print("Name")
for name in names:
    print(name)

for line in lines:
    parts = line.split(maxsplit=2)
    birthdates.append(parts[2].strip()) 


# Print the birthdates section
print("\nBirthdate")
for birthdate in birthdates:
        print(birthdate,)
