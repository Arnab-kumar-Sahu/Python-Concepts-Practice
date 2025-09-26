l=[i for i in range(1,11)]
print(l)
l=[i for i in range(1,11) if i%2==0]
print(l)
l=[i for i in range(1,11) if i%2==0 and i>5]
print(l)
L=[1 if i%2==0 else 0 for i in range(1,11)]
print(L)
# if if-else conditon is there then if-else comes first in other cases for loop first