
# Online Python - IDE, Editor, Compiler, Interpreter

def outer(func):
    def inner(*args):
        result=func(*args)
        return result*2
    return inner
@outer
def add(x,y):
    return x+y
print(add(3,5))



