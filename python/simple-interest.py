# Take principal, rate, and time as input and calculate simple interest.

principal=float(input("Enter Principal Amount:"))
rate=float(input("Enter Interest Rate:"))
time=int(input("Enter Time In Months:"))
interest=(principal*rate)/100
total=principal+interest*time
print(f"Your Amount Is {principal}")
print(f"Your Interest Rate Is {rate}% For 1 Month")
print(f"Your Time Period Is {time} Months")
print(f"Total Amount Is {total:.2f}")