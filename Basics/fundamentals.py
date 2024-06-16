# print (sep / end)
print("hello world", "hello", sep=" | ")
print("second line", end=" ")
print("third line")

# map (can pass functions too)
strings = ["my", "world", "apple", "pear"]
lengths = map(len, strings)  # returns map object
lengths = map(lambda x: x + "s", strings)
print(list(lengths))


# filter (similar to map)
def longer_than_4(string):
    return len(string) > 4


filtered = filter(longer_than_4, strings)  # returns filter object
filtered = filter(lambda x: len(x) > 4, strings)
print(list(filtered))


# sort (using key)
people = [
    {"name": "Alice", "age": 30},
    {"name": "Bob", "age": 20},
    {"name": "Charlie", "age": 10},
]
sorted_people = sorted(people, key=lambda person: person["age"], reverse=True)
print(sorted_people)

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

for name, age in combined:
    print(f"{name} is {age} years old")

# open (file / read - r / write - w / append - a)
# uses a context manager, ensures file is closed properly
with open("test.txt", "r") as file:
    text = file.read()
    print(text)
