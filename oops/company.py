class Company:
    Company_name="ABC"
    Company_location="Bangalore"
    Company_CEO="XYZ"
    def __init__(self,en,eage,ejob,esal):
        self.Ename=en
        self.Eage=eage
        self.Ejob=ejob
        self.Esal=esal
    def employee_details(self):
        print(f"Employee name is {self.Ename}")
        print(f"Employee age is {self.Eage}")
        print(f"Employee job is {self.Ejob}")
        print(f"Employee sal is {self.Esal}")
    @classmethod
    def company_details(cls):
        print(f"Company name is {cls.Company_name}")
        print(f"Company location is {cls.Company_location}")
        print(f"Company CEO is {cls.Company_CEO}")
    @staticmethod
    def get_int_value():
        int_value=int(input("enter integer value: "))
        return int_value
    def increment(self):
        amount=self.get_int_value()
        self.Esal+=amount
        print("new salary assigned")
    @staticmethod
    def change():
        change=input("enter new change: ")
        return change
    def new_job(self):
        new_job=self.change()
        self.Ejob=new_job
        print(f"new job is {self.Ejob}")
    @classmethod
    def new_company_location(cls):
        new_location=cls.change()
        cls.Company_location=new_location
        print(f"company new location is {cls.Company_location}")
arnab=Company("ARNAB KUMAR SAHU",21,'Python Developer',35000)
arnab.employee_details()
Company.company_details()
arnab.increment()
arnab.new_job()
Company.new_company_location()
Company.employee_details(arnab)