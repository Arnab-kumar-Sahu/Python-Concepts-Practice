wantpizza=input('yes/no')

bill=0
if wantpizza.lower()=='yes' :
    sizeofpizza=input('size of pizza')
    if sizeofpizza.lower()=='small':
        bill+=100
        print('your bill is 100')
    elif sizeofpizza.lower()=='medium':
        bill+=200
        print('your bill is 200')
    elif sizeofpizza.lower()=='large':
        bill+=300
        print('your bill is 300')
    else:
        print('invalid size')
    pepperoni=input('yes/no')
    if pepperoni.lower()=='yes' and sizeofpizza.lower()=='small':
        bill+=20
    if pepperoni.lower()=='yes' and sizeofpizza.lower()=='large' or sizeofpizza.lower()=='medium':
        bill+=50
    cheese=input('yes/no')
    if cheese.lower()=='yes' and sizeofpizza.lower() in ['small','medium','large']:
        bill+=20
    print(bill)
else :
    print('no pizza')

