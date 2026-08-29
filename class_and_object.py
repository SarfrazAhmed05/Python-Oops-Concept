######################      Class   #####################
class Phone:
    def __init__(self, brand, model, price):
        self.brand=brand
        self.model=model
        self.price=price
#############       Method          #############
    def full_specification(self):
        print(f'Brand name {self.brand} model {self.model} and price are {self.price}')
###############     Object           ################

phone=Phone('Nokia', 'C3', 12000)
phone2=Phone('Reliance', 'Classic 200', 8000)
phone.full_specification()
phone2.full_specification()
print(phone.brand)
print(phone2.model)