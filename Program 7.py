# WAP that prints all Positive numbers from a given range.
# Input: Start: -7 End: 8
# Output: 1 2 3 4 5 6 7


Start = int(input("Enter the Start : "))
End = int(input("Enter the End : "))

for i in range(Start,End):
    if(i>0):
        print(i, end=" ")