####        HANGMAN         ####

word_to_guess = 'peudocode'
guessed_letters = []

def word():
    guessed = ''
    for letter in word_to_guess:
        if letter not in guessed_letters:
            letter = '_'
        hidden_word = hidden_word + letter + guessed
    print(hidden_word)

def hangman():
    wrong_guesses = 5
    while wrong_guesses > -1:
        word()
        print('Guesses Left:', wrong_guesses)
        print('Guessed Letters:', *guessed_letters)
        guess = input("?")
        if guess and guess not in guessed_letters:
            guessed_letters.append(guess)
            if guess in word_to_guess:
                print("Correct")
            else:
                wrong_guesses -= 1

hangman()
