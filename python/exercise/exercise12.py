#  Write a Python program to copy the contents of a file to another file.

f=open("E:\\BCA-SEM-5\\CS-30\\data-career-python-practice\\python\\exercise\\hello.txt","r")

f2=open("E:\\BCA-SEM-5\\CS-30\\data-career-python-practice\\python\\exercise\\hello_copy.txt","w")
#create new file name with hello_copy.txt and copy content of the hello.txt file
f2.write(f.read())
f2.close()
f.close()