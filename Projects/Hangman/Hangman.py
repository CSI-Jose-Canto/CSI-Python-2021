import random


HangManArt = [
"""
  _______
     |/      |
     |      (_)
     |      
     |       
     |      
     |
     |___
""",

"""
  _______
     |/      |
     |      (_)
     |       |
     |       |
     |      
     |
     |___
""",
"""
  _______
     |/      |
     |      (_)
     |      \|
     |       |
     |      
     |
     |___
""",
"""
  _______
     |/      |
     |      (_)
     |      \|/
     |       |
     |      
     |
     |___
""",
"""
  _______
     |/      |
     |      (_)
     |      \|/
     |       |
     |      / 
     |
     |___
""",
"""
  _______
     |/      |
     |      (_)
     |      \|/
     |       |
     |      / \\
     |
     |___
"""
]

words = ["CELTICS", "BULLS", "CAVS", "BUCKS", "MAVERICKS", "WARRIORS", "LAKERS", "SPURS", "SIXERS", "CLIPPERS", "PISTONS", "KINGS", "NUGGETS", "HEAT", "SUNS", "NETS", "ROCKETS", "THUNDER", "JAZZ", "HAWKS"]

def get_Word(wordList):
     # This function returns a random string from the list of strings.
     #In this case, the computer will choose a random NBA Team
     wordIndex = random.randint(0, len(wordList) - 1)
     return wordList[wordIndex]

def display(missedLetters, correctLetters, compWord):
     print(HangManArt[len(missedLetters)])
     print()

     print("Used letters:", end=" ")
     for letter in usedLetters:
         print(letter, end=' ')
     print()

     blanks = "_" * len(compWord)

     for i in range(len(compWord)): # Replace blanks with correctly guessed letters.
        if compWord[i] in correctLetters:
             blanks = blanks[:i] + compWord[i] + blanks[i+1:]

     for letter in blanks:          # Show the word with spaces in between each letter.
         print(letter, end=" ")
     print()

def getGuess(alreadyGuessed):
                                   # Returns the letter the player entered. This function makes sure the player entered a single letter and not something else.
     while True:
         print("Guess a letter.")
         guess = input()
         guess = guess.upper()
         if len(guess) != 1:
             print("Please enter ONE (1), letter.")
         elif guess in alreadyGuessed:
             print("You have already guessed that letter. Choose another one.")
         elif guess not in 'A B C D E F G H I J K L M N O P Q R S T U V W X Y Z':
             print("Please enter a LETTER, (in british accent) you donut.")
         else:
             return guess

def playAgain():
     # This function returns True if the player wants to play again; otherwise, it returns False.
     #If True then the game will start again, if False the game will end.
     print("Do you want to play again? (YES or NO)")
     return input().upper().startswith("Y")

print("Hang Man!!")
usedLetters = " "
correctLetters = " "
compWord = get_Word(words)
gameIsDone = False

while True:
     display(usedLetters, correctLetters, compWord)

     # This will let the player enter a letter, the letter is the imput.
     guess = getGuess(usedLetters + correctLetters)

     if guess in compWord:
         correctLetters = correctLetters + guess

         # This will check if the player has won.
         foundAllLetters = True
         for i in range(len(compWord)):
             if compWord[i] not in correctLetters:
                 foundAllLetters = False   #No se como hacer que print "Game Over"
                 break
         if foundAllLetters:
             print('CORRECT! The word is "' + compWord +
                   '"You have won!!')
             gameIsDone = True
     else:
         usedLetters = usedLetters + guess

         # Check if player has guessed too many times and lost.
         if len(usedLetters) == len(HangManArt) - 1:
             display(usedLetters, correctLetters, compWord)
             print("You ran out of guesses!\nAfter " +
                   str(len(usedLetters)) + "wrong guesses and " +
                   str(len(correctLetters)) + "correct guesses",
                   "the word was " + compWord + "")
             gameIsDone = True

     # Ask the player if they want to play again (but only if the game is done).
     if gameIsDone:
         if playAgain():
             usedLetters = ""
             correctLetters = ""
             gameIsDone = False
             compWord = get_Word(words)
         else:
            break