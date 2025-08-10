#  Write a Python program to work with the different ways of creating set objects with 
# suitable example programs. 
# Program: Different ways of creating set objects in Python

# 1. Creating an empty set using set() constructor
empty_set = set()
print("1. Empty set:", empty_set, "Type:", type(empty_set))

# 2. Creating a set from a list
list_set = set([1, 2, 3, 4, 4, 5])
print("2. Set from list (duplicates removed):", list_set)

# 3. Creating a set from a tuple
tuple_set = set((10, 20, 30, 20, 40))
print("3. Set from tuple (duplicates removed):", tuple_set)

# 4. Creating a set from a string
string_set = set("Hello World")
print("4. Set from string (unique characters):", string_set)

# 5. Creating a set using curly braces {}
direct_set = {1, 2, 3, 4, 5}
print("5. Direct set using {}:", direct_set)

# 6. Creating a set from another set
copy_set = set(direct_set)
print("6. Set from another set (copy):", copy_set)

# 7. Creating a set from a range
range_set = set(range(1, 6))
print("7. Set from range:", range_set)

# 8. Creating a set using set comprehension
comp_set = {x * 2 for x in range(5)}
print("8. Set comprehension (x*2):", comp_set)
