def add(**kwargs):
    print(kwargs)
    summ=0
    for i in kwargs.values():
        summ+=i
    print('sum is:',summ)
add(a=1,b=2,c=3)
add()
