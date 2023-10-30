# Program 9: Write a program to check whether the input character is a vowel or Consonant
# Input: 'a'
# Output: vowel
# Input: 'b'
# Output: consonant
'''
X = input("Enter the Character in smallcase : ")

if(X=='a'or X=='e'or X=='i' or X=='o'or X=='u'):
    print("vowel")
else:
    print("consonant")
'''
# Input a character from the user (assuming a single character)
char = input("Enter a character: ")

# Make sure the input is a single character
if len(char) == 1:
    # Check if the character is a vowel (lowercase and uppercase)
    if char in 'aeiouAEIOU':
        print(char," is a vowel.")
    else:
        print(char," is a consonant.")
else:
    print("Invalid input. Please enter a single character.")
