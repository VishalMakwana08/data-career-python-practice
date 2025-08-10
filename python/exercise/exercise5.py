# Write a Python program to work with the following Operators in Python with 
# suitable examples. 
# i) Arithmetic Operators  
# ii) Relational Operators  
# iii) Assignment Operator  
# iv) Logical Operators  
# v) Bit wise Operators  
# vi) Ternary Operator 

#i) Arithmetic Operators  

a = 10
b = 3
print("\nArithmetic Operation Output:\n")
print("Addition:", a + b)        
print("Subtraction:", a - b)     
print("Multiplication:", a * b)  
print("Division:", a / b)        
print("Floor Division:", a // b) 
print("Modulus:", a % b)         
print("Exponentiation:", a ** b) 


# ii) Relational Operators  
print("\nRelational Operation Output:\n")
print("Equal to:", a == b)           
print("Not equal to:", a != b)       
print("Greater than:", a > b)        
print("Less than:", a < b)           
print("Greater or equal:", a >= b)   
print("Less or equal:", a <= b)      


# iii) Assignment Operator 
print("\nAssignment Operation Output:\n")
x = 10
print("Start: x =", x)

# Arithmetic assignment operators
x += 5      # Add and assign
print("After x += 5:", x)   # 15

x -= 3      # Subtract and assign
print("After x -= 3:", x)   # 12

x *= 2      # Multiply and assign
print("After x *= 2:", x)   # 24

x /= 4      # Divide and assign (float result)
print("After x /= 4:", x)   # 6.0

x //= 2     # Floor divide and assign
print("After x //= 2:", x)  # 3.0

x %= 2      # Modulus and assign
print("After x %= 2:", x)   # 1.0

x **= 3     # Exponentiation and assign
print("After x **= 3:", x)  # 1.0 (1³ = 1)


# iv)Logical Operators  
print("\nLogical Operation Output:\n")
v1=True
v2=False

print(v1 and v2) # and logical operator

print(v1 or v2) #or logical operator

print(not(v1 and v2)) #not logical operator


# v) Bit wise Operators 

print("\nBitwise Operation Output:\n")
a = 5   # 0101 in binary
b = 3   # 0011 in binary

print("a & b =", a & b)  #AND bitwise
print("a | b =", a | b)  #OR bitwise
print("a ^ b =", a ^ b)  #XOR bitwise
print("~a =", ~a)        #NOT bitwise
print("a << 1 =", a << 1)#Left shift bitwise
print("a >> 1 =", a >> 1)#Right shift bitwise

# vi) Ternary Operator 
print("\nTernary Operation Output:\n")
a=10
b=30
largest= a if a>b else b

print("Largest:",largest)