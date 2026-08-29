# INHERITANCE:- 
            # Inheritance means child class inherit the attributes and method from a parents class. Inherit process 
            # reduce redundency and establish a clean hirarchiee relation.

#MULTILEVEL INHERITANCE:- 
            # In multilevel inheritance child class inherit from parent class and parent class also  inherit attribute or method from 
            #grandparent class. It create multilayered generational chain.

######################     Grandparent  Class   #####################
class Phone:
    def __init__(self, brand, model, price):
        self.brand=brand
        self.model=model
        self.price=price
    def full_specification(self):
        print(f'Brand name {self.brand} model {self.model} and price are {self.price} \n')

######################     Parent  Class   #####################
class Smartphone(Phone):
    def __init__(self, brand, model, price, android, color, camera):
        super().__init__(brand, model, price)
        self.android=android
        self.color=color
        self.camera=camera
    def full_specification(self):
        print(f'Brand name {self.brand}, model {self.model}, and price {self.price}. Android {self.android}, color {self.color}, camera {self.camera}. \n')

######################     Child  Class   #####################
class FlagshipPhone(Smartphone):
    def __init__(self, brand, model, price, android, color, camera, ram, processor, battery):
        super().__init__(brand, model, price, android, color, camera)
        self.ram=ram
        self.processor=processor
        self.battery=battery
    def full_specification(self):
        print(f'Brand name {self.brand}, model {self.model}, and price {self.price}. Android {self.android}, color {self.color}, camera {self.camera}. Ram {self.ram}, Processor {self.processor}, Battery {self.battery}.\n')

phone=Phone('Nokia', 'C3', 12000)
smartphone=Smartphone('Samsung', 'J2 Prime', 15000, 'KITKAT 10', 'SnowWhite', '50MP')
flagship=FlagshipPhone('Apple', 'Iphone 17 Pro Max', 156000, 'LolliPop 15', 'Charchol Black', '20MP', '12GB', 'A19 Chip', '6000mah')
smartphone.full_specification()
phone.full_specification()
flagship.full_specification()