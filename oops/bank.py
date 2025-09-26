class Bank:
    Bank_name="SBI"
    Bank_ifsc=1234
    Bank_branch="marathali"
    Bank_roi=5
    def __init__(self,cn,cac,cbal):
        self.cname=cn
        self.caccountname=cac
        self.cbalance=cbal
    @staticmethod
    def get_int_value():
        int_value=int(input("enter integer value: "))
        return int_value
    def coustmer_details(self):
        print(f"coustmer name is {self.cname}")
        print(f"coustmer account name is {self.caccountname}")
        print(f"coustmer balance is {self.cbalance}")
    @classmethod
    def Bank_details(cls):
        print(f"bank name is {cls.Bank_name}")
        print(f"bank ifcode is {cls.Bank_ifsc}")
        print(f"bank branch is {cls.Bank_branch}")
        print(f"bank roi is {cls.Bank_roi}")
    def withdraw(self):
        amount=self.get_int_value()
        if amount < self.cbalance:
            self.cbalance -= amount
            print("withdrawal sucessfull")
        else:
            print("insufficient balance")
        print("remaining balance is:",self.cbalance)
    def deposit(self):
        amount=self.get_int_value()
        self.cbalance += amount
        print("deposit sucessfull")
    @classmethod
    def new_roi(cls):
        new_roi=cls.get_int_value()
        cls.Bank_roi=new_roi
        print(f"new rate of interest is {cls.Bank_roi}")
arnab=Bank("arnab",12543,200000)
arnab.coustmer_details()
Bank.Bank_details()
arnab.withdraw()
arnab.deposit()
Bank.new_roi()