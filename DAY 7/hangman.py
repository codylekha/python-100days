#for & whileloop if else lists strings range modules

#breaking the problem
# 1. start 
# 2. generate random word
# 3. generate  blank 
# 4. is the guessed letter in the word
# 5. if yes replace the blank with the word
# 6. are all the blanks are filled
# 7. if yes gameover
# 8. step 4 if no lose a life
# 9. have they run out of lives 
# 10. if yes game over if no goto step4



#for loop with list
word_list = ["ardvark", "baboon", "camel"]

import random 
chosen_word = random.choice(word_list)
print(f"pssst the chosen word {chosen_word}" )
   
display = []
word_length = len(chosen_word)
for _ in range(word_length):
    display+= '_'
print(display)

end_of_game = False
while not end_of_game:
    guess = input("Guess a letter? ").lower()

    #check guessed letter
    for position in range(word_length):
        letter = chosen_word[position]
        print(f"Current Position: {position}\n Current letter: {letter}\n Guessed letter: {guess}")
        if letter == guess:
            display[position] = letter 

    print(display)


    if "_" not in display:
        end_of_game = True
        print("You Win!")

    #ctrl + right squarebracket