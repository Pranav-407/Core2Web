# Program 1: Write a Program to Find a Maximum between two numbers
# Take Input: 1 2
# Output: 2 is Max number between 1 & 2


x = int(input("Enter the First number : "))
y = int(input("Enter the Second number : "))

if (x>y):
    print("In ",x,"&",y,",",x," is greater.")
else:
    print("In ",x,"&",y,",",y," is greater.")