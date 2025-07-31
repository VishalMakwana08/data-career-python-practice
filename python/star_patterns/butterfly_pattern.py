
#butterfly pattern
num=int(input("Enter Any Number Greater Than 3 :"))
if num%2!=0:
    num+=1
mid=num//2
if num>3:
    for i in range(1,num):
        for j in range(1,num):
            if (i==j) or (j==num-i) or j==1 or j==num-1 or((i>2 and i <mid+1)and( j<i or j>num-i))or(i>mid and (j<num-i or j>i)):
                print("*",end=" ")
            else:
                print(" ",end=" ")
        print("")
else:
    print("Plz Enter Number Greater Than 3")
#Output:
#Enter Any Number Greater Than 3 :11
# *                   * 
# * *               * *
# * * *           * * *
# * * * *       * * * *
# * * * * *   * * * * *
# * * * * * * * * * * *
# * * * * *   * * * * *
# * * * *       * * * *
# * * *           * * *
# * *               * *
# *                   *
