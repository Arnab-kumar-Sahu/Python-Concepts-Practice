rows=int(input("Enter the number of rows: "))
for i in range(1,rows+1):
    for k in range(1,rows-i+1):
        print(end=" ")
    for j in range(1,rows+1):
        if j==1 or j==i:
            print("*",end=' ')
        else:
            print(' ',end=" ")
    print()
for i in range(rows-1,0,-1):
    for k in range(1, rows-i+1):
        print(end=' ')
    for j in range(1,rows):
        if j==1 or j==i:
            print("*",end=' ')
        else:
            print(' ',end=' ')
    print()




