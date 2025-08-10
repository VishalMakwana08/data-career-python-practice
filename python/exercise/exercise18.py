#  Write a Python program to work with the different ways of creating tuple objects 
# with suitable example programs. 

# 1. Creating an empty tuple
tuple1 = ()
print("Empty tuple:", tuple1)

# 2. Creating a tuple with elements
tuple2 = (1, 2, 3, 4, 5)
print("Tuple with elements:", tuple2)

# 3. Creating a tuple without parentheses (tuple packing)
tuple3 = 10, 20, 30
print("Tuple packing (no parentheses):", tuple3)

# 4. Creating a single element tuple (needs a comma!)
tuple4 = (5,)
print("Single element tuple:", tuple4)

# 5. Creating a tuple using tuple() constructor from a list
tuple5 = tuple([10, 20, 30])
print("Tuple from list:", tuple5)

# 6. Creating a tuple from a string
tuple6 = tuple("Python")
print("Tuple from string:", tuple6)

# 7. Creating a tuple from another (set)
tuple7 = tuple({100, 200, 300})
print("Tuple from set:", tuple7)

# 8. Nested tuple
tuple8 = (1, 2, (3, 4, 5))
print("Nested tuple:", tuple8)

# 9. Tuple comprehension (via generator, then converted to tuple)
tuple9 = tuple(x**2 for x in range(5))
print("Tuple using comprehension:", tuple9)
