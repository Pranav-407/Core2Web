# Program 2: Write a Program to check whether the number is Negative, Positive or equal to Zero.
# Take Input: -2
# Output: -2 is the negative number

x = int(input("Enter the number : "))

if(x==0):
    print(x, "is equal to zero.")
elif(x>0):
    print(x, "is Positive number.")
else:
    print(x, "is Negative Number" )