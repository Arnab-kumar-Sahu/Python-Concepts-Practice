def encryption(s,encrypt=1):
    s1=''
    for i in s:
        s1+=chr(encrypt+ord(i))
    print("encrypted message is:",s1)
def decryption(s,decrypt=1):
    s1=''
    for i in s:
        s1+=chr(ord(i)-decrypt)
    print("decrypted message Is:",s1)
    
s=input("enter ur word:")
shift=int(input("enter shift number"))
want=input("encryption or decryption")
if want.lower()=='encryption':
    encryption(s,shift)
else:
    decryption(s,shift)
    