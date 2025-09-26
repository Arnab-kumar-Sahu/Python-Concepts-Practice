def sum (*args):
    print(args)
    summ=0
    for i in args:
        summ+=i
        print(f'number: {i}')
    print('sum is:',summ)
sum(21,34)
sum(45,6,42,43,5,45,6,67,89,6)
sum(23,65,76)