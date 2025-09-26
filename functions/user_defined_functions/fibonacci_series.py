def fibonacci_series(terms):
    n1,n2=0,1
    for i in range(1,terms+1):
        print(n1,end=' ')
        n=n1+n2
        n1=n2
        n2=n
fibonacci_series(20)

    

        

    