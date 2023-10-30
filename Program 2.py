# Write a Program to print all Even numbers from a given range.
# Input : Start = 10; End = 20;
# Output: 10 12 14 16 18

Start = 10
End = 20

for i in range(10,20):
    if(i%2==0):
        print(i,end=" ")