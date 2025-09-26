l=[10,200.59,['son goku','vegeta',[300,'monkey','hanuman']],[['java',5+8j,False],'ashok'],'arnab sahu']
print(len(l))
print(id(l[4]))
print(type(l[3]))
print(type(l[3][0][2]))
print(type(l[3][0][1]))
print(l[2][2][1][:4:3])
print(l[3][1][::])
print(l[2][0][-3:-5:-1])
print(l[2][2][2])

print(l[::-1])
l[3][0][0]='python'
print(l)
l[2][2][1]='monkey D luffy'
print(l)
l[2][2][::]=['sun wukong']
print(l)
l[2][2]='sun wukong'
print(l)
l[2]=['ravan','ram','sita','laxman']
print(l)
l[:-3:-1]=['arjun','karna']
print(l)
l[:2:1]=['luv','kush']
print(l)
l[::]='ramayan'
print(l)
l[::2]=['ram','mata','yash','nandini']
print(l)
l[1::2]=['arnab','ankita','arpita']
print(l)
l[::]='mahabharat'
print(l)
l[:4:1]=['india']
print(l)
l[1::1]=['bharat']
print(l)
l[::-1]=['vishnu','balram']
print(l)
l[::]=['hanuman']
print(l)


#del l[2][0]
#print(l)
#del l[::]
#print(l)
