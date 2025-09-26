n=int(input())
if n>1:
    i=2
    while i<=n//2+1:
        if n%i==0:
            print('it\'s not a prime number')
            break
        i+=1
    else:
        print("it's a prime number")
else:
    print("it's not a prime number")