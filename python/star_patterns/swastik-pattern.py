

for i in range(1,10):
    for j in range(1,10):
        if (i==1 and j>5) or (j==5 or i==5) or (i>5 and j==9) or (i==9 and j<5) or (j==1 and i <5) or ((i==3 or i==7) and (j==3 or j==7)):
           print("*",end=" ")
        else:
            print(" ",end=" ")
    print("")
'''
*       * * * * * 
*       *
*   *   *   *
*       *
* * * * * * * * *
        *       *
    *   *   *   *
        *       *
* * * * *       *
'''