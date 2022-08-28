import pygame

#initialise pygame
pygame.init()

#create a display surface - i.e. the window the player is going to see
screen = pygame.display.set_mode((800,400))


while True:

    #check for player's input (i.e. the event loop)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()

    # draw all of our elements
    # update everything
    pygame.display.update()

