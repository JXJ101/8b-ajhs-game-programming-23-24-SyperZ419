# Hangman Game By Xavier Oliver, v0.8
import random
#words = 'cat heat fold paper freeze keys light gate ham corn fiend utopia twilight sporange potato dystopia falcon raptor fossilized permeate pragmatic cornucopia pneumonoultramicroscopicsilicovolcanoconiosis hippopotomonstrosesquippedaliophobia honorificabilitudinitatibus floccinaucinihilipilification incomprehensible sigma mitochondrion agglutinative variable volcanic metamorphic'.split()
# DICTIONARY VERSION
# Stored in Key:Value Pairs
# Actual Dictionary Word (Key) : Value (Definition)
# Uses {} to specify a dictionary
words = {'Colors': 'blue green orange fuschia indigo black white maroon sanguine gold'.split(),
         'Animals': 'monkey dragon pangolin giraffe scorpion hamster scarab starfish octopus shrimp'.split(),
         'Shapes': 'triangle square rhombus trapezoid diamond rectangle oval dodecahedron hexagon octogon'.split(),
         'Foods': 'waffle potato calamari escargot haggis popsicle chocolate nachos steak watermelon'.split()}

# VARIABLE NAMES in ALL-CAPS ARE CONSTANTS AND NOT MEANT TO CHANGE!
HANGMAN_BOARD = ['''
    +---+
        |
        |
        |
     =======''', '''   
    +---+
    O   |
        |
        |
     =======''', '''
    +---+
    O   |
    |   |
        |
     =======''', '''
    +---+
    O   |
   /|   |
        |
     =======''', '''
    +---+
    O   |
   /|\  |
        |
     =======''', '''            
    +---+
    O   |
   /|\  |
   /    |
     =======''', '''           
    +---+
    O   |
   /|\  |
   / \  |
     =======''']
                   
# Pick Word from List
def getRandomWord(wordList): # Return a random word from the list.
    wordIndex = random.randint(0, len(wordList) - 1 )
    # len(listname) - 1 is  EXTREMELY COMMON WHEN WORKING WITH LISTS.
    return wordList[wordIndex]

# Pick Word from Dictionary
def getRandomWord(wordDict): # Return a random word from the list.
    wordKey = random.choice(list(wordDict.keys()))
    wordIndex = random.randint(0, len(wordDict[wordKey] - 1))
    return [wordDict[wordKey]

def displayBoard(missedLetters, correctLetters, secretWord):
    print(HANGMAN_BOARD[len(missedLetters)])
    print()

    print('Missed Letters:', end = ' ')
    for eachLetter in missedLetters:
        print(eachLetter, end = ' ')
    print()
    
    blanks = '_' * len(secretWord)
    
    # Replace Blanks with Correct Letters
    for i in range(len(secretWord)):
        if secretWord[i] in correctLetters:
            blanks = blanks[:i] + secretWord[i] + blanks[i+1:]

    for letter in blanks:
        print(letter, end = ' ')
    print()


def getGuess(alreadyGuessed):
    while True:
        print('Please guess a letter, then hit ENTER')
        guess = input()
        guess = guess.lower()
        if len(guess) != 1:
            print('Please enter only one letter.')
        elif guess in alreadyGuessed:
            print('You have already guessed this letter. Please guess a different letter.')
        elif guess not in 'abcdefghijklmnopqrstuvwxyz':
            print('Please guess a LETTER.')
        else:
            return guess
        
def playAgain():
    print('How about another game? Yes or No.')
    return input().lower().startswith('y')

# Introduce the Game
print('Welcome to Hangman')
missedLetters = ''
correctLetters = ''
secretWord = getRandomWord(words)
gameIsDone = False

# Main Game Loop
while True:
    displayBoard(missedLetters, correctLetters, secretWord)

    guess = getGuess(missedLetters + correctLetters)

    if guess in secretWord:
        correctLetters = correctLetters + guess

        # Check to See If Winner
        foundAllLetters = True
        for i in range(len(secretWord)):
            if secretWord[i] not in correctLetters:
                foundAllLetters = False
                break
        if foundAllLetters:
            print('Victory has been attained.')
            print('This was the secret word: ' + secretWord)
            gameIsDone = True
    else:
        missedLetters = missedLetters + guess

        if len(missedLetters) == len(HANGMAN_BOARD) - 1:
            displayBoard(missedLetters, correctLetters, secretWord)
            print('You have run out of guesses and lost the game.')
            print('You made this number of correct guesses ' + str(len(correctLetters)))
            print('This was the secret word: ' + secretWord)
            gameIsDone = True

    if gameIsDone:
        if playAgain():
            missedLetters = ''
            correctLetters = ''
            gameIsDone = False
            secretWord = getRandomWord(words)
        else:
            break





# i = 0
# while i < 50 :
#     word = getRandomWord(words)
#     print(word)
#     i += 1
