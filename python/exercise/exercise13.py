# Write a Python program to work with the count frequency of characters in a given 
# file. 


f=open("E:\\BCA-SEM-5\\CS-30\\data-career-python-practice\\python\\exercise\\hello.txt","r")


content=f.read()

ch=input("Enter Character You Want To Count:")
#count() use for count the number of appearance characters
print(f"\'{ch}\' appear In The hello.txt file {content.count(ch)} Times")

f.close()