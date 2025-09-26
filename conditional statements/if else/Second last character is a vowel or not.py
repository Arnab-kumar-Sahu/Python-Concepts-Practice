s = input("Enter a string: ")
if  len(s) >= 2 and s[-2].lower() in 'aeiou':
    print("Second last character is a vowel")
else:
    print("Not a vowel")
