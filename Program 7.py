# Program 7 : Write a Program to take a number of months and print the number of days in that month.
# Take Input : 4
# Output : April is a 30-day month.


x = int(input("Enter the number : ")) 

if(x==1):
    print("Janauary is a 31-Day Month.")
elif(x==2):
    print("February is a 28-Day Month.")
elif(x==3):
    print("March is a 31-Day Month.")
elif(x==4):
    print("April is a 30-Day Month.")
elif(x==5):
    print("May is a 31-Day Month.")
elif(x==6):
    print("June is a 30-Day Month.")
elif(x==7):
    print("July is a 31-Day Month.")
elif(x==8):
    print("August is a 31-Day Month.")
elif(x==9):
    print("September is a 30-Day Month.")
elif(x==10):
    print("Octomber is a 31-Day Month.")
elif(x==11):
    print("November is a 30-Day Month.")
else:
    print("December is a 31-Day Month.")