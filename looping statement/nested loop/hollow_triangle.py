rows=int(input("Enter number of rows: "))
for i in range(1,rows+1):
    for k in range(1,rows-i+1):
        print(end=" ")
    for j in range(1,i+1):
        if i== rows or j==1 or j==i:
            print("*",end=" ")
        else:
            print(' ' ,end=" ")
    print()