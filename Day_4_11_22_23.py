for i in range(5):
    print(i)

print()

i = 0
while i < 5:
    print(i)
    i += 1

user_input = input("Enter something: ")
while user_input != "stop":
    print(user_input)
    user_input = input("Enter something: ")

num = int(input("Enter a number: "))
total = 0
while num != -1:
    total += num
    num = int(input("Enter a number: "))

print(total)
