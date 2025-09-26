Python 3.13.6 (tags/v3.13.6:4e66535, Aug  6 2025, 14:36:00) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
import re
s='haeeep hep hp 123@'
res=re.findall('([a-z})([0-9])')
Traceback (most recent call last):
  File "<pyshell#2>", line 1, in <module>
    res=re.findall('([a-z})([0-9])')
TypeError: findall() missing 1 required positional argument: 'string'
res=re.findall('([a-z})([0-9])',s)
res.groups
Traceback (most recent call last):
  File "<pyshell#4>", line 1, in <module>
    res.groups
AttributeError: 'list' object has no attribute 'groups'
res=re.search('([a-z})([0-9])',s)
res.groups
<built-in method groups of re.Match object at 0x000001FB25B1AA70>
res
<re.Match object; span=(0, 1), match='h'>
res=re.search('([a-z})([0-9]){3}',s)
res
<re.Match object; span=(0, 3), match='hae'>
res.groups
<built-in method groups of re.Match object at 0x000001FB25B1AC20>
res=re.findall('([a-z})([0-9]){3}',s)
res
['e', 'p', 'p', '3']
res=re.findall('([a-z}){3}([0-9])',s)
res
['h', 'a', 'e', 'e', 'e', 'p', 'h', 'e', 'p', 'h', 'p', '1', '2', '3']
res=re.search('([a-z}){3}([0-9])',s)
res.groups
<built-in method groups of re.Match object at 0x000001FB25B1AC20>
res
<re.Match object; span=(0, 1), match='h'>
s
'haeeep hep hp 123@'
res=re.search("(.+)({0-9]+)")
Traceback (most recent call last):
  File "<pyshell#19>", line 1, in <module>
    res=re.search("(.+)({0-9]+)")
TypeError: search() missing 1 required positional argument: 'string'
res=re.search("(.+)({0-9]+)",s)
res
print(res)
None
res=re.search("(.+)({0-9]+)@",s)
res
print(res)
None
res=re.search(".+{0-9]+@",s)
rs
Traceback (most recent call last):
  File "<pyshell#27>", line 1, in <module>
    rs
NameError: name 'rs' is not defined. Did you mean: 're'?
res
s
'haeeep hep hp 123@'
res=re.search("^.+.+[0-9]@$",s)
res
<re.Match object; span=(0, 18), match='haeeep hep hp 123@'>
res=re.search("(^.+)(.+)([0-9]@$)",s)
res.groups
<built-in method groups of re.Match object at 0x000001FB288F8510>
print(res.groups)
<built-in method groups of re.Match object at 0x000001FB288F8510>
len(res.groups)
Traceback (most recent call last):
  File "<pyshell#35>", line 1, in <module>
    len(res.groups)
TypeError: object of type 'builtin_function_or_method' has no len()
for i in res.groups:
    print(i)

Traceback (most recent call last):
  File "<pyshell#38>", line 1, in <module>
    for i in res.groups:
TypeError: 'builtin_function_or_method' object is not iterable
for i in res:
    print(i)

Traceback (most recent call last):
  File "<pyshell#40>", line 1, in <module>
    for i in res:
TypeError: 're.Match' object is not iterable
for i in res.groups():
    print(i)

haeeep hep hp 1
2
3@
res.groups()
('haeeep hep hp 1', '2', '3@')
res=re.search(".+",s)
res
<re.Match object; span=(0, 18), match='haeeep hep hp 123@'>
res=re.findall(r'\bh',s)
res
['h', 'h', 'h']
res=re.findall(r'\Ba',s)
res
['a']
res=re.findall(r'\Ah',s)
res
['h']
res=re.findall(r'\Z@',s)
res
[]
s
'haeeep hep hp 123@'
res=re.findall(r'@\Z',s)
res
['@']
s='+918094545556 +916305356452 +1155675833'
res=re.findall('\+91[7-9][0-9]{9}')
Traceback (most recent call last):
  File "<pyshell#57>", line 1, in <module>
    res=re.findall('\+91[7-9][0-9]{9}')
TypeError: findall() missing 1 required positional argument: 'string'
res=re.findall('\+91[7-9][0-9]{9}',s)
res
['+918094545556']
res=re.findall('\+91[6-9][0-9]{9}',s)
>>> res
['+918094545556', '+916305356452']
>>> res=re.findall(r'p\b',s)
>>> res
[]
>>> s
'+918094545556 +916305356452 +1155675833'
>>> s='haeeep hep hp 123@'
>>> res=re.findall(r'p\b',s)
>>> res
['p', 'p', 'p']
>>> res=re.split(s)
Traceback (most recent call last):
  File "<pyshell#68>", line 1, in <module>
    res=re.split(s)
TypeError: split() missing 1 required positional argument: 'string'
>>> res=re.split('',s)
>>> res
['', 'h', 'a', 'e', 'e', 'e', 'p', ' ', 'h', 'e', 'p', ' ', 'h', 'p', ' ', '1', '2', '3', '@', '']
>>> res=re.split(' ',s)
>>> res
['haeeep', 'hep', 'hp', '123@']
>>> res=re.sub(' ',',',s)
>>> res
'haeeep,hep,hp,123@'
>>> res=re.subn(' ',',',s)
>>> res
('haeeep,hep,hp,123@', 3)
>>> res=re.finditer('he*p',s)
>>> for i in res:
...     print(i)
... 
<re.Match object; span=(7, 10), match='hep'>
<re.Match object; span=(11, 13), match='hp'>
>>> po=compile('he*p')
Traceback (most recent call last):
  File "<pyshell#81>", line 1, in <module>
    po=compile('he*p')
TypeError: compile() missing required argument 'filename' (pos 2)
po=compile('he*p')
Traceback (most recent call last):
  File "<pyshell#82>", line 1, in <module>
    po=compile('he*p')
TypeError: compile() missing required argument 'filename' (pos 2)
po=re.compile('he*p')
res=po.findall(s)
res
['hep', 'hp']
