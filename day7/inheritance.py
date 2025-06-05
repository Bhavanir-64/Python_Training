class Vehicle:
    def __init__(self, brand):
        self.brand = brand
    def honk(self):
        print("Beep beep!")

class Car(Vehicle):
    def __init__(self, brand, model):
        super().__init__(brand)  
        self.model = model
    def display_info(self):
        print(f"{self.brand} {self.model}")

my_car = Car("Honda", "Civic")
my_car.display_info()  
my_car.honk()          
