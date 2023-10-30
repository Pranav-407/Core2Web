# WAP to determine whether entered angles define a right-angled triangle.
# Take three values of angle from the user
# Inputl: angle1 = 90
# Input2: angle2 = 90
# Input3: angle3 = 90
# Output: It is NOT a right-angle triangle
# Inputl: angell = 90
# Input2: angle2 = 60
# Input3: angle3 = 30
# Output: It is a right-angle triangle

angle1=int(input("Enter Angle 1 :"))
angle2=int(input("Enter Angle 2 :"))
angle3=int(input("Enter Angle 3 :"))

if((angle1==90 or angle2==90 or angle3==90) and angle1+angle2+angle3==180):
    print("It is a Right Angled Triangle")
else:    
    print("It is a NOT Right Angled Triangle")
