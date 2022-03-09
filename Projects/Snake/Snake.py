import pygame       #Imports the gane
pygame.init()       #Starts the game
dis=pygame.display.set_mode((400,300))      #creates the display

pygame.display.update()     #Updates the display

pygame.display.set_caption('Snake game by Canto')     #Adds to the display

black=(0,0,0)       #Makes the original blue into black
red=(255,0,0)       #Sets the color

game_over=False         #If the game is over the gfame will end, if not it will continue
while not game_over:
    for event in pygame.event.get():    
        if event.type==pygame.QUIT:
            game_over=True              #if the game is over the game will quit
        pygame.draw.rect(dis,blue,[200,150,10,10])  #displays the blue rectangle
    pygame.display.update()     #Updates display
 
pygame.quit()       #Depending on "game_over" the game will end
quit()          #The game will quit