# print (sep / end)
print("hello world", "hello", sep=" | ")
print("second line", end=" ")
print("third line")

# map (can pass functions too)
strings = ["my", "world", "apple", "pear"]
lengths = map(len, strings)  # returns map object
lengths = map(lambda x: x + "s", strings)
print(f"map output: {list(lengths)}")


# filter (similar to map)
def longer_than_4(string):
    return len(string) > 4


filtered = filter(longer_than_4, strings)  # returns filter object
filtered = filter(lambda x: len(x) > 4, strings)
print(f"filter output: {list(filtered)}")


# sort (using key)
people = [
    {"name": "Alice", "age": 30},
    {"name": "Bob", "age": 20},
    {"name": "Charlie", "age": 10},
]
sorted_people = sorted(people, key=lambda person: person["age"], reverse=True)
print(f"sort output: {sorted_people}")

# enumerate
for index, value in enumerate(strings):
    print(index, value)

# zip
names = [
    "Alice",
    "Bob",
    "Charlie",
]
ages = [30, 20, 10]

combined = list(zip(names, ages))  # returns zip object
print(combined)  # list of tuples
# output [('Alice', 30), ('Bob', 20), ('Charlie', 10)]

for name, age in combined:
    print(f"{name} is {age} years old")

# open (file / read - r / write - w / append - a)
# uses a context manager, ensures file is closed properly
# with open("test.txt", "r") as file:
# text = file.read()
# print(text)

# mutable vs immutable
x = 2
y = x  # makes a copy of x instead
x = 3  # does not affect y
print(x, y)

x = ["1", "2"]
y = x  # directly modifies x (linked) use y = x[:] to make a copy
x[0] = "100"
print(x, y)

# list comprehensions
x = [i for i in range(10) if i % 2 == 0]
print(x)

x = [[j for j in range(5)] for i in range(10)]
print(x)


# functions argument and parameter types
def complicated_func(x, y, z=None):  # z becomes optional / default value
    print(x, y, z)
    pass


complicated_func(2, z=1, y=3)


# args (pass any positional arguments in a tuple)
def complicated_func(x, y, *args):
    print(x, y, args)


complicated_func(1, 2, 3, 4, 5, 6, 7, 8)


# kwargs (pass any keyword arguments in a dict)
def complicated_func(*args, **kwargs):
    print(args, kwargs)


complicated_func(1, 2, 3, x=1, s="hello", b=True)


# example
def complicated_func(a, b, c=True, d=False):
    print(a, b, c, d)


complicated_func(*[1, 2], **{"c": "hello", "d": "cool"})

# __main__
# ensures u run file directly instead of being imported and ran by another file
if __name__ == "__main__":
    print("run")
