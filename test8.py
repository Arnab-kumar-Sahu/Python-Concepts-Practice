terms=int(input("Enter number of terms: "))
n1,n2=0,1
if terms<=0:
    print("Enter a positive integer")
elif terms==1:
    print(f'{n1}')
else:
    for i in range(terms):
        print(n1,end=" ")
        n=n1+n2
        n1=n2
        n2=n





