class car:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model

    def full_name(self):
        return f"{self.brand}{self.model}" 


class electriccar(car):
    def __init__(self, brand, model, battery_size):
        super().__init__(brand, model)
        self.battery_size = battery_size 


my_tesla = electriccar("tesla", "model s", "85kw")
print(my_tesla.full_name())              


#