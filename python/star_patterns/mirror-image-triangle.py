#mirror image triangle

n=0
for i in range(1,6):
    print(n*" ",end="")
    for j in range(i,6):
        print(j,end=" ")
    print("")
    n+=1
n=4
for i in range(4,0,-1):
    n-=1
    print(n*" ",end="")
    for j in range(i,6):
        print(j,end=" ")
    print("")
   
  