# WAP to print all the ASCII values from a given character range.
# Input : Enter the start of range : A
#         Enter end of range: Z
# Output : ASCII value of A is 65
#         ASCII value of B is 66
#         ASCII value of C is 67


print("For UPPERCASE Character Enter the range from A to Z.")
print("For LOWERCASE Character Enter the range from a to z.")

start = input("Enter The Start :")
end = input("Enter The End :")

start_ascii = ord(start)
end_ascii = ord(end)

# For uppercase :
if(start_ascii in range(65,91) and end_ascii in range(65,91)):
    for i in range(start_ascii,end_ascii+1):
        print("The character of ASCII value",i," is ",(chr(i)))

# For Lowercase :
elif(start_ascii in range(97,123) and end_ascii in range(97,123)):
    for i in range(start_ascii,end_ascii+1):
        print("The character of ASCII value",i," is ",(chr(i)))

else:        
    print("Wrong Input")
