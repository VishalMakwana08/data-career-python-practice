#  Write a Python program to work with the following functions/methods which 
# operates on dictionary in Python with suitable examples: i) dict( ) ii) len( ) iii) clear( ) 
# iv) get( ) v) pop( )vi)popitem( ) vii) keys( ) viii) values() ix) items( ) x) copy( ) xi) 
# update( ) 
# Program: Demonstrating Dictionary Functions/Methods in Python

# 1) dict() - Create dictionary
dict1 = dict(name="Alice", age=25, city="New York")
print("1) dict():", dict1)

# 2) len() - Length of dictionary
print("2) len():", len(dict1))

# 3) clear() - Remove all items
temp_dict = dict1.copy()
temp_dict.clear()
print("3) clear():", temp_dict)

# 4) get() - Get value for a key (returns None if not found)
print("4) get('name'):", dict1.get("name"))
print("   get('salary'):", dict1.get("salary", "Not Found"))

# 5) pop() - Remove and return value by key
temp_dict = dict1.copy()
removed_value = temp_dict.pop("age")
print("5) pop('age'):", removed_value, "→", temp_dict)

# 6) popitem() - Remove and return last inserted key-value pair
temp_dict = dict1.copy()
last_item = temp_dict.popitem()
print("6) popitem():", last_item, "→", temp_dict)

# 7) keys() - Return all keys
print("7) keys():", dict1.keys())

# 8) values() - Return all values
print("8) values():", dict1.values())

# 9) items() - Return all key-value pairs
print("9) items():", dict1.items())

# 10) copy() - Create shallow copy
dict_copy = dict1.copy()
print("10) copy():", dict_copy)

# 11) update() - Add or modify items
dict2 = {"country": "USA", "age": 30}
dict1.update(dict2)
print("11) update():", dict1)
