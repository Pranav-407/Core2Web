# WAP to check numbers are divisible by 4 and 5 between a given range Print those numbers
# Inputl: numl =20
# Output:Numbers divisible by 4 and 5 are 20
# Inputl: numl =15
# Output: Numbers Not divisible by 4 and 5 are

for i in range(2):
    x = int(input("Enter Number : "))
    if(x%4==0 and x%5==0):
        print(x," is divisible by 4 and 5")
    else:
        print(x," is NOT divisible by 4 and 5")
    