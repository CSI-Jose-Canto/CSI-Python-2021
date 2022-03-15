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

dis_width = 800     #sets the size 
dis_height  = 600 
dis = pygame.display.set_mode((800, 600))       #sets the display's mode
pygame.display.set_caption('Snake Game by Canto')     #Adds to the display
 
game_over = False       #states the game_over as false so that the code continues
 
x1 = dis_width/2        #Changes the start of the snake
y1 = dis_height/2   
 
snake_block=10 #size of snake block

x1_change = 0       #holds the change in x
y1_change = 0       #holds the change in y
 
clock = pygame.time.Clock()
snake_speed=30          #sets speed of snack

font_style = pygame.font.SysFont(None, 50)  #Sets the font for the game
 
def message(msg,color):             #defines "message" with the ms and its color.
    mesg = font_style.render(msg, True, color)
    dis.blit(mesg, [dis_width/2, dis_height/2])
 
while not game_over:
    for event in pygame.event.get():        #This loop will "read" the comands made by the user such as up down...
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
    if x1 >= dis_width or x1 < 0 or y1 >= dis_height or y1 < 0:
        game_over = True
 
    x1 += x1_change
    y1 += y1_change
    dis.fill(white)
    pygame.draw.rect(dis, black, [x1, y1, 10, 10])      #this will make the snake
 
    pygame.display.update()     #updates display
 
    clock.tick(30)          #It will compute how many milliseconds have passed since the previous call

message("You lost",red)
pygame.display.update()
time.sleep(2)
 
pygame.quit()
quit()