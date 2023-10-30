# WAP to prints numbers which are divisible by 3 and 5 both in a given range.
# Input: Start: 15 End: 50
# Output: 15 30 45


Start = int(input("Enter the Start : "))
End = int(input("Enter the End : "))

for i in range(Start,End):
    if(i%3==0 and i%5==0):
        print(i, end=" ")