import random

print("Welcome to Hang Man!")

wordList = ["Celtics", "Bulls", "Cavs", "Bucks", "Mavericks", "Warriors", "Lakers", "Spurs", "Sixers", "Clippers", "Pistons", "Kings", "Nuggets", "Timber Wolves", "Suns", "Nets", "Rockets", "Heat", "Jazz", "Hawks"]
computerChoice = random.choice(wordList)
print(f"Computer selected: {computerChoice}")

(len(computerChoice)*"_ ")

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