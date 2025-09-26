from math import comb

rows = int(input("Enter number of rows: "))

for i in range(rows):
    # Print spaces for alignment
    print(' ' * (rows - i), end='')

    # Print values using combinations
    for j in range(i + 1):
        print(comb(i, j), end=' ')

    print()  # Newline
