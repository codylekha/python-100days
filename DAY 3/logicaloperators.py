# A and B
# C or D
# not E

height = int(input("enter the height"))
age = int(input("What is your age? "))

if height>120:
    print("Can ride")
    if age<12:
        bill = 5
        print("Child tickets are $5")
    elif age<=18:
        print("Youth tickets are $7")
        bill = 7
    elif age>=45 and age<=55:
        bill = 0
    else:
        bill=12        
    want_photos = input("Do you want a photo taken? Y or N.")
    if want_photos == "Y":
        bill+=3
    print(f"Your final bill is {bill}")        
else:
    print("Can't ride")           

