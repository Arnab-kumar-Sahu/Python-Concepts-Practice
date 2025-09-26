l=[5, 15, 35, 'hai', 75, [20, 50, 'shriram'], 'shaktiman']
l.pop()#default index value is -1
print(l)
l.pop(3)
print(l)
l.pop(0)
print(l)
l.pop(100)#it'll give error cuz the index pos is more than the length of the list
print(l)
