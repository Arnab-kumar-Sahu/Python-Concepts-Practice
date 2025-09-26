rows=int(input("Enter number of rows: "))
for i in range(1,rows+1):
    for j in range(1,rows+1):
        if i%2!=0 and j%2!=0 or i%2==0 and j%2==0:
            print(1,end="")
        else:
            print(0,end="")
    print()