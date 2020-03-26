####        HANGMAN         ####

word_to_guess = 'pseudocode'
guessed_letters = []

def word():
    guessed = ''
    for letter in word_to_guess:
        if letter not in guessed_letters:
            letter = '_'
        guessed = guessed + letter + ''
    print(guessed)

def hangman():
    wrong_guesses = 5
    while wrong_guesses > 0:
        word()
        print('Guesses Left:', wrong_guesses)
        print('Guessed Letters:', *guessed_letters)
        guess = input("Guess a Letter: ")
        if guess and guess not in guessed_letters:
            guessed_letters.append(guess)
            if guess in word_to_guess:
                print("Correct")
            else:
                wrong_guesses -= 1

        letters_left = set(word_to_guess) - set(guessed_letters)
        if not in letters_left:
            print("You WIN!")
            return

    print('Guessed Letters:', *guessed_letters)
    print("You Lose!")

hangman()

## TODO ##

# need to figure how to stop when word guessed successfully

