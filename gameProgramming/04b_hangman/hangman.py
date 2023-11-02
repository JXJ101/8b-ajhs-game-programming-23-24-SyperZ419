# Hangman Game By Xavier Oliver, v0.7
import random
words = 'cat heat fold paper freeze keys light gate ham corn fiend utopia twilight sporange potato dystopia falcon raptor fossilized permeate pragmatic cornucopia pneumonoultramicroscopicsilicovolcanoconiosis hippopotomonstrosesquippedaliophobia honorificabilitudinitatibus floccinaucinihilipilification incomprehensible sigma mitochondrion agglutinative variable volcanic metamorphic'.split()

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





# i = 0
# while i < 50 :
#     word = getRandomWord(words)
#     print(word)
#     i += 1
