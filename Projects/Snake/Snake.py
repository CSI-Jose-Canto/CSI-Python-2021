import pygame       #Imports the gane
pygame.init()       #Starts the game
dis=pygame.display.set_mode((400,300))      #creates the display
pygame.display.update()     #Updates the display
pygame.display.set_caption('Snake game by Edureka')     #Adds to the display
game_over=False         #If the game is over the gfame will end, if not it will continue
while not game_over:
    for event in pygame.event.get():
        print(event)   #prints out all the actions that take place on the screen
 
pygame.quit()       #Depending on "game_over" the game will end
quit()          #The game will quit