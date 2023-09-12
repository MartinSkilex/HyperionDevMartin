def print_stringlist(names):
    for name in names:
        for i in name:
            print(i, end = " ")
        print()
    
with open('DOB.txt', 'r+') as f: # Open the file again!
    lines = f.readlines()

names = []
dates = []

for line in lines:
    names.append(line.split()[:2])
    dates.append(line.split()[2:])

print("Names")
print_stringlist(names)
print("\nBirthdate")
print_stringlist(dates)
    