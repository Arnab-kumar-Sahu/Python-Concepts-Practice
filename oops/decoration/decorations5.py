def isprime(n):
    if n>1:
        for i in range(2,n//2+1):
            if n%i==0:
                return False
        else:
            return True
    else:
        return True

def decorators(func):
    def inner():
        from time import time
        ST=time()
        func()
        ET=time()
        print('Time elapsed: ',ET-ST)
    return inner
@decorators
def primenumbers():
    ll=int(input("enter lower limit: "))
    ul=int(input("enter upper limit: "))
    for i in range (ll,ul+1):
        if isprime(i):
            print(i,end=' ')
    print()
primenumbers()
@decorators
def fibo():
    a=int(input("Enter a number: "))
    b=int(input("Enter another number: "))
    n=int(input("range of fibonacci series: "))
    if n==1:
        print(a)
    elif n==2:
        print(a,b)
    else:
        print(a,b, end=' ')
        for i in range(n-2):
            c=a+b
            print(c,end=' ')
            a,b=b,c
        print()
fibo()