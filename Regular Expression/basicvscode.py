Python 3.13.6 (tags/v3.13.6:4e66535, Aug  6 2025, 14:36:00) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
import re
s='helllo hai python'
re.Match('h',s)
Traceback (most recent call last):
  File "<pyshell#2>", line 1, in <module>
    re.Match('h',s)
TypeError: cannot create 're.Match' instances
re.match('h',s)
<re.Match object; span=(0, 1), match='h'>
list(re.match('h',s))
Traceback (most recent call last):
  File "<pyshell#4>", line 1, in <module>
    list(re.match('h',s))
TypeError: 're.Match' object is not iterable
re.search('h',s)
<re.Match object; span=(0, 1), match='h'>
re.search('l',s)
<re.Match object; span=(2, 3), match='l'>
re.findall('l',s)
['l', 'l', 'l']
re.findall('h',s)
['h', 'h', 'h']
re.findall('.',s)
['h', 'e', 'l', 'l', 'l', 'o', ' ', 'h', 'a', 'i', ' ', 'p', 'y', 't', 'h', 'o', 'n']
re.Match('.',s)
Traceback (most recent call last):
  File "<pyshell#10>", line 1, in <module>
    re.Match('.',s)
TypeError: cannot create 're.Match' instances
re.match('.',s)
<re.Match object; span=(0, 1), match='h'>
re.search('.',s)
<re.Match object; span=(0, 1), match='h'>
re.findall('^h',s)
['h']
re.findall('^a',s)
[]
re.search('^h',s)
<re.Match object; span=(0, 1), match='h'>
print(re.search('^a',s))
None
re.findall('$n',s)
[]
re.search('$n',s)
re.findall('$n',s)
[]
re.match('$n',s)
s
'helllo hai python'
re.findall('^h',s)
['h']
re.findall('$n',s)
[]
re.findall('n$',s)
['n']
re.match('n$',s)
re.search('n$',s)
<re.Match object; span=(16, 17), match='n'>
s='heeep hp heep heap python'
re.findall('he*p)
           
SyntaxError: unterminated string literal (detected at line 1)
re.findall('he*p')
           
Traceback (most recent call last):
  File "<pyshell#29>", line 1, in <module>
    re.findall('he*p')
TypeError: findall() missing 1 required positional argument: 'string'
re.findall('he*p',s)
           
['heeep', 'hp', 'heep']
re.findall('he+p')
           
Traceback (most recent call last):
  File "<pyshell#31>", line 1, in <module>
    re.findall('he+p')
TypeError: findall() missing 1 required positional argument: 'string'
re.findall('he+p',s)
           
['heeep', 'heep']
re.findall('he?p',s)
           
['hp']
re.findall('he{3}p')
           
Traceback (most recent call last):
  File "<pyshell#34>", line 1, in <module>
    re.findall('he{3}p')
TypeError: findall() missing 1 required positional argument: 'string'
re.findall('he{3}p',s)
           
['heeep']
re.findall('he{1,4}p',s)
           
['heeep', 'heep']
re.findall('he{1,3}p',s)
           
['heeep', 'heep']
re.findall('he{1,3}p'|'python',s)
           
Traceback (most recent call last):
  File "<pyshell#38>", line 1, in <module>
    re.findall('he{1,3}p'|'python',s)
TypeError: unsupported operand type(s) for |: 'str' and 'str'
>>> re.findall('he{1,3}p| python',s)
...            
['heeep', 'heep', ' python']
>>> re.findall('hp',s)
...            
['hp']
>>> re.findall('hp',s)
...            
['hp']
>>> re.findall(['ha'],s)
...            
Traceback (most recent call last):
  File "<pyshell#42>", line 1, in <module>
    re.findall(['ha'],s)
  File "C:\Program Files\WindowsApps\PythonSoftwareFoundation.Python.3.13_3.13.1776.0_x64__qbz5n2kfra8p0\Lib\re\__init__.py", line 278, in findall
    return _compile(pattern, flags).findall(string)
  File "C:\Program Files\WindowsApps\PythonSoftwareFoundation.Python.3.13_3.13.1776.0_x64__qbz5n2kfra8p0\Lib\re\__init__.py", line 335, in _compile
    return _cache2[type(pattern), pattern, flags]
TypeError: unhashable type: 'list'
>>> re.findall('[ha]',s)
['h', 'h', 'h', 'h', 'a', 'h']
>>> s
'heeep hp heep heap python'
>>> re.findall('[hap]',s)
['h', 'p', 'h', 'p', 'h', 'p', 'h', 'a', 'p', 'p', 'h']
>>> re.findall('[a-z]{3}'),s)
SyntaxError: unmatched ')'
>>> re.findall('[a-z]{3}',s)
['hee', 'hee', 'hea', 'pyt', 'hon']
>>> S='89bye123589'
>>> re.findall('[4-9][0-9]',S)
['89', '58']
>>> S='89bye123559'
>>> re.findall('[4-9][6-9]',S)
['89', '59']
