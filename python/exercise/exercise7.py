# Write a Python program to work with the Conditional statements in Python with 
# suitable examples. i) if statement ii) if else statement iii) if – elif – else statement 


a=30
b=20

# i) if statement

if a>b:
    print(f"{a} is largest number")

# ii) if else statement
x=10
y=20

if x>y:
    print(f"{x} is largest number")
else:
     print(f"{y} is largest number")


# iii) if – elif – else statement 

x=10
y=10

if x>y:
     print(f"{x} is largest number")
elif y>x:
     print(f"{y} is largest number")
else:
     print("Both are equal")