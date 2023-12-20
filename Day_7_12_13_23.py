num = -10

if num == 1:
    print("num is equal to 1")

elif num > 1:
    print("num is larger than 1")

else:
    print("num is smaller than 1")

# AND Example
num = 5
string = "e"
if num > 4 and string == "f":
    print("num is above 4 and string is f")
    
else:
    print("Either num is less than 4 and/or string is not f")

# OR Example
num = 10
if num > 5 or num < 0:
    print("num is greater than 5 or less than 0")

# Number Bounds
num = 7
if num >= 0 and num <= 5:
    print("num is between 0 and 5")

elif num > 5 and num <= 10:
    print("num is between 5 and 10")

else:
    print("num is greater than 10")

# Difference Between 21
n = int(input("Enter a number: "))
if n <= 21:
    print(21 - n)

else:
    print((n - 21) * 2)
