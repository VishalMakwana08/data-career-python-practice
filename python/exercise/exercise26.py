# Write a Python program to demonstrate Local and Global variables.



x=100 #Global Variable
def local():
    x=200 #Local Variable
    print("Local:",x)
local()
print("Global:",x)