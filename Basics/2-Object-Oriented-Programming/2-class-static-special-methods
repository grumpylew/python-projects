# Class methods (not tagged to any specific instance)
class Person:
    number_of_people = 0

    def __init__(self, name):
        self.name = name
        Person.add_person()

    @classmethod
    def add_person(cls):
        cls.number_of_people += 1

    @classmethod
    def num_of_people(cls):
        return cls.number_of_people


p1 = Person("Tim")
p2 = Person("Bob")
print(f"num_of_people: {Person.num_of_people()}")


# static methods (can use without using an instance)
class Math:
    @staticmethod
    def add5(x):  # dont need any arguments (since no instance)
        return x + 5

    @staticmethod
    def pr():
        print("Test")


print(f"static method: {Math.add5(5)}")


# special methods / class and variable instance
class Employee:
    def __init__(self, name, pay):
        self.name = name
        self.pay = pay

    def apply_raise(self):
        self.pay = int(self.pay * self.raise_amount)

    @classmethod
    def set_raise_amount(cls, amount):
        cls.raise_amount = amount

    @staticmethod
    def is_workday(day):
        if day.weekday() == 5 or day.weekday() == 6:
            return False
        return True

    """ special / dunder - double underscores methods (eg. __init__) """

    # Defines a string representation of the object, useful for debugging.
    def __repr__(self) -> str:
        return f"Employee('{self.name}', '{self.pay}')"

    # basically the same as repr but print(emp1) takes precedence over repr
    def __str__(self) -> str:
        return f"Employee('{self.name}')"

    # special methods - arithmetic operators
    def __add__(self, other):
        return self.pay + other.pay

    # special methods - len operators
    def __len__(self):
        return len(self.name)


emp1 = Employee("Billyyy", 100)
emp2 = Employee("Bob", 100)

""" special methods """

# __repr__ method
print(f"__repr__: {emp1.__repr__()}")

# __str__ method
print(f"__str__: {emp1.__str__()}")

# __add__ method specifies how to add 2 emp together
print(f"__add__ : {emp1 + emp2}")

# __len__ method
print(f"__len__ : {emp1.__len__()}")


""" class and variable instance """

Employee.set_raise_amount(1.05)  # affects every instance
emp1.raise_amount = 1.06  # only affects this instance

print(f"overall raise amount: {Employee.raise_amount}")
print(f"emp1 raise amount:: {emp1.raise_amount}")
print(f"emp2 raise amount: {emp2.raise_amount}")

# import datetime
# print(Employee.is_workday(datetime.date(2024, 1, 1)))
