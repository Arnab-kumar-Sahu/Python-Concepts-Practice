l=[12,234,[23,344,76],'fsdf']
l2=l.copy()#it'll only copy outer elements but the inner elements memory remains the same
print(l2)
del l[2][0]
print(l2)
