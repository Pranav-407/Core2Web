# Program 5: Write a Program to take an integer ranging from 0 to 6 and print corresponding weekday (week starting from Monday)
# Take Input: 2
# Output: Wednesday.

x = int(input("Enter the number From 0 to 6 : "))

if(x==0):
    print("Monday.")
elif(x==1):
    print("Tuesday.")
elif(x==2):
    print("Wednesday.")
elif(x==3):
    print("Thursday.")
elif(x==4):
    print("Fridayday.")
elif(x==5):
    print("Saturday.")
else:
    print("Sunday.")