# Basic For Loop printing user numbers
num = int(input("Enter a number: "))
for i in range(num):
    print(i)

# Summing up numbers in a range
start = int(input("Enter a start: "))
end = int(input("Enter an end: "))
total = 0

for i in range(start, end+1):
    total += i

print("Your total is", total)

# Drawing square
import turtle

t = turtle.Turtle()

size = int(input("Enter a size: "))

for i in range(4):
    t.forward(size)
    t.right(90)

# Drawing square with halving sides
import turtle

t = turtle.Turtle()

size = int(input("Enter a size: "))

for i in range(4):
    t.forward(size)
    t.right(90)
    size /= 2
