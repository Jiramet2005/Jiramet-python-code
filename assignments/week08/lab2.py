""" 
Create a class hierarchy:

    Base class Vehicle with attributes: brand, model, year
    Derived class Car with additional attribute: number_of_doors
    Implement a method get_info() in both classes

"""
class Vehicle:
    def __init__(self, brand, model, year):
        # Instance attributes (unique to each instance)
        self.brand = brand
        self.model = model
        self.year = year
    def get_info(self):
        return f"Brand: {self.brand}, Model: {self.model}, Year: {self.year}"


class Car(Vehicle):
    def __init__(self,brand,model,year,number_of_door):
        super().__init__(brand,model,year)
        self.number_of_door = number_of_door
    def get_info(self):    
        return f"Brand: {self.brand}, Model: {self.model}, Year: {self.year}, Number of door: {self.number_of_door}"
    
molly = Car("ToYoTa","Prius","2020",4)
print(molly.get_info())