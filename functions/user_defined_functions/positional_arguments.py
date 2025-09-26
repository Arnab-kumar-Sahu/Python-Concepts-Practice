def add(a,b):
    print(a+b)
add(10,20)
add(45,75)
# for only postional arguments
def summ(a,b,/):
    print(a+b)
summ(40,25)
summ(50,60)