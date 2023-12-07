# Conditionals

# Basic Conditionals
num = 1

if num > 2:
    print("num is greater than 2")

elif num == 2:
    print("num is equal to 2")

else:
    print("num is less than 2")

# Even or Odd
num = int(input("Enter a number: "))

if num % 2 == 0:
    print(num, "is even")

else:
    print(num, "is odd")

# Positive, Negative, or Neutral
num = int(input("Enter a number: "))

if num > 0:
    print(num, "is positive")

elif num < 0:
    print(num, "is negative")

else:
    print(num, "is zero")

# Multiple Finder
max_number = int(input("Enter a number: "))
multiple = int(input("Enter the number to find multiples: "))

for i in range(1, max_number+1):
    if i % multiple == 0:
        print(i)
