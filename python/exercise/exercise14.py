#  Write a Python program to print each line of a file in reverse order.

f=open("E:\\BCA-SEM-5\\CS-30\\data-career-python-practice\\python\\exercise\\hello.txt","r")

for line in f:
    print(line.strip()[::-1]) #print file each line in reverse order    