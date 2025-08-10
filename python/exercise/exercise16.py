#  Write a Python program to work with the different ways of creating list objects with 
# suitable example programs. 

# 1. Creating a list using square brackets []
list1 = [1, 2, 3, 4, 5]
print("List using []:", list1)

# 2. Creating a list using list() constructor
list2 = list((10, 20, 30, 40))  # tuple converted to list
print("List using list() constructor:", list2)

# 3. Creating a list from a string (each char becomes an element)
list3 = list("Python")
print("List from string:", list3)

# 4. Creating a list using range()
list4 = list(range(1, 6))
print("List using range():", list4)

# 5. Creating a list with list comprehension
list5 = [x**2 for x in range(1, 6)]  # squares of numbers 1–5
print("List using list comprehension:", list5)

# 6. Creating an empty list
list6 = []
print("Empty list:", list6)

# 7. Creating a list with repeated elements
list7 = [0] * 5
print("List with repeated elements:", list7)

# 8. Creating a list from another iterable (set)
list8 = list({100, 200, 300})
print("List from set:", list8)
