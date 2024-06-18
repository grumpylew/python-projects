# basics
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
        return "woof"


# instantiate new instance of <class Dog>
d = Dog("Tim", 32)

# calling <bark> method using an instance
print(f"<bark> method: {d.bark()}")

d.set_age(23)
print(f" New age of dog: {Dog.get_age(d)}")  # call method using class
print(f" New age of dog: {d.get_age()}")  # call method using instance


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


# Inheritance
class Pet:  # parent class
    def __init__(self, name, age):
        self.name = name
        self.age = age

    # # default intro if not specified
    def intro(self):
        print(f"I am {self.name} and I am {self.age} years old")

    # default sound if not specified
    def sound(self):
        print("unspecified")


class Dog(Pet):  # child class
    pass


class Cat(Pet):
    def __init__(self, name, age, color):
        super().__init__(name, age)  # reference super/parent class attributes
        self.color = color  # add additional attribute

    def intro(self):
        print(f"I am {self.name} and I am {self.age} years old and I am {self.color}")

    def sound(self):
        print("meow")


p = Pet("Mio", 7)
p.intro()

c = Cat("Mikko", 3, "Calico")
c.intro()  # inherits methods/attributes from <class Pet>
c.sound()

d = Dog("Oreo", 5)
d.sound()
