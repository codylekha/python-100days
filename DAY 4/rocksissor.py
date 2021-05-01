import random

rock = '''
       _____Rock__
  ---'   ____)
        (_____)
        (_____)
        (____)
  ---.__(___)
       '''
scissors = '''
       _____Scissors__
  ---'   ____)____
        (_________)
        (_________)
        (____)
  ---.__(___)
       '''
paper = '''
       _____Paper__
  ---'   ____)____
        (_________)
        (_________)
        (_________)
  ---.__(_________)
       '''

game_images = [rock,paper,scissors]
user_choice = int(input("What do you choose? Type 0 for rock 1 for paper 2 for Scissors "))
print(game_images[user_choice])

computer_choice = random.randint(0,2)
print("Computer Chose: ")
print(game_images[computer_choice])


if user_choice>=3 or user_choice<0:
     print("You entered invalid number")
if user_choice == 0 and computer_choice == 2:
    print("You Win!")
elif computer_choice ==0 and  user_choice==2:
    print("You lose")
elif computer_choice > user_choice:
    print("You lose")    
elif user_choice > computer_choice:    
    print("You Win!")
elif computer_choice == user_choice:
    print("Its draw")  
