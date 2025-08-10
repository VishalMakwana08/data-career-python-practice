#  Write a Python program to work with the following functions/methods which 
# operates on sets in Python with suitable examples: i) add( ) ii) update( ) iii) copy( ) 
# iv) pop( ) v) remove( )vi)discard( ) vii) clear( ) viii) union() ix) intersection( ) x) 
# difference( )

# Python Program - Demonstrating Various Set Functions/Methods

# 1. Creating a set
my_set = {1, 2, 3}
print("Initial Set:", my_set)

# i) add()
my_set.add(4)
print("\nAfter add(4):", my_set)

# ii) update()
my_set.update([5, 6, 7])
print("After update([5, 6, 7]):", my_set)

# iii) copy()
set_copy = my_set.copy()
print("Copy of set:", set_copy)

# iv) pop() - removes and returns an arbitrary element
popped_element = my_set.pop()
print("Popped element:", popped_element)
print("After pop():", my_set)

# v) remove() - removes specific element (Error if not found)
my_set.remove(4)
print("After remove(4):", my_set)

# vi) discard() - removes specific element (No error if not found)
my_set.discard(10)  # No error even though 10 is not in the set
print("After discard(10):", my_set)

# vii) clear() - removes all elements
temp_set = {1, 2, 3}
temp_set.clear()
print("After clear():", temp_set)

# viii) union()
set_a = {1, 2, 3}
set_b = {3, 4, 5}
union_set = set_a.union(set_b)
print("\nUnion of", set_a, "and", set_b, ":", union_set)

# ix) intersection()
intersection_set = set_a.intersection(set_b)
print("Intersection of", set_a, "and", set_b, ":", intersection_set)

# x) difference()
difference_set = set_a.difference(set_b)
print("Difference of", set_a, "and", set_b, ":", difference_set)
