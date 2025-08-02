# Swap Two Numbers Without Temp Variable

num1=int(input("Enter First Number:"))
num2=int(input("Enter Second Number:"))

print("Before Swap:")
print(f"num1 is {num1} and num2 is {num2}")

print("After Swap")
#swap numbers 
num1=num1-num2
num2=num2+num1
num1=num2-num1
print(f"num1 is {num1} and num2 is {num2}")