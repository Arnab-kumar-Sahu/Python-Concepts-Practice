s='Hai PYTHon'
print(s.lower())
print(s.upper())

print(s.title())#convert the first character of every word into upper case and others into loower case in a string
S='arnabsahu@gmail.com'
print(S.title())

print(s.capitalize())#only convert the first character of a word in a string into upper case remaining all the words into lower case
print(s.swapcase())#if lower then convert it into upper or upper then convert into lower

#the method starting with "is" always gives boolean value
s1='hai'
print(s1.islower()) #gives true only if lower case alphabet 
s2='hai hello'
print(s2.islower())
s3='HELLO HIE'
print(s3.isupper())#give true only upper case alphabet
s4='Arnab Sandhya'
print(s4.istitle()) #gives true only if title case style

s5='Ankita'
print(s5.isalpha()) #gives true if only alphabet present no spaces
s6='Ankita Ankit'
print(s6.isalpha())

s7='12489478369713'
print(s7.isdigit())# gives true if only digits are present no spaces and alphabets
s8='12342 ufhgh 89489'
print(s8.isdigit())
s9='arnab1234'
print(s9.isalnum())#gives true if only alphabet present or only digits or mix of both but no spaces
s10='arnab37y4 urfio83'
print(s10.isalnum())

s11='   '
print(s11.isspace()) # gives true only if space is there
print(s2[3].isspace())
print(s3[5].isspace())


