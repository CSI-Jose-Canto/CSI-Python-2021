import random

print("Welcome to Hang Man!")

wordList = ["CELTICS", "BULLS", "CAVS", "BUCKS", "MAVERICKS", "WARRIORS", "LAKERS", "SPURS", "SIXERS", "CLIPPERS", "PISTONS", "KINGS", "NUGGETS", "HEAT", "SUNS", "NETS", "ROCKETS", "THUNDER", "JAZZ", "HAWKS"]
computerChoice = random.choice(wordList)

print("Computer selected: " + computerChoice)
print(len(computerChoice)*"_ ")

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

posibleLetters = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", 'X', "Y", "Z"]

def getInput():
     Letter = input("Choose Letter")
     while(Letter.upper() not in posibleLetters):
        print("Error")
        Letter = input("Choose Letter")        
     return Letter

print(getInput())

# def printWord(...)
#      Temp: Str=""
#      len(word)
#      for[Letter in word]

#      for(incorrect)
     
