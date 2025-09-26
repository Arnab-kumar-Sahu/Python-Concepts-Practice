def sum(n):
    if n==0:
        return 0
    return n+sum(n)
n=int(input())
result=sum(n)
print(result)