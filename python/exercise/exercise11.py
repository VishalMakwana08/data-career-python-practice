# Write a Python program to work with the read and write operations on a file.



#Create And Write Into File hello.txt

f=open("E:\\BCA-SEM-5\\CS-30\\data-career-python-practice\\python\\exercise\\hello.txt","w")

f.write("Hello World")

f.close()

#Read Data From The hello.txt

f=open("E:\\BCA-SEM-5\\CS-30\\data-career-python-practice\\python\\exercise\\hello.txt","r")

print(f.read())

f.close()