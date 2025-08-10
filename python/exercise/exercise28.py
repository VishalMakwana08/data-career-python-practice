 
# Write a program that asks the user to enter their name and their age. Print out a 
# message addressed to them that tells them the year that they will turn 60 years old. 
import datetime #for current date and time
current_date=datetime.datetime.now()
age=int(input("Enter Your Age:"))

if age>1 and age<60:
     born_year=current_date.year-age
     print("You Are Become 60 Year Old in",(born_year+60))
elif age>60:
    print("You Are Already Older Than 60 years ")
elif age==60:
    print("You Are Already 60 Year Old in ",current_date.year)
else:
    print("Invalid Age")