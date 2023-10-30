# WAP program to calculate and print the product of the count of odd numbers within a given range.
# Input: Start: 1 End: 11
# Output: 3125

start = int(input("Enter the starting number: "))
end = int(input("Enter the ending number: "))

count = 0
product = 1

for i in range(start, end):
    if (i%2 != 0):
        count = count + 1

# Calculate the product of the count of odd numbers
for i in range(count):
    product = product * count

print("Product of the count of odd numbers:", product)
