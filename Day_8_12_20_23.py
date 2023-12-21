factor = int(input("Enter a number: "))
maximum = int(input("Enter a max number: "))

multiples = []

for i in range(1, maximum+1):
    if i % factor == 0:
        multiples.append(i)

print(multiples)
