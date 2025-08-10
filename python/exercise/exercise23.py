#  Write a Python program to work with the different ways of creating dictionary 
# objects with suitable example programs. 

# Program: Different ways to create Dictionary objects in Python

# 1. Creating an empty dictionary
dict1 = {}
print("1. Empty dictionary:", dict1)

# 2. Creating a dictionary using curly braces
dict2 = {"name": "Alice", "age": 25, "city": "New York"}
print("2. Dictionary using curly braces:", dict2)

# 3. Creating a dictionary using dict() constructor
dict3 = dict(name="Bob", age=30, city="London")
print("3. Dictionary using dict() constructor:", dict3)

# 4. Creating a dictionary from a list of tuples
dict4 = dict([("name", "Charlie"), ("age", 28), ("city", "Paris")])
print("4. Dictionary from list of tuples:", dict4)

# 5. Creating a dictionary using dictionary comprehension
dict5 = {x: x**2 for x in range(5)}
print("5. Dictionary comprehension (squares):", dict5)

# 6. Creating a dictionary from two lists using zip()
keys = ["name", "age", "city"]
values = ["David", 35, "Tokyo"]
dict6 = dict(zip(keys, values))
print("6. Dictionary from two lists using zip():", dict6)

# 7. Creating a dictionary with default values using fromkeys()
dict7 = dict.fromkeys(["name", "age", "city"], "Unknown")
print("7. Dictionary using fromkeys():", dict7)

# 8. Nested dictionary (dictionary inside a dictionary)
dict8 = {
    "emp1": {"name": "Emma", "age": 28},
    "emp2": {"name": "John", "age": 35}
}
print("8. Nested dictionary:", dict8)
