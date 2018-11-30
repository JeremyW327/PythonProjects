# Jeremy Wilson
# Guess The Word Game
# Only single words will be guessed

# List of words to guess
wordlist = ['banana', 'apple', 'kiwi', 'pear', 'orange', 'grape']
list_of_guessed_letters = []

# User Input
# Get user's guess, check to make sures its valid
# return valid letter guess
def getuserguess():
    guess = raw_input("Guess a Letter: ")
    while True:
        if len(guess) > 1 or guess.isdigit():
            guess = raw_input("Single letters and No numbers. Guess Again: ")
        else:
            print('You have guessed {}.'.format(guess))
            list_of_guessed_letters.append(guess)
            list_of_guessed_letters.sort()
            break

    return guess

# Display Function
# Adds spaces to the word for easier viewing
def displayaddspaces(word, length):
    i, j = 0, 0
    tempWord = []
    while i < length:
        tempWord.append(word[i] + " ")
        i += 1
    word = ''.join(tempWord)
    return word
    #return underscores

# Scan word for letter they user has guessed
# return either no letters found message
# or replace underscores with letter
def searchword(letter, word, word_):
    wordtemp = [x for x in word_]
    for num, c in enumerate(word):
        if letter == c:
            wordtemp[num] = letter
    newword = ''.join(wordtemp)
    return newword

# Game Start
i = 0
userchoice = raw_input("Do you want to play? (yes/no): ")
while True:

    if userchoice == "yes":
        word = wordlist[i]
        i += 1
        word_ = "_" * len(word)
        print("!Guess the Word!")
        while True:
            print(displayaddspaces(word_, len(word_)))
            print(list_of_guessed_letters)
            if word == word_:
                print("You Won!")
                userchoice = raw_input("Play Again? ")
                del list_of_guessed_letters[:]
                break
            else:
                letter = getuserguess()
                if letter in word:
                    word_ = searchword(letter, word, word_)
                else:
                    print("Letter not found.")
    elif userchoice == "no":
        break
    else:
        userchoice = raw_input("Invalid option. Please enter yes or no.")

print("Goodbye")

