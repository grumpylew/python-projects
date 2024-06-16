# basic
values = [x for x in range(10)]
print(values)

# applying functions
from numpy import square

squared = [square(x) for x in range(10)]
print(squared)

# filtering (if is on the right)
evens = [number for number in range(10) if number % 2 == 0]
print(evens)

# multiple conditions
strings = ["any", "albandy", "apple", "world"]
valid_strings = [
    string
    for string in strings
    if len(string) >= 2
    if string[0] == "a"
    if string[-1] == "y"
]
print(valid_strings)

# nested for loops (first for loop is the outer one)
matrix = [[1, 2, 3], [4, 5, 6]]
flatten = [num for row in matrix for num in row]
print(flatten)

# if / Else (categorizes value, if is on the left as we are not filtering)
categories = ["Even" if x % 2 == 0 else "Odd" for x in range(10)]
print(categories)

# creating a hashmap / dictionary
pairs = [("a", 1), ("b", 2)]
my_dict = {k: v for k, v in pairs}
print(my_dict)

# creating a hashset
nums = [
    1,
    2,
    2,
    3,
    4,
    4,
]
unique_squares = {x**2 for x in nums}
print(unique_squares)
