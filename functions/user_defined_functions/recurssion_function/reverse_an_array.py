def func(l,left,right):
    if left>=right:
        return l
    l[left],l[right]=l[right],l[left]
    return func(l,left+1,right-1)
print(func([1,2,3,8,5,4,9],2,5))