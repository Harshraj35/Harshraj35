class car:
    total_car = 0
    def __init__(self, brand, model):
        self.__brand = brand
        self.__model = model
        car.total_car += 1

    def get_brand(self):
        return self.__brand + " !"     

    def full_name(self):
        return f"{self.__brand}{self.__model}" 
    
    def fuel_type(self):
        return "petrol or diesel" 
    
    @staticmethod
    def general_description():
        return "cars are means of transport"
    
@property    
def model(self):
    return self.__model





class electriccar(car):
    def __init__(self, brand, model, battery_size):
        super().__init__(brand, model)
        self.battery_size = battery_size

    def fuel_type(self):
        return "electic charge"     


#my_tesla = electriccar("tesla", "model s", "85kw")
#print(my_tesla.__brand) 
#print(my_tesla.fuel_type())  


my_car = ("tata", "safari")
my_car_model = "city"
car("tata", "nexon")


#print(my_car.general_description())
print(my_car_model)


#