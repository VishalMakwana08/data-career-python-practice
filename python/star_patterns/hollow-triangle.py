#hollow triangle 
n=5
for i in range(1,6):
    n-=1
    print(n*" ",end="")#for right side space
    for j in range(1,i+1):
        if j==i or j==1 or i==5: #for actual position *
            print("* ",end="")
        else:
            print("  ",end="")#for space inside in a triangle
    print("")