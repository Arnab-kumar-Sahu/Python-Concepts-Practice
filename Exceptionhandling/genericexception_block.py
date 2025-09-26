from logging import exception

print("pogram starts")
try:
    a=int(input())
    b=int(input())
    res=a/b
except Exception as e:
    print(e)
else:
    print(res)
finally:
    print([1])