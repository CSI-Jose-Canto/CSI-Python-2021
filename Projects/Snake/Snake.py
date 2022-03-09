# import pygame       #Imports the gane
# pygame.init()       #Starts the game
# dis=pygame.display.set_mode((400,300))      #creates the display

# pygame.display.update()     #Updates the display

# pygame.display.set_caption('Snake game by Canto')     #Adds to the display

# black=(0,0,0)       #Makes the original blue into black
# red=(255,0,0)       #Sets the color

# game_over=False         #If the game is over the gfame will end, if not it will continue
# while not game_over:
#     for event in pygame.event.get():    
#         if event.type==pygame.QUIT:
#             game_over=True              #if the game is over the game will quit
#         pygame.draw.rect(dis,black,[200,150,10,10])  #displays the blue rectangle
#     pygame.display.update()     #Updates display
 
# pygame.quit()       #Depending on "game_over" the game will end
# quit()          #The game will quit

import pygame   #imports the game
 
pygame.init()      #Starts game
 
white = (255, 255, 255)     #Sets the colors
black = (0, 0, 0)
red = (255, 0, 0)
 
dis = pygame.display.set_mode((800, 600))       #sets the display's mode
pygame.display.set_caption('Snake Game by Canto')     #Adds to the display
 
game_over = False       #states the game_over as false so that the code continues
 
x1 = 300
y1 = 300
 
x1_change = 0       #holds the change in x
y1_change = 0       #holds the change in y
 
clock = pygame.time.Clock()
 
while not game_over:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_over = True
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                x1_change = -10
                y1_change = 0
            elif event.key == pygame.K_RIGHT:
                x1_change = 10
                y1_change = 0
            elif event.key == pygame.K_UP:
                y1_change = -10
                x1_change = 0
            elif event.key == pygame.K_DOWN:
                y1_change = 10
                x1_change = 0
 
    x1 += x1_change
    y1 += y1_change
    dis.fill(white)
    pygame.draw.rect(dis, black, [x1, y1, 10, 10])
 
    pygame.display.update()
 
    clock.tick(30)
 
pygame.quit()
quit()