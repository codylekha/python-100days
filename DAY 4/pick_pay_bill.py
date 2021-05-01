import random

names_string = input("Give me everybody's names, seperated by a comma.")

#Angela, Ben, Jenny
#splits the component based on some sort of divider ,
names = names_string.split(', ')
print(names)

num_items= len(names)
random_var = random.randint(0, num_items-1)

person_who_will_pay = names[random_var]
print(person_who_will_pay +"is going to pay the meal!")


#random.choice() is a replaces these codes