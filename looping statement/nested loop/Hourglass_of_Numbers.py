rows=int(input("Enter the number of rows: "))
for i in range(rows,0,-1):
    for j in range (1,rows-i+1):
        print(end=' ')
    for k in range(1,i+1):
        print(k,end="")
    for w in range(i-1,0,-1):
        print(w,end="")
    print()
for i in range(1,rows):
    for j in range(1,rows-i):
        print(end=' ')
    for k in range(1,i+2):
        print(k,end="")
    for w in range(i,0,-1):
        print(w,end="")
    print()