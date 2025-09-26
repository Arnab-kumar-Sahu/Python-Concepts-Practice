import copy
l=[56,48,67,[434,'hai','python',79],76.5,'arnab']
l2=copy.deepcopy(l)#it'll copy both outer and inner elements and memory address will be different
print(l2)

del l[3][2]
print(l2) #it'll remain same cuz the memory address for outer and inner element is different

print(id(l[5]))
print(id(l2[5]))

del l[5]
print(l2)
