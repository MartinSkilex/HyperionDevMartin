with open("DOB.txt", "r") as file:
    lines = file.readlines()

names = []
birthdates = []

for line in lines:
    parts = line.split(maxsplit=2)
    names.append(parts[0:2])
    birthdates.append(parts[2].strip())

print("Name")
for name in names:
    print(name)

print("\nBirthdate")
for birthdate in birthdates:
    print(birthdate)
