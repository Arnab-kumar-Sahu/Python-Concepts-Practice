class incorrectpin(BaseException):
    def __init__(self, msg):
        self.msg = msg
class insufficientbalance(BaseException):
    def __init__(self, msg):
        self.msg = msg
class bank:
    def __init__(self,name,balance,pin):
        self.name=name
        self.balace=balance
        self.pin=pin
    def withdraw(self):
        pin=int(input("Enter pin: "))
        try:
            if self.pin!=pin:
                raise incorrectpin("incorrect pin")
            try:
                amount=int(input("Enter amount: "))
                if amount>=self.balace:
                    raise insufficientbalance("insufficient balance")
            except insufficientbalance as ie:
                    print(ie)
        except incorrectpin as ic:
                print(ic)
        else:
            self.balace-=amount
            print(f"available balance is {self.balace}")
arnab=bank("arnab",50000,1234)
arnab.withdraw()