
class Address:
    def __init__(self, street, city, state, zip):
        self.street = street
        self.city = city
        self.state = state
        self.zip = zip
    def display_address(self):
        print(f"street is {self.street}")
        print(f"city is {self.city}")
        print(f"state is {self.state}")
        print(f"zip is {self.zip}")
banglore = Address('belandur','marathali','karnataka',567002)
class student():
   def __init__(self,name,age,rollno,address):
      self.name = name
      self.age = age
      self.rollno = rollno
      self.address = address
   def student_info(self):
      print(f"name is {self.name}")
      print(f"age is {self.age}")
      print(f"rollno is {self.rollno}")
      print("address is ") ,self.address.display_address()
arpita=student("arpita",21,212039,banglore)
arpita.student_info()