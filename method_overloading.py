#Method Overloading :- 
            # Python doesn't support traditional method overloading( class having multiple method with same name but different parameter). 
            # Instead python achive method overloading using default argument, *args. 


######################    Class   #####################
# class Calculator:
#     def add(self, a, b):
#         print(f'Sum of Two Number:- {a + b}')
#     def add( self,a, b, c):
#         print(f'Sum of Three Number:- {a + b + c}')
# total=Calculator()
# total.add(112, 18)    #TypeError:- required value of c
# total.add(12, 18, 14)

###########################         AntherWay    ############
class Calculator:
    def add( self,a, b=0, c=0):
        print(f'Sum of Three Number:- {a + b + c}')
total=Calculator()
# total.add(112, 18)    #TypeError:- required value of c
total.add(12, 18)
total.add(12, 18, 50)