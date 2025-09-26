rows = int(input("Enter an odd number of rows: "))

for i in range(1, rows + 1, 2):
    for space in range((rows - i) // 2):
        print(" ", end="")
    for star in range(i):
        print("*", end="")
    print()

for i in range(rows - 2, 0, -2):
    for space in range((rows - i) // 2):
        print(" ", end="")
    for star in range(i):
        print("*", end="")
    print()



