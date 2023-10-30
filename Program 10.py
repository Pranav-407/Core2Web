# Program 10: WAP that determines whether a given input year is a leap year or not
'''
x = int(input("Enter Year : "))

if(x%4==0):
    print(x," is a leap year")
else:
    print(x," is not a leap year") 
'''


# Input three angles from the user
angle1 = float(input("Enter the first angle: "))
angle2 = float(input("Enter the second angle: "))
angle3 = float(input("Enter the third angle: "))

# Check if the angles define a right-angled triangle
if angle1 == 90 or angle2 == 90 or angle3 == 90:
    print("The entered angles define a right-angled triangle.")
else:
    print("The entered angles do not define a right-angled triangle.")
