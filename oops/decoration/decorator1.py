
# Online Python - IDE, Editor, Compiler, Interpreter


def decorator(func):
    def wrapper(*args):
        print("Arguments:", args)
        return func(*args)
    return wrapper

@decorator
def add(a, b):
    return a + b

print(add(3, 4))



