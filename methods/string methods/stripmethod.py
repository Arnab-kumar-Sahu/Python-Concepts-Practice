s='     hai what are u doing     '
print(s.strip())#default value for strip is space
s1='.........     hai this is goku      '
print(s1.strip('.').strip(' '))
print(s.rstrip())#only strip the right end
print(s.lstrip())#only strip the left end
print('##@@hello@@##1'.strip('#@1'))# u can also do like this for removing multiple elements

