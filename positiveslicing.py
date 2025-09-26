s='arnab kumar sahu'
print(len(s))
print(s[0:16:1])
print(s[ : : ])
print(s[3:16:2])
print(s[-15:-2:3])
print(s[-16:16:15])
print(s[-16:-1:15])#it'll give empty space
print(s[-16:0:15])
#it'll not give u error even if u give incorrect index
print(s[9:20:8])
print(s[0:16:16])
print(s[0:16:15])
print(s[5:5])#it'll give empty space

print(s[-1:-17:-1])    
print(s[15:0:-1])
print(s[15:-1:-1])#it'll give empty space
#if the updation is zero it'll give error
print(s[15:-1:0])
