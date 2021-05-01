
#if the bill was $150.00, split between 5 people, 12% tip.
#each person should pay (150.00 / 5) * 1.12 = 3.36
#round the result to 2 decimals places
print("Welcome to the tip calculator!")

bill = float(input("What was the total bill? $"))
people  = int(input("How many people to split the bill?"))
tip  = int(input("What percentage tip would you like to give? 10, 12 & 15? "))

bill_with_tip = tip / 100 * bill + bill

print(bill_with_tip)


tip_as_percent = tip / 100 #12/100=0.12
total_tip_amount = bill * tip_as_percent #100*0.12=12
total_bill = bill + total_tip_amount #100+12 =112.0
bill_per_person = total_bill / people #112.0/4 = 28
final_amount = round(bill_per_person, 2) #how many decimals
#print(f"Each person should pay:${final_amount} ")
#this is fstring add f in front

#prints 2decimal at last
final_amount ="{:.2f}".format(bill_per_person)
print(f"Each person should pay:${final_amount} ")
