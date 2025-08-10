#  Write Python programs to print the following Patterns:

for i in range(1,6):
    print(i*(str(i)+' '))
# 1 
# 22 
# 333 
# 4444 
# 55555 
print("")

for i in range(ord('A'),ord('E')+1):
    for j in range(ord('A'),i+1):
        print(chr(j),end=" ")
    print("")
print("")
# A 
# A B 
# A B C 
# A B C D 
# A B C D E 

for i in range(5,0,-1):
    print(i*'* ')
# ***** 
# **** 
# *** 
# ** 
# *