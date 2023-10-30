'''
WAP to print all the character values of the given ASCII value range from the user
Input :
    Enter the start of range : 1
    Enter end of range: -2
Output :
    Wrong input
Input :
    Enter start of range : 65
    Enter end of range : 67
Output :
    The character of ASCII value 65 is A.
    The character of ASCII value 66 is B.
    The character of ASCII value 67 is C.
'''

print("For UPPERCASE Character Enter the range from 65 to 90.")
print("For LOWERCASE Character Enter the range from 97 to 122.")

x = int(input("Enter the Start : "))
y = int(input("Enter the End : "))

# For uppercase :
if(x in range(65,91) and y in range(65,91)):
    for i in range(x,y+1):
        print("The character of ASCII value",i," is ",(chr(i)))

# For Lowercase :
elif(x in range(97,123) and y in range(97,123)):
    for i in range(x,y+1):
        print("The character of ASCII value",i," is ",(chr(i)))

else:        
    print("Wrong Input")
