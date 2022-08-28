import pygame
from sys import exit #to close any part of the code (similar to break statement but better)

#initialise pygame
pygame.init()

#create a display surface - i.e. the window the player is going to see
screen = pygame.display.set_mode((800,400))
pygame.display.set_caption('Runner')

#creating a clock object - helps us with time and framerates
clock = pygame.time.Clock()

#Creating a surface of just plain colour
test_surface = pygame.Surface((100, 200))
test_surface.fill('Blue')

while True:

    #check for player's input (i.e. the event loop)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

    #attach test_surface to display surface
    screen.blit(test_surface, (200, 100)) #calling the display surface itself (blit = block image transfer - i.e. 
    #putting 1 surface on another surface). surface = test_surface, position = c(0,0)

    pygame.display.update()
    clock.tick(60) #60 tells Python that the while True loop should not run faster than 60 times per second - i.e. setting
    #the maximum framerate


#Controlling the frame rate (i.e. how fast the game runs)

#our animation speed depends on how fast we're updating the game. 

