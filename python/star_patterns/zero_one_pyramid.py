#=zero one pyramid


for i in range(1,6):
    for j in range(1,i+1):
        if ((not j%2==0)and(not i%2==0))or((j%2==0)and(i%2==0)):
            print(1,end=" ")
        else:
            print(0,end=" ")
    print("")
  