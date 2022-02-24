from argparse import _AppendAction, _AppendConstAction
import random


steps = ["""
      _______
     |/      |
     |      
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
""",

]
wordList = ["CELTICS", "BULLS", "CAVS", "BUCKS", "MAVERICKS", "WARRIORS", "LAKERS", "SPURS", "SIXERS", "CLIPPERS", "PISTONS", "KINGS", "NUGGETS", "HEAT", "SUNS", "NETS", "ROCKETS", "THUNDER", "JAZZ", "HAWKS"]

def get_word():
     computerChoice = random.choice(wordList)
     return computerChoice.upper()

myWord = get_word()

posibleLetters = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", 'X', "Y", "Z"]

usedLetters = []

def getInput():
     Letter = input("Choose Letter")
     while(Letter.upper() not in posibleLetters):
        print("Error")
        Letter = input("Choose Letter")        
     return Letter

print("Welcome to Hang Man!")

print("Computer selected: " + myWord)
print(len(myWord)*"_ ")

def getGuess():
     while True:
          print('Guess a letter.')
          guess = input()
          guess = guess.upper()
          if len(guess) != 1:
            print('Please enter a single letter.')
          elif guess in usedLetters:
               print('You have already guessed that letter. Choose again.')
          elif guess not in 'A B C D E F G H I J K L M N O P Q R S T U V W X Y Z':
               print('Please enter a LETTER.')
          else:
               usedLetters.add(guess)
               return guess

def printWord(computerChoice):
     temp: str=""
     len(computerChoice)
     for Letter in myWord:
          if Letter in usedLetters:
               temp+=Letter
          else:
               temp+="_"

     print(temp)

# def play(computerChoice):
#    word_completion = "_ "* len(computerChoice)
#    print("Computer sslected: " + computerChoice)
#    guessed = False
#    guessed_letters = []
#    tries = 7
#    print(word_completion)
#    print("\n")
#    while not guessed and tries > 0:
#       guess = input("Guess the word:").upper()
#       if len(guess) == 1 and guess.isalpha():
#          if guess in guessed_letters:
#             print("already used that letter", guess)
#          elif guess not in computerChoice:
#             print(guess, "Not the word: (")
#             tries -= 1
#             guessed_letters.append(guess)
#          else:
#             print("CORRECT", guess, "the letter is in the word")
#             guessed_letters.append(guess)
#             word_as_list = list(word_completion)
#             indices = [i for i, letter in enumerate(computerChoice) if letter == guess]
#             for index in indices:
#                word_as_list[index] = guess
#             word_completion = "".join(word_as_list)
#             if "_" not in word_completion:
#                guessed = True
    

print(getInput())

# def printWord(...)
#      Temp: Str=""
#      len(word)
#      for[Letter in word]

#      for(incorrect)
     
