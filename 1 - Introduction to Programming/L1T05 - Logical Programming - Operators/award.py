#asking user to input time take to complete different events
swimming = float(input("Enter time taken to complete swimming: "))
cycling = float(input("Enter time taken to complete cycling: "))
running = float(input("Enter time taken to complete running: "))

#calculating and displaying total time taken
triathlon = swimming + cycling + running
print("Total time taken to complete the triathlon: ",str(triathlon))

#determining award based on total time taken
if triathlon <= 100.0:
    award = "Provincial Colours"
elif triathlon > 100.0 and triathlon <=105.0:
    award = "Provincial Half Colours"
elif triathlon > 105.0 and triathlon <=110.0:
    award = "Provincial Scroll"
else:
    award = "No award"

print("You have received ",award)
