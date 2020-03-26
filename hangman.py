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

