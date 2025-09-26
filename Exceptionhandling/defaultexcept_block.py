print("pogram starts")
try:
    a=int(input())
    b=int(input())
    res=a/b
except :
    print("we can't specify which error it is")
else:
    print(res)
finally:
    print([1])