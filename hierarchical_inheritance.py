# INHERITANCE:- 
            # Inheritance means child class inherit the attributes and method from a parents class. Inherit process 
            # reduce redundency and establish a clean hirarchiee relation.

#HIERARCHICAL INHERITANCE:- 
            # In Hierarchical inheritance more than one child class inherit attribute and method  from single  parent class. 

######################     Parent  Class   #####################
class Phone:
    def __init__(self, brand, model, price):
        self.brand=brand
        self.model=model
        self.price=price
    def full_specification(self):
        print(f'Brand name {self.brand} model {self.model} and price are {self.price} \n')

######################     Child  Class 1  #####################
class Smartphone(Phone):
    def __init__(self, brand, model, price, android, color, camera):
        super().__init__(brand, model, price)
        self.android=android
        self.color=color
        self.camera=camera
    def full_specification(self):
        print(f'Brand name {self.brand}, model {self.model}, and price {self.price}. Android {self.android}, color {self.color}, camera {self.camera}. \n')

######################     Child  Class 2  #####################
class FlagshipPhone(Phone):
    def __init__(self, brand, model, price, ram, processor, battery):
        super().__init__(brand, model, price,)
        self.ram=ram
        self.processor=processor
        self.battery=battery
    def full_specification(self):
        print(f'Brand name {self.brand}, model {self.model}, and price {self.price}.  Ram {self.ram}, Processor {self.processor}, Battery {self.battery}.\n')

phone=Phone('Nokia', 'C3', 12000)
smartphone=Smartphone('Samsung', 'J2 Prime', 15000, 'KITKAT 10', 'SnowWhite', '50MP')
flagship=FlagshipPhone('Apple', 'Iphone 17 Pro Max', 156000, '12GB', 'A19 Chip', '6000mah')
smartphone.full_specification()
phone.full_specification()
flagship.full_specification()