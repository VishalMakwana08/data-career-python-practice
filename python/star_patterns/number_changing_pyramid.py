#number changing pyramid
num=0
for i in range(1,6):
    for j in range(1,i+1):
        num+=1 #increase number like 1 2 3 4 5...n
        print(num,end=" ")
    print("")
  