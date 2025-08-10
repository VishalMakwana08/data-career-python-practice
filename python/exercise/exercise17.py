#  Write a Python program to work with the following functions/methods which 
# operates on lists in Python with suitable examples: i) list( ) ii) len( ) iii) count( ) iv) 
# index ( ) v) append( ) vi) insert( ) vii) extend() viii) remove( ) ix) pop( ) x) reverse( ) 
# xi) sort( ) xii) copy( ) xiii) clear( ) 

# original list
my_list = [10, 20, 30, 20, 40]
print("Original List:", my_list)

# i) list() – Create a list from tupel
tuple_data = (1, 2, 3)
new_list = list(tuple_data)
print("list() from tuple:", new_list)

# ii) len() – Number of elements in a list
print("len():", len(my_list))

# iii) count() – Count occurrences of an element
print("count(20):", my_list.count(20))

# iv) index() – Find index of the first occurrence of an element
print("index(30):", my_list.index(30))

# v) append() – Add an element at the end
my_list.append(50)
print("After append(50):", my_list)

# vi) insert() – Insert element at a specific position
my_list.insert(2, 25)
print("After insert(2, 25):", my_list)

# vii) extend() – Add multiple elements from another list
my_list.extend([60, 70])
print("After extend([60, 70]):", my_list)

# viii) remove() – Remove the first occurrence of a value
my_list.remove(20)  # Removes the first 20
print("After remove(20):", my_list)

# ix) pop() – Remove element at given index (default last)
removed_element = my_list.pop()
print("After pop():", my_list, "| Removed:", removed_element)

# x) reverse() – Reverse the list in-place
my_list.reverse()
print("After reverse():", my_list)

# xi) sort() – Sort the list in ascending order
my_list.sort()
print("After sort():", my_list)

# xii) copy() – Create a shallow copy of the list
copied_list = my_list.copy()
print("copy() of list:", copied_list)

# xiii) clear() – Remove all elements from the list
my_list.clear()
print("After clear():", my_list)
