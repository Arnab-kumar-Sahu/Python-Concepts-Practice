coloumns=int(input("Enter the number of coloumns: "))
for i in range(1,4):
    for k in range(1,3-i+1):
        print(" ", end="")
    for j in range(1,coloumns+1):
        if i==2 or j%2!=0:
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print()
               # OR
coloumns = int(input("Enter the number of columns: "))
for i in range(1, 4):
    for j in range(1, coloumns + 1):
        if (i + j) % 4 == 0 or (i == 2 and j % 4 == 0):
            print("*", end="")
        else:
            print(" ", end="")
    print()
