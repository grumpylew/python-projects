# property decorators (getters, setters, deleters)
class Person:
    def __init__(self, name, age):
        self._name = name
        self._age = age

    # Getter for name
    @property
    def name(self):
        return self._name

    # Setter for name
    @name.setter
    def name(self, value):
        if not value:
            raise ValueError("Name cannot be empty.")
        self._name = value

    # Deleter for name
    @name.deleter
    def name(self):
        print("Deleting name...")
        self._name = None

    @property
    def get_age(self):
        return self._age

    @get_age.setter
    def get_age(self, value):
        if value < 0:
            raise ValueError("Invalid Age")
        self._age = value

    @get_age.deleter
    def get_age(self, value):
        self._age = None

    # Getter for email (computed from name)
    @property
    def email(self):
        return f"{self._name.lower().replace(' ', '.')}@example.com"


# Create a Person instance
person_1 = Person("John Doe", 30)

# Access the name
print(f"Name: {person_1.name}")  # Output: Name: John Doe
print(f"Email: {person_1.email}")  # Output: Email: john.doe@example.com

# Update the name
person_1.name = "Jane Doe"

# Access the updated name
print(f"Updated Name: {person_1.name}")  # Output: Updated Name: Jane Doe
print(f"Updated Email: {person_1.email}")  # Output: Updated Email: jane.doe@example.com

# Delete the name
del person_1.name

# Access the deleted attributes (will print None)
print(f"Deleted Name: {person_1.name}")  # Output: Deleted Name: None
