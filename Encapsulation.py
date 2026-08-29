#ENCAPSULATION :-
          # Wrapping up data(Attribute) and method associated with that
          #  data into a single unit is called ENCAPSULATION in python.

######################      Class   #####################
class Phone:
    def __init__(self, brand, model, price):
        self._brand=brand       #Protected :- It means method & object of the class access the variable.
        self.__model=model     #Private :- It means method of the class access the variable object can't be access the variable.
        self.price=price             #Public

#############       Method          #############
    def brand_name(self):
        print(f'Brand name is {self._brand} ')

    def full_specification(self):
        print(f'Brand name {self._brand} model {self.__model} and price are {self.price}')

###############     Object           ################
phone=Phone('Nokia', 'C3', 12000)
phone2=Phone('Reliance', 'Classic 200', 8000)
# phone.full_specification()
phone2.full_specification()         #Protected:- variable access by the method
print(phone._brand)                    #Protected :- variable access by the object

# phone.brand_name()
phone.full_specification()              #Private:- variable access by the method
print(phone2.__model)                  #Private :- variable can't access by the object

