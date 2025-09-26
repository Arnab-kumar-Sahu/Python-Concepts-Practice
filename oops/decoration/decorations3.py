
# Online Python - IDE, Editor, Compiler, Interpreter

def heck_even(func):
    def inner(*args):
        if func(*args)%2==0:
            print("Even result")
        else:
            print("odd result")
    return inner
@heck_even
def multiply(x,y):
    return x*y
multiply(23,4)
multiply(7,9)
multiply(15,6)
    


