height = int(input("enter the height in cm "))

if(height > 120):
    print("Can ride")
    age = int(input("what is your age"))
    if age<=18:
        print("please pay  $7")
    else:
         print("please pay $12")
else:
    print("Can't ride")            
