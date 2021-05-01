print("Welcome to Python pizza Deliveries!")
size = input("What size pizza do you want? S,M,L ")

if size=="S":
    bill = 15
    
    print("Small Pizza's Order $15")
    add_pepperoni = input("Do you want pepperoni? Y or N ")
    if add_pepperoni=="Y":
        bill = bill+2
        print(f"Pepperoni for small pizza: ${bill}")
        extra_cheese = input("Do you want extra cheese")

    if extra_cheese=="Y":
        bill +=1
        print(f"Extra Cheese for any pizza: ${bill}")


elif size=="M":
    bill = 20
    print("Medium Pizza's Order $20")
    add_pepperoni = input("Do you want pepperoni? Y or N ")
    if add_pepperoni=="Y":
        bill = bill+3
        print(f"Pepperoni for small pizza: ${bill}")
        extra_cheese = input("Do you want extra cheese")

    if extra_cheese=="Y":
        bill +=1
        print(f"Extra Cheese for any pizza: ${bill}")

elif size=="L":
    bill = 25
    print("Large pizza's Order $25")
    add_pepperoni = input("Do you want pepperoni? Y or N ")
    if add_pepperoni=="Y":
        bill = bill+3
        print(f"Pepperoni for small pizza: ${bill}")
        extra_cheese = input("Do you want extra cheese")

    if extra_cheese=="Y":
        bill +=1
        print(f"Extra Cheese for any pizza: ${bill}")

else:
    print("Invalid input")



