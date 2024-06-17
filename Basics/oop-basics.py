# Object Oriented Progamming


class Dog:

    # intialise object when Dog() is created
    def __init__(self, name, age):
        self.name = name  # attribute of class
        self.age = age

    # method - something like .upper() for <class strings>
    def get_name(self):
        return self.name

    def get_age(self):
        return self.age

    def set_age(self, age):
        self.age = age

    def bark(self):
        print("woof")


d = Dog("Tim", 32)  # instantiate new instance of <class Dog>
# d.bark()   # calling <bark> method
# print(d.add_one(5))
# print(d.get_name())
d.set_age(23)
# print(d.get_age())


class Student:
    def __init__(self, name, age, grade):
        self.name = name
        self.age = age
        self.grade = grade

    def get_grade(self):
        return self.grade


class Course:
    def __init__(self, name, max_students):
        self.name = name
        self.max_students = max_students
        self.students = (
            []
        )  # list to store student object (has name, age, grade attributes)

    def add_students(self, student):
        if len(self.students) < self.max_students:
            self.students.append(student)
            return True
        return False

    def get_average_grade(self):
        value = 0
        for student in self.students:
            value += student.get_grade()
        return value / len(self.students)


s1 = Student("Tim", 19, 95)
s2 = Student("Bill", 19, 75)
s3 = Student("Jill", 19, 65)

course1 = Course("Science", 2)
course1.add_students(s1)
course1.add_students(s2)
# print(course1.add_students(s3))
# print(course1.students[0].name)
# print(course1.name)
# print(course1.get_average_grade())


# inheritance
class Pet:  # parent class
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def show(self):
        print(f"I am {self.name} and I am {self.age} years old")

    def sound(self):  # default sound if not specified
        print("N/A")


class Dog(Pet):  # child class
    pass


class Cat(Pet):
    def __init__(self, name, age, color):
        super().__init__(name, age)  # reference super/parent class attributes
        self.color = color  # add attributes

    def sound(self):
        print("meow")

    def show(self):
        print(f"I am {self.name} and I am {self.age} years old and I am {self.color}")


p = Pet("Tim", 19)
p.show()

c = Cat("Bill", 34, "Orange")
c.show()  # inherits methods/attributes from <class Pet>
c.sound()

d = Dog("Jack", 10)
d.sound()


# class methods (not tagged to any specific instance)
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
print(Person.num_of_people())


# static methods (can use without using an instance)
class Math:
    @staticmethod
    def add5(x):  # dont need any arguments (since no instance)
        return x + 5

    @staticmethod
    def pr():
        print("Test")


print(Math.add5(5))
Math.pr()
