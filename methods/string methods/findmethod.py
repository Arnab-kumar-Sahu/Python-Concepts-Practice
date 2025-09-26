#find() is same as index but if the value is not present it doesn't give u value error like index
s='hai python'
print(s.find('h'))
print(s.find('h',2))
print(s.find('h',2,8))
print(s.find('p'))
print(s.find('y'))
print(s.rfind('h',0,7))#in rfind slicing left to right but searching element right to left
print(s.rfind('h',0,8))
print(s.find('py'))

#the below code doesn't give u error it'll return -1 as int value
print(s.rfind('yp'))
print(s.find('w'))
