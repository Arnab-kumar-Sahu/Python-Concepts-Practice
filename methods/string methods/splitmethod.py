s='hello Python'
print(s.split())#in rsplit the searching of eliment from left to right execution is same left to right
print(s.split('h'))
print(s.split('h',1))
s1='hello bello'
print(s1.split('l'))
print(s1.split('l',2))

print(s1.rsplit('l',2))#in rsplit the searching of eliment from right to left but execution is  left to right

s3='hello world from python'
print(s3.split())
s4='apple:banana:mango:grape'
print(s4.split(':',3))
s5='one#two#three#four'
print(s5.split('#',1))
s6='path/to/file/document.pdf'
print(s6.split('.',1)[1])
s7='name|age|location#extra'
print(s7.split('#')[0])
s8='2025-04-29 10:30:45,ERROR,Failed to connect to server'
print(s8.split(',')[2])
s9=' spaced out string '
print(s9.split(' '))
print(len(s.split()))
