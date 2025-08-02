n=int(input("Enter Any Number:"))
#The Uper Half 
if n >=3 and n <= 9:
    for i in range(1,n+1):
        c=i
        for j in range(n+1,i,-1):
            print(end="  ")
        for k in range(1,i+1):
            print(k,end=" ")
        if i>1: 
            for l in range(i-1,0,-1):
                print(l,end=" ")
        print("")

    #Lower Half
    for i in range(n-1,0,-1):
        c=i
        for j in range(i,n+1,1):
            print(end="  ")
        for k in range(1,i+1,1):
            print(k,end=" ")
        if i>1: 
            for l in range(i-1,0,-1):
                print(l,end=" ")
        print("")
else:
    print("Plz Enter Number Between 3 To 9 for a Perfect View")