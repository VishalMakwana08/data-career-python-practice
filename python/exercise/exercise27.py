 
# Write a Python program to work with the lambda functions in Python with suitable 
# examples. 

#lambad function

x=lambda a,b:a if a>b else b 

v1=int(input("Enter Value1:"))
v2=int(input("Enter Value2:"))

print("Largest Number:",x(v1,v2))