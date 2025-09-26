def outer(arg):
    print("outer function is started")
    print(arg)
    def inner():
        print("inner function is started")
        arg()
        print("inner function is ended")
    return inner
@outer#wish=outer(arg==wishFa)->wish=innerFA
def wish():
    print("wish function is started")
    print("wish function is ended")
wish()
@outer
def work():
    print("work function is started")
    print("work function is ended")
work()