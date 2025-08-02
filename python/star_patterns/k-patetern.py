#k pattern 

n=12 #use even number for best result
num=n//2 #mid range 
for i in range(1,n):
     if(i<(n//2)):
          print(num*"* ")
          num-=1
     else:
          print(num*"* ")
          num+=1