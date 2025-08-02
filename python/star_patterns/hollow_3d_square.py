#hollow 3d square 

for i in range(1,19):
    for j in range(1,19):
        if ((j==1 or j==9) and i<10) or ((j==5 or j==13) and i>5 and i<14) or(i==5 and j>4 and j<14) or((i==1 or i==9) and j<9) or(i==13 and j>4 and j<14) or (i==j and ((j<5)or(j>9 and j<14)))or(i<6 and j==8+i)or(i>8 and i<14 and(j==i-8)):
            print("* ",end=" ")
        else:
            print("  ",end=" ")
    print("")