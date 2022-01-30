import random
from wordlist import words

def print_design(guesses, word):
    if guesses == 0:
        print("___________\n"
              "|          |\n"
              "|\n"
              "|\n"
              "|\n"
              "|\n"
              "|__________")
    if (guesses == 1):
        print("___________\n"
              "|          |\n"
              "|          O\n"
              "|\n"
              "|\n"
              "|\n"
              "|__________")
    if (guesses == 2):
        print("___________\n"
              "|          |\n"
              "|          O\n"
              "|          \ \n"
              "|\n"
              "|\n"
              "|__________")
    if (guesses == 3):
        print("___________\n"
              "|          |\n"
              "|          O\n"
              "|         \ / \n"
              "|           \n"
              "|\n"
              "|__________")
    if (guesses == 4):
        print("___________\n"
              "|          |\n"
              "|          O\n"
              "|         \ / \n"
              "|          | \n"
              "|\n"
              "|__________")
    if (guesses == 5):
        print("___________\n"
              "|          |\n"
              "|          O\n"
              "|         \ / \n"
              "|          | \n"
              "|         /"
              "\n"
              "|__________")
    if (guesses == 6):
        print("___________\n"
              "|          |\n"
              "|          O\n"
              "|         \ / \n"
              "|          |\n"
              "|         / \ \n"
              "|__________")


def randomword():
    #words = ['random', 'shishir', 'perfect', 'nepal', 'gentle']
    word = random.choice(words).upper()
    return word


def hangman():
    guesses = 0
    guess_list = []
    word = randomword()
    wordlist = list(word)
    blanks = '_' * len(word)
    blank_list = list(blanks)
    new_blank_list = list(blanks)
    print('Lets play hangman')
    print('\n ' + ''.join(blank_list))

    while guesses < 6:
        guess = input('--> ').upper()

        if len(guess) > 1:
            print('Please enter one letter at a time ')
        elif guess == '':
            print('Enter at least one letter')
        elif guess in guess_list:
            print('You have already guessed these letter ')
            print(' '.join(guess_list))

        else:
            guess_list.append(guess)
            i = 0
            while i < len(word):
                if guess == word[i]:
                    new_blank_list[i] = wordlist[i]
                i = i + 1
            if new_blank_list == blank_list:
                print('Oops! your letter is not here ')
                guesses = guesses + 1
                print_design(guesses, word)

                if guesses < 6:
                    print('Guess again'.join(blank_list))
            elif wordlist != blank_list:
                blank_list = new_blank_list[:]
                print(''.join(blank_list))

                if wordlist == blank_list:
                    print('You won!')
                    print('Do you want to play again? If so than type y for yes and n for no')
                    again = input('--> ')
                    if again == 'y':
                        hangman()
                    quit()
                else:
                    print('Great guess!, Guess next')


hangman()
