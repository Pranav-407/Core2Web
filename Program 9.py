# WAP to print the count of all negative numbers from a given range
# Input: Start: -15 End: 50
# Output: 15

Start = int(input("Enter the Start : "))
End = int(input("Enter the End : "))

count = 0

for i in range(Start,End):
    if(i<0):
        count+=1
print(count)        