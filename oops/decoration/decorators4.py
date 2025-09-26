
# Online Python - IDE, Editor, Compiler, Interpreter
def print_args(func):
    def inner(*args):
        print("arguments:",args)
        func(*args)
    return inner
@print_args
def greet(name, age):
    print(f"{name} is {age} years old")

greet("Arnab", 21)



