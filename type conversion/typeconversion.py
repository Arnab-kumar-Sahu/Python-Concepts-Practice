#int type conversion
print(int(23.7))
print(int(True))
print(int(False))
print(int('23'))
#int conversion only happens when the data type is float,boolean or string containing only interger 

#float type conversion
print(float(24))
print(float(True))
print(float(False))
print(float('56'))
print(float('90.5'))
#float conversion only happens when the data type is int,boolean or string containing interger and float

#complex type conversion
print(complex(23))
print(complex(23.5))
print(complex(True))
print(complex(False))
print(complex('23'))
print(complex('23.4'))
print(complex('23+5j'))
#complex conversion only happens when the data type is float,boolean or string containing  interger,float and complex

#Boolean type conversion
print(bool(0))              
print(bool())
print(bool(0j))
print(bool(0.0))              
print(bool([]))
print(bool(()))
print(bool(''))
print(bool({}))
print(bool(set()))
print(bool(23))
print(bool(67.5+9j))
print(bool('ydydy'))
print(bool([45])) 
print(bool((34,)))
print(bool({23,454,66}))
print(bool({34:45}))
#boolean conversion happens in all the data types But if the value is 0,0.0,0j or empty collection data type then the output is zero

#string type conversion
print(str(23))
print(str(23.4))
print(str(23.4+8j))
print(str(True))
print(str(['arnab']))
print(str((23,)))
print(str({23,45,65,56}))
print(str({'name':'arnab','age':21}))
#string converts all the data types

#list type conversion
print(list('arpita'))
print(list(('arpita',65)))
print(list({'arpita',23,56,(90,98)}))
print(list({'name':'arpita','age':21}))
#list converts only the collection data types but dictionary only gives it's keys values

#tuple type conversion
print(tuple('ankita'))
print(tuple(['ankita',65]))
print(tuple({'ankita',23,56,(90,98)}))
print(tuple({'name':'ankita','age':21}))
#tuple also converts only the collection data types and dictionary only gives it's keys values

#set type conversion
print(set('bharati'))
print(set(('bharati',65)))
print({'bharati', 23, 56, (90, 98)})
print(set({'name': 'bharati', 'age': 21}))
#set also converts only the collection data types and dictionary only gives it's keys values but in random order

#dictionary type conversion
#in dictionary u can type convert (list,tuple,set) but the values in between them should be in pairs and in set value pairs should be tuple coz it's stores only immutable data types
print(dict({('bharati',23),(56,(90,98))}))
print(dict([{'arnab','smruti'},('age',21),['age',19]]))

print(dict([('arnab',54)]))
print(dict((['arnab',54],)))

