num=int(input("Enter A Number You Want To Print Table:"))

if num>0:
    for i in range(1,11):
        print(f"{num}*{i}={num*i}")
else:
    print("Plz Enter Number Greater Than 0")