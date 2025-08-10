# Write a Python program to work with the control transfer statements in Python with 
# suitable examples. i) break ii) continue iii) pass

#i)break

for i in range(1,6):
    if i==3:
        break #Terminate Loop When i is equal to 3
    print(i,end=" ")

print("")
#ii)continue
for i in range(1,6):
    if i==3:
        continue #skip one iteration of the loop
    print(i,end=" ")


print("")
for i in range(1,6):
    pass #nothing 

