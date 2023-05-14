class car:
    def __init__(self, brand, YOM, YOR):
        self.brand = brand
        self.YOM = YOM
        self.YOR = YOR

    
    def get_data(self):
        return self.brand, self.YOM, self.YOR

        

car1 = car("Toyota", "2019", "2020")
print(f"car brand : {car1.brand}\n YOM : {car1.YOM}\n YOR : {car1.YOR}")
print("===========================")
print(car1.get_data())

