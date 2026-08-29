# INHERITANCE:- 
            # Inheritance means child class inherit the attributes and method from a parents class. Inherit process 
            # reduce redundency and establish a clean hirarchiee relation.

#SINGLE INHERITANCE:- 
            # In single inheritance means single parent class and single child class .

######################     Parent  Class   #####################
class Phone:
    def __init__(self, brand, model, price):
        self.brand=brand
        self.model=model
        self.price=price
    def full_specification(self):
        print(f'Brand name {self.brand} model {self.model} and price are {self.price}')

######################     Child  Class   #####################
class Smartphone(Phone):
    def __init__(self, brand, model, price, android, color, camera):
        super().__init__(brand, model, price)
        self.android=android
        self.color=color
        self.camera=camera
    def full_specification(self):
        print(f'Brand name {self.brand}, model {self.model}, and price {self.price}. Android {self.android}, color {self.color}, camera {self.camera}. ')

phone=Phone('Nokia', 'C3', 12000)
smartphone=Smartphone('Samsung', 'J2 Prime', 15000, 'KITKAT 10', 'SnowWhite', '50MP')
smartphone.full_specification()
phone.full_specification()
