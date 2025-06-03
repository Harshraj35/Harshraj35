class car:
    total_car = 0
    def __init__(self, brand, model):
        self.__brand = brand
        self.model = model
        car.total_car += 1

    def get_brand(self):
        return self.__brand + " !"     

    def full_name(self):
        return f"{self.__brand}{self.model}" 
    
    def fuel_type(self):
        return "petrol or diesel" 
    

class electriccar(car):
    def __init__(self, brand, model, battery_size):
        super().__init__(brand, model)
        self.battery_size = battery_size

    def fuel_type(self):
        return "electic charge"     


#my_tesla = electriccar("tesla", "model s", "85kw")
#print(my_tesla.__brand) 
#print(my_tesla.fuel_type())  


car("tata", "safari")
car("tata", "nexon")

print(car.total_car)


#