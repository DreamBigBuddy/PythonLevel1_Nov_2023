# Replace Function
def replace(string, replace_str, new_str):
    while replace_str in string:
        loc = string.find(replace_str)
        string = string[:loc] + new_str + string[loc+len(replace_str):]

    return string

string = input("Enter a phrase: ")
replace_str = input("Enter the phrases to be replaced: ")
new_str = input("Enter the phrases to replace the others: ")
print(replace(string, replace_str, new_str))

# TypeError Example
x = 1
a = "a"

try:
    print(x + a)

except:
    print("An error has occurred. It was due to an invalid type")

# IndexError Example
my_list = [1, 2, 3, 4, 5]

try:
    index = int(input("Enter an index: "))

    print(my_list[index])

except:
    print("Please input a value lower than the length of the list")
    print("The list is", len(my_list), "items long")

# Shape Drawer
import turtle, random

def random_position(t):
    t.penup()
    t.goto(random.randint(-400, 400), random.randint(-400, 400))
    t.pendown()

def draw_square(size):
    for i in range(4):
        t.forward(size)
        t.right(90)

t = turtle.Turtle()

choice = ""

while choice != "quit":
    choice = input("Enter a shape: ")
    size = int(input("Enter a size: "))

    if choice == "square":
        random_position(t)
        draw_square(size)

    elif choice == "circle":
        random_position(t)
        t.circle(size)
