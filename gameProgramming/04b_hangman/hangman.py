# Hangman Game By Xavier Oliver, v0.3
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

i = 0
while i < 50 :
    word = getRandomWord(words)
    print(word)
    i += 1
