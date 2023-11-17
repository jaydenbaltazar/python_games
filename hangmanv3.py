import random


def hangman(attempts):      # hangman drawing in a list, so you can easily access them
    display = ['''
  _______
 /     |
 |     
 |     
 |
_|_''', '''
  _______
 /     |
 |     0
 |     
 |
_|_''', '''
  _______
 /     |
 |     0
 |     |
 |
_|_''', '''
  _______
 /     |
 |     0
 |    -|
 |
_|_''', '''
  _______
 /     |
 |     0
 |    -|-
 |
_|_''', '''
  _______
 /     |
 |     0
 |    -|-
 |    /
_|_''', '''
  _______
 /     |
 |     0
 |    -|-
 |    /(
_|_''']

    return display[attempts]


def get_secret_word(category):      # gets a random word from a specific category
    movies = ['avengers', 'dracula', 'frozen', 'jaws', 'shrek', 'barbie']
    animals = ['lion', 'snake', 'tiger', 'shark', 'horse']
    fruits = ['grape', 'mango', 'orange', 'lemon', 'lime']
    countries = ['finland', 'portugal', 'denmark', 'ireland', 'brazil']
    if category.lower() == 'movies':        # .lower() will allow the user to type Movies or MOVIES
        secret_word = random.choice(movies)     # And it will still continue the code
    elif category.lower() == 'animals':
        secret_word = random.choice(animals)
    elif category.lower() == 'fruits':
        secret_word = random.choice(fruits)
    elif category.lower() == 'countries':
        secret_word = random.choice(countries)
    return secret_word


def display_board(word):
    spaces = '_' * len(word)    # tells the user how many spaces in the word
    guessed = False
    guessed_words = []  # starts with an empty list since it will be filled w/ user inputs
    guessed_letters = []
    attempts = 0
    print(hangman(attempts))    # calling a function within a function
    print(spaces)
    while not guessed and attempts < 6:
        guess = input('Guess a letter or word: ').lower()   # makes input lowercase since all the keywords are lowercase
        if len(guess) == 1 and guess.isalpha():     # .isalpha is to make sure the user input is in the alphabet
            if guess in guessed_letters:
                print(f'You already guessed the letter, {guess.upper()}')
            elif guess not in word:
                print(f'{guess.upper()} is not in the word.')
                attempts += 1
                guessed_letters.append(guess)   # adds the guessed letter to the empty list
            else:
                print(f'{guess.upper()} is in the word.')
                guessed_letters.append(guess)
                spaces_list = list(spaces)
                indices = [i for i, letter in enumerate(word) if letter == guess]
                for index in indices:   # this allows the correct letter in the space
                    spaces_list[index] = guess
                    spaces = ''.join(spaces_list)
                    if '_' not in spaces:   # if user puts in all the correct letter then you win since guessed = true
                        guessed = True
        elif len(guess) == len(word) and guess.isalpha():   # instead of checking the letters you check words
            if guess == word:
                guessed = True
                spaces = word
            elif guess not in guessed_words:
                print(f'{guess.upper()} is not the word.')
                attempts += 1
                guessed_words.append(guess)
            elif guess in guessed_words:
                print(f'You already guessed this word, {guess.upper()}.')
        else:
            print('Not a valid guess.')
        print(hangman(attempts))    # calling the function hangman to show the picture
        print(spaces)   # shows the spaces
    if guessed:
        print(f'YOU GOT IT! The word was {word.upper()}.')
    else:
        print(f'No more tries. The word was {word.upper()}. Maybe next time!')
    return


def play():
    plays = 1   # counts how many times the user plays. Start at 1 so it counts the first game
    start = input('Do you want to play HANGMAN? ').lower()
    game = True
    if start == 'yes' or start == 'y':
        while game:
            print('''
                ===========
                  HANGMAN
                ===========
Categories: Movies, Countries, Animals, Fruits''')
            choice = input('Pick a category: ')
            correct_word = get_secret_word(choice)
            display_board(correct_word)
            play_again = input('Do you want to play again? ').lower()
            if play_again == 'no' or play_again == 'n':
                game = False
                print(f'Thanks for playing HANGMAN {plays} times!')
            else:
                plays += 1
    else:
        print('fine :(')
        quit()
    return


if __name__ == '__main__':  # protect users from accidentally executing code from another module or file
    play()
