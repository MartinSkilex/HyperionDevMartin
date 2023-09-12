import math
#asking the user to enter all 3 sides of the triangle

side1 = int(input("Enter the length of first side: "))
side2 = int(input("Enter the length of second side: "))
side3 = int(input("Enter the length of third side: "))

s = (side1+side2+side3)/2
area = math.sqrt(s*(s-side1)*(s-side2)*(s-side3))

print("The area of the triangle is: ", round(area,3))
