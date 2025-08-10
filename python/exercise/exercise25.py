#  Write a Python program to return multiple values at a time using a return statement. 
def multiple_value(v1,v2):
    
    return min(v1,v2),max(v1,v2)#return multiple value

v1=int(input("Enter Value1:"))
v2=int(input("Enter Value2:"))

min_value,max_value=multiple_value(v1=v1,v2=v2)#store return values in sequence

print("Largets Value:",max_value)
print("Smallest Value:",min_value)


