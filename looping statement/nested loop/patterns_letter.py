rows=int(input("enter the number of rows: "))
for i in range(1,rows+1):
    for j in range(1,i+1):
        print(chr(64+i),end=" ")
    print()
