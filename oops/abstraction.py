from abc import ABC, abstractmethod
class Rentals(ABC):
    @abstractmethod
    def rent(self,hours):
        pass
class CarRental(Rentals):
    def rent(self,hours):
        rentamount=hours*350
        print(rentamount)
class BikeRental(Rentals):
    def rent(self,hours):
        rentamount=hours*150
        print(rentamount)
a=CarRental()
a.rent(2)
b=BikeRental()
b.rent(4)