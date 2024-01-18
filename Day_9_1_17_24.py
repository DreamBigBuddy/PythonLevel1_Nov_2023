# Function
def ageCalc():
    age = int(input("Enter your age: "))
    print("You will be", age + 10, "in 10 years")
    print("You will be", age + 20, "in 20 years")
    
ageCalc(age)

# Function with Parameters
def ageCalc(age):
    print("You will be", age + 10, "in 10 years")
    print("You will be", age + 20, "in 20 years")

age = int(input("Enter your age: "))
ageCalc(age)

# Function with Parameters and Return
def add(x, y):
    return x + y

x = int(input("Enter a number: "))
y = int(input("Enter another number: "))
print(add(x, y))

# Odd or Even Checker
def odd_or_even(num):
    if num % 2 == 0:
        print("Even")

    else:
        print("Odd")

number = int(input("Enter a number: "))
odd_or_even(num=number)

# String Reverser Splicing
def reverse_string(string):
    return string[::-1]

# String Reverser Loop
def reverse_string_loop(string):
    reversed_string = ""

    for i in range(len(string)-1, -1, -1):
        reversed_string += string[i]

    return reversed_string

sentence = input("Enter a string: ")
print(reverse_string_loop(sentence))

# Palindrome Checker
def reverse_string(string):
    return string[::-1]

def palindromeCheck(string):
    if string.lower().replace(" ", "") == reverse_string(string.lower().replace(" ", "")):
        print("It is a palindrome")

    else:
        print("It is not a palindrome")

palindromeCheck("was it a car or a cat I saw")
