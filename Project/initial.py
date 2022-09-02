import pygame
from sys import exit #to close any part of the code (similar to break statement but better)

#initialise pygame
pygame.init()

#create a display surface - i.e. the window the player is going to see
screen = pygame.display.set_mode((800,400))
pygame.display.set_caption('Runner')

#Create font
test_font = pygame.font.Font('font/Pixeltype.ttf', 50) #2 arguments - font type, font size

#creating a clock object - helps us with time and framerates
clock = pygame.time.Clock()

#Creating a surface of just plain colour
sky_surface = pygame.image.load('graphics/Sky.png').convert()
ground_surface = pygame.image.load('graphics/ground.png').convert()
text_surface = test_font.render('My game', False, 'Black') #3 arguments - text info, whether you want to anti-aliase it, and colour
#anti-aliasing means you're smoothing the edges of the text

#import snail image
snail_surface = pygame.image.load('graphics/snail/snail1.png').convert_alpha()
snail_rect = snail_surface.get_rect(bottomright = (600, 300))

player_surface = pygame.image.load('graphics/player/player_walk_1.png').convert_alpha()
player_rect = player_surface.get_rect(midbottom = (80, 300))

mouse_pos = pygame.mouse.get_pos() #get the mouse position

while True:

    #check for player's input (i.e. the event loop)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
        
        #gives us the mouse position (this would only trigger if we move the mouse)
        # if event.type == pygame.MOUSEMOTION:
        #     print(event.pos)

        #checking if the mouse collides with the player rectangle 
        

    #attach sky_surface to display surface
    screen.blit(sky_surface, (0, 0)) #calling the display surface itself (blit = block image transfer - i.e. 
    #putting 1 surface on another surface). surface = sky_surface, position = c(0,0)

    #attach ground_surface to display surface
    screen.blit(ground_surface, (0, 300))

    screen.blit(text_surface, (300, 50))
    
    snail_rect.right -= 4
    screen.blit(snail_surface, snail_rect)

    if snail_rect.right <= 0:
        snail_rect.left = 800

    player_rect.left += 1
    screen.blit(player_surface, player_rect)

    # if player_rect.colliderect(snail_rect):
    #     print('collision')

    #collidepoint with mouse
    
    if player_rect.collidepoint(mouse_pos):
        print(pygame.mouse.get_pressed())



    pygame.display.update()
    clock.tick(60) #60 tells Python that the while True loop should not run faster than 60 times per second - i.e. setting
    #the maximum framerate


#Controlling the frame rate (i.e. how fast the game runs)

#our animation speed depends on how fast we're updating the game. 

