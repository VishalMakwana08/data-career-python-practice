#reverse left half pyramid

num=0 #for indicate right side space
for i in range(5,0,-1):
    num+=1
    print(num*"  ",end="")#for right side space
    print(i*"* ")