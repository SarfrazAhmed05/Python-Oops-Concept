#Method Overriding :- 
            # A child class provide a specific implementation of a method that is already defined in its parent class.
            # Python determine Which version of the method call at runtime base on object's type.

######################     Parent  Class   #####################
class Phone:
    def __init__(self, brand, model, price):
        self.brand=brand
        self.model=model
        self.price=price
    def full_specification(self):                       #### full_specification() name Method in parent class 
        print(f'Brand name {self.brand} model {self.model} and price are {self.price}')

######################     Child  Class   #####################
class Smartphone(Phone):
    def __init__(self, brand, model, price, android, color, camera):
        super().__init__(brand, model, price)
        self.android=android
        self.color=color
        self.camera=camera
    def full_specification(self):                       ##### Same method in child class with specific implementation
        print(f'Brand name {self.brand}, model {self.model}, and price {self.price}. Android {self.android}, color {self.color}, camera {self.camera}. ')

phone=Phone('Nokia', 'C3', 12000)
smartphone=Smartphone('Samsung', 'J2 Prime', 15000, 'KITKAT 10', 'SnowWhite', '50MP')

smartphone.full_specification()                     #During Runtime as object's requirement  method will called .
phone.full_specification()
