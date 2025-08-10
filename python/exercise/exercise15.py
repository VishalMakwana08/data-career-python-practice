#  Write a Python program to compute the number of characters, words and lines in a 
# file.

f=open("E:\\BCA-SEM-5\\CS-30\\data-career-python-practice\\python\\exercise\\hello.txt","r")

lines=f.readlines()
#count number of lines
print("Number Of Lines In hello.txt file:",len(lines))

#count number of words
words=0

for line in lines:
    words+=len(line.split())

print("Number Of Words In hello.txt file:",words)

#count number of characters

characters=0
for line in lines:
    characters+=len(line.strip())

print("Number Of Characters In hello.txt file:",characters)

f.close()