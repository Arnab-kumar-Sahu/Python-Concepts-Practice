#in dictionary keys can only be immutable data type
d={'name':'arnab','age':21,'Address':['Bonth','Bhadrak','odisha'],'mobile no':{8889997,9998889},'achievments':{'cricket':1,'football':3}}
print(d['Address'])
d['hobby']='sports'
print(d)
print(d['Address'][1::])
del d['Address']
print(d)
d['age']=20
print(d)
