print("pogram starts")
try:
    a=int(input())
    b=int(input())
    res=a/b
except ZeroDivisionError as ze:
    print(ze)
else:
    print(res)
finally:
    print([1])
