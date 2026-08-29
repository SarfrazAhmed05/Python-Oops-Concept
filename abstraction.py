#ABSTRACTION :- 
        ## It is used to hide implementation details and show only the necessary functionality.
        ## we can achive abstration using the ABC class and @abstractmethod decorator. An abstract class 
        ## can contain attribute, normal method, and abstract method.
from abc import ABC, abstractmethod

class Employee(ABC):

    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

    @abstractmethod
    def work(self):
        pass

    def display_info(self):
        print("Name:", self.name)
        print("Salary:", self.salary)


class Developer(Employee):

    def work(self):
        print("Developer writes Python code")


class Tester(Employee):

    def work(self):
        print("Tester tests the application")


# Create objects
developer = Developer("Rahul", 40000)
tester = Tester("Amit", 35000)

# Developer
developer.display_info()
developer.work()

print()

# Tester
tester.display_info()
tester.work()