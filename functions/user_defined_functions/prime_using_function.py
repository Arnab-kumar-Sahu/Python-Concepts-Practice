def isprime(n):
    if n>1:
        for i in range(2, n // 2 + 1):
            if n % i == 0:
                return False
        else:
            return True
    else:
        return False

def prime_numbers(LL,UL):
    for i in range(LL,UL):
        if isprime(i):
            print(i)

prime_numbers(1,101)
