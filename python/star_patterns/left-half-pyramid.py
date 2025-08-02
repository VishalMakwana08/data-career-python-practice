#left half pyramid

num=5 #for indicate right side space
for i in range(1,6):
    num-=1
    print(num*"  ",end="")#for right side space
    print(i*"* ")