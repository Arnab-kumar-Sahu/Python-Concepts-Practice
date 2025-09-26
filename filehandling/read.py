file=open("python.txt","r")

#number of words in a file
l=file.read().split()
print(l)
print(len(l))
file.seek(0)
#number of lines in a file
lines=file.readlines()
print(lines)
print(len(lines))
file.seek(0)
#number of characters in a file
l=file.read().split()
s="".join(l)
print(s)
print(len(s))
#largest word in a file
file.seek(0)
l=file.read().split()
LW=''
for i in l:
    if len(LW)<len(i):
        LW=i
print(LW)
#longest line in a file
file.seek(0)
l=file.readlines()
LL=''
for i in l:
    if len(LL)<len(i):
        LL=i
print(LL)