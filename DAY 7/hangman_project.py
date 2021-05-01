import random
#using hangman_artfolder importing arts
# from hangman_art import stages,logo

word_list = ["aardvark", "baboon", "camel"]
chosen_word = random.choice(word_list)
word_length = len(chosen_word)

lives = 6

#Testing code
print(f'Pssst, the solution is {chosen_word}.')

#Create blanks
display = []
for _ in range(word_length):
    display += "_"

#TODO-1: - Use a while loop to let the user guess again. The loop should only stop once the user has guessed all the letters in the chosen_word and 'display' has no more blanks ("_"). Then you can tell the user they've won.
end_of_game = False

while not end_of_game:
    guess = input("Guess a letter: ").lower()

    #Check guessed letter
    for position in range(word_length):
        letter = chosen_word[position]
        #print(f"Current position: {position}\n Current letter: {letter}\n Guessed letter: {guess}")
        if letter == guess:
            display[position] = letter
    if guess not in chosen_word:
        lives -= -1
        if lives ==0:
            end_of_game = True
            print("You lose.")
    print(f"{' '.join(display)}")

    #Check if there are no more "_" left in 'display'. Then all letters have been guessed.
    if "_" not in display:
        end_of_game = True
        print("You win.")


    # OUTPUT
    # Pssst, the solution is camel.
    # Guess a letter: c
    # ['c', '_', '_', '_', '_']
    # Guess a letter: a
    # ['c', 'a', '_', '_', '_']
    # Guess a letter: m
    # ['c', 'a', 'm', '_', '_']
    # Guess a letter: e
    # ['c', 'a', 'm', 'e', '_']
    # Guess a letter: l
    # ['c', 'a', 'm', 'e', 'l']
    # You win.