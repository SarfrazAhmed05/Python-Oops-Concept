# INHERITANCE:- 
            # Inheritance means child class inherit the attributes and method from a parents class. Inherit process 
            # reduce redundency and establish a clean hirarchiee relation.

#MULTIPLE INHERITANCE:- 
            # In multiple inheritance child class inherit attribute and method  from more than one parent class. 

######################     Parent  Class  1 #####################
class Phone:
    def __init__(self, brand, model, price):
        self.brand=brand
        self.model=model
        self.price=price
    def full_specification(self):
        print(f'Brand name {self.brand} model {self.model} and price are {self.price} \n')

######################     Parent  Class 2  #####################
class Smartphone:
    def __init__(self,android, color, camera):
        self.android=android
        self.color=color
        self.camera=camera
    def full_specification(self):
        print(f' Android {self.android}, color {self.color}, camera {self.camera}. \n')

######################     Child  Class   #####################
class FlagshipPhone(Phone, Smartphone):
    def __init__(self, brand, model, price,android, color, camera, ram, processor, battery):
        Phone.__init__(self,brand, model, price)
        Smartphone.__init__(self, android, color, camera)
        self.ram=ram
        self.processor=processor
        self.battery=battery
    def full_specification(self):
        print(f'Brand name {self.brand}, model {self.model}, and price {self.price}.Android {self.android}, color {self.color}, camera {self.camera}.   Ram {self.ram}, Processor {self.processor}, Battery {self.battery}.\n')

phone=Phone('Nokia', 'C3', 12000)
smartphone=Smartphone('KITKAT 10', 'SnowWhite', '50MP')
flagship=FlagshipPhone('Apple', 'Iphone 17 Pro Max', 156000,'LolliPop 15', 'Charchol Black', '50MP', '12GB', 'A19 Chip', '6000mah')
smartphone.full_specification()
phone.full_specification()
flagship.full_specification()