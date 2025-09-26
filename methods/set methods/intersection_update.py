s={32,44,55,78,96,24}
s1={32,10,49,44}
s2={96,40,70,44}
#it perform same operation as intersection but it'll update that to the baseset
s.intersection_update(s1)
print(s)
s.intersection_update(s2)
print(s)
s.intersection_update(s1,s2)
print(s)

