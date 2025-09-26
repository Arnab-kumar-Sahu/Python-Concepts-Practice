class Nagarjuna():
    car='nano'
    house='1bhk'
    money=100000
    land="2acres"
class Akhil(Nagarjuna):
    house="3bhk"
    bike="Super XL"
amala=Nagarjuna()
zainab=Akhil()
print(Nagarjuna.money)
print(Nagarjuna.house)
print(amala.money)
print(amala.house)
print(Akhil.money)
print(Akhil.house)
print(zainab.money)
print(zainab.house)
#modification of parent class properties by using parent class then it modifies parent class and it's objects
#and child class and it's objects
Nagarjuna.money=50000
print(Nagarjuna.money)
print(amala.money)
print(Akhil.money)
print(zainab.money)
#modification of parent class properties by using parent class objects only modifies in that object
amala.money=20000
print(Nagarjuna.money)
print(amala.money)
print(Akhil.money)
print(zainab.money)
#modification of parent class properties by using child class only modifies child class and it's objects
Akhil.money=70000
print(Nagarjuna.money)
print(amala.money)
print(Akhil.money)
print(zainab.money)
#modification of parent class properties by using child class objects only modifies in that object
zainab.money=40000
print(Nagarjuna.money)
print(amala.money)
print(Akhil.money)
print(zainab.money)