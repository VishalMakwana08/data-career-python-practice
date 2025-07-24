# Convert temperature from Celsius to Fahrenheit and vice versa using formula.

while True:
    print("1.Celsius to Fahrenheit")
    print("2.Fahrenheit to Celsius")
    print("3.Exit")
    choice=int(input("Enter Any Option:"))
    match choice:
        case 1:
            celsius=float(input("Enter Celsius:"))
            fahrenhit=celsius*9/5+32
            print(f"Fahrenheit:{fahrenhit}")
        case 2:
            fahrenhit=float(input("Enter Fahrenhit:"))
            celsius=(fahrenhit-32)*(5/9)
            print(f"Celsius:{celsius}")
        case 3:
            break
        case _:
            print("Invalid Option")
            break
