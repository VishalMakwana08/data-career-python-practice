# Area Calculator

while True:
    print("1.Area Of Circle")
    print("2.Area Of Rectangle")
    print("3.Exit")
    choice=int(input("Enter Any Option:"))
    match choice:
        case 1:
            PI=3.1416
            radius=float(input("Enter Ratio Of Circle:"))
            area=PI*(radius**2)
            print(f"Area Of Circle Based On Given Radius Is:{area:.2f}")
        case 2:
            length = float(input("Enter the length of the rectangle: "))
            width = float(input("Enter the breadth of the rectangle: "))
            area = length * width
            print(f"Area of the rectangle is: {area:.2f}")

        case 3:
            break
        case _:
            print("Invalid Option")
            break



