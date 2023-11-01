# User Input and Printing
name = input("Enter your name: ")
print("Hello " + name)

age = int(input("Enter your age: "))
print("You are " + str(age))

# User Info Exercise
first_name = input("What is your first name:")

last_name = input("what is your last name:")

birthday_month = int(input("What month were you born:"))

birthday_day = int(input("What day were you born:"))

birthday_year = int(input("what year were you born:"))

print("Hello", first_name, last_name, ". You were born in", str(birthday_month) + "/" + str(birthday_day) + "/" + str(birthday_year))

# Using type function to get data type
name = input("Enter your name: ")
print(type(name))

age = int(input("Enter your age: "))
print(type(age))

# Copying a string using multiplication
print("a" * 5)
