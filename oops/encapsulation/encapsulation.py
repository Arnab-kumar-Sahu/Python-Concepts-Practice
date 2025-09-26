class A:
    name='abc'
    _age=20
    __mobile=9070400304
    def display(self):
        print(self.__mobile)
    def _protected(self):
        print("this is protected method")
    def __private(self):
        print("this is private method")
oa=A()
oa.display()
oa._protected()
oa._A__private()
