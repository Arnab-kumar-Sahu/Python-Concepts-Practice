
class Address:
    def __init__(self,street,city,state,zip):
        self.street=street
        self.city=city
        self.state=state
        self.zip=zip
    def display_address(self):
        print(f"street is {self.street}")
        print(f"city is {self.city}")
        print(f"state is {self.state}")
        print(f"zip is {self.zip}")
class Student:
    def __init__(self,name,age,rollno):
        self.name=name
        self.age=age
        self.rollno=rollno
        street=input("enter street name")
        city=input("enter city name")
        state=input("enter state name")
        zip=input("enter zip code")
        self.address=Address(street,city,state,zip)
    def student_details(self):
        print(f"name is {self.name}")
        print(f"age is {self.age}")
        print(f"rollno is {self.rollno}")
        print("address is"), self.address.display_address()
arnab=Student("arnab",21,2102039)
arnab.student_details()
print(bool([]))