s='hai\npython'
print(s)
d={i:s[i] for i in range(len(s))}
print(d)
d={i:j for i,j in enumerate(s)}
print(d)
l=[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15]
d={i:j for i,j in zip(l,s)}
print(d)
d={i:j for i,j in zip(s,l)}
print(d)
from itertools import zip_longest
d={i:j for i,j in zip_longest(l,s)}
print(d)

