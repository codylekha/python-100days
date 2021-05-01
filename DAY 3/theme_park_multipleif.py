height = int(input("enter the height in cm "))

if(height >= 120):
    print("Can ride")
    age = int(input("what is your age"))
    if age<12:
        bill = 5
        print(f"please pay  ${bill}")
    elif age<=18:
        bill =7
        print(f"please pay ${bill}")    
    else:
        bill =12
        print(f"please pay ${bill}")


    want_photos = input("Do you want a photo taken? Y or N.")
    if want_photos == "Y":
        bill+=3
    print(f"Your final bill is {bill}")        
else:
    print("Can't ride")            
