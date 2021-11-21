# ░░░░░░░▐█▀█▄░░░░░░░░░░▄█▀█▌
# ░░░░░░░█▐▓░█▄░░░░░░░▄█▀▄▓▐█
# ░░░░░░░█▐▓▓░████▄▄▄█▀▄▓▓▓▌█
# ░░░░░▄█▌▀▄▓▓▄▄▄▄▀▀▀▄▓▓▓▓▓▌█
# ░░░▄█▀▀▄▓█▓▓▓▓▓▓▓▓▓▓▓▓▀░▓▌█
# ░░█▀▄▓▓▓███▓▓▓███▓▓▓▄░░▄▓▐█▌
# ░█▌▓▓▓▀▀▓▓▓▓███▓▓▓▓▓▓▓▄▀▓▓▐█
# ▐█▐██▐░▄▓▓▓▓▓▀▄░▀▓▓▓▓▓▓▓▓▓▌█▌
# █▌███▓▓▓▓▓▓▓▓▐░░▄▓▓███▓▓▓▄▀▐█
# █▐█▓▀░░▀▓▓▓▓▓▓▓▓▓██████▓▓▓▓▐█▌
# ▓▄▌▀░▀░▐▀█▄▓▓██████████▓▓▓▌█
# Coded by Shiba https://shiba.house
# Artwork by https://www.instagram.com/gabriel_bastens/
# Sound design & music by https://www.instagram.com/nina.casteleyn/
# Story script by https://www.instagram.com/caz.arteel/

import pygame
from sys import exit

# ---- general properties ----
# screen propertiees
SCREEN_WIDTH = 852
SCREEN_HEIGHT = 480


# initiating 
pygame.init()

# windows properties
# pygame.display.set_icon(pygame.image.load("logo.png"))
pygame.display.set_caption("Five nights at Senne")
screen = pygame.display.set_mode(size=(SCREEN_WIDTH, SCREEN_HEIGHT), flags=pygame.RESIZABLE)
screen.fill((255, 248, 220))

# game state
game_over = False

# ---- game loop ----
while not game_over:
    # ---- events ----
    for event in pygame.event.get():
        # only do something if the event is of type QUIT
        if event.type == pygame.QUIT:
            # change the value to False, to exit the main loop
            running = False

        # resize window
        if event.type == pygame.VIDEORESIZE:
                # There's some code to add back window content here.
                surface = pygame.display.set_mode((event.w, event.h),
                                                pygame.RESIZABLE)
        
        # making the program exitable
        if event.type == pygame.QUIT:
                pygame.quit()
                exit()
    




    pygame.display.update()
    