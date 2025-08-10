#  Write a Python program to work with the the following functions/methods which 
# operates on tuples in Python with suitable examples: i) len( ) ii) count( ) iii) index( ) 
# iv) sorted( ) v) min ( )vi)max( ) vii) cmp( ) viii) reversed( ) 

# Python program to demonstrate tuple functions/methods

# Creating tuples
tuple1 = (10, 20, 30, 40, 50)
tuple2 = (5, 15, 25, 35, 45, 55, 65)
tuple3 = (10, 20, 10, 40, 10)

print("Tuple 1:", tuple1)
print("Tuple 2:", tuple2)
print("Tuple 3:", tuple3)

# i) len()
print("\nLength of tuple1:", len(tuple1))

# ii) count()
print("Count of 10 in tuple3:", tuple3.count(10))

# iii) index()
print("Index of 40 in tuple1:", tuple1.index(40))

# iv) sorted()
print("Sorted tuple1:", sorted(tuple1))  # returns a list
print("Sorted tuple1 in descending:", sorted(tuple1, reverse=True))

# v) min()
print("Minimum value in tuple1:", min(tuple1))

# vi) max()
print("Maximum value in tuple1:", max(tuple1))

# vii) cmp() alternative in Python 3
# We'll use normal comparison operators
if tuple1 > tuple2:
    print("tuple1 is greater than tuple2")
elif tuple1 < tuple2:
    print("tuple1 is smaller than tuple2")
else:
    print("tuple1 and tuple2 are equal")

# viii) reversed()
print("Reversed tuple1:", tuple(reversed(tuple1)))
