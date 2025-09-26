l=[11,22,100,10,15,23.5]
l.sort()#ascending order
print(l)
l.sort(reverse=True)#descending order
print(l)
l2=[10,20,'hai',97]
#l2.sort() it'll give error cuz same data type allowed only int and float exception
l3=['hai','python','class','Hello','Alpha']
l3.sort() #it'll judge by first charcter of ascii value A=65 go on to Z=90 and a=97 go on to z=122
print(l3)
l3.sort(reverse=True)
print(l3)
print(ord('A'))#ascii values
print(ord('a'))
l4=[(100,484),(4456,),(14,45,667,5555,)]
l4.sort()#consider the first elements of the tuple and then sort
print(l4)
l4.sort(reverse=True)
print(l4)

