# Program 6: Write a Program to check whether the Character is Alphabet or not.
# Take Input: v
# Output: v is an alphabet.



# Input a character from the user
char = input("Enter a character: ")

# Check if the character is an alphabet
if (char >= 'a' and char <= 'z') or (char >= 'A' and char <= 'Z'):
    print(f"{char} is an alphabet.")
else:
    print(f"{char} is not an alphabet.")
