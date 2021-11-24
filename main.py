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
from pygame.locals import K_LEFT, K_RIGHT, K_UP, K_DOWN
from pygame.locals import K_w, K_a, K_s, K_d, K_q, K_z
from pygame.locals import CONTROLLER_BUTTON_DPAD_LEFT, CONTROLLER_BUTTON_DPAD_RIGHT, CONTROLLER_BUTTON_DPAD_UP, CONTROLLER_BUTTON_DPAD_DOWN
from sys import exit

# ---- general properties ----
# screen propertiees
SCREEN_WIDTH = 852
SCREEN_HEIGHT = 480

# variables to be used through the program

vec = pygame.math.Vector2
FRIC = 0.20
FPS = 60
FPS_CLOCK = pygame.time.Clock()

ENLARGE = 8

# ---- character selection ----
characters = {1: "Caz",
              2: "Gabriel",
              3: "Nina",
              4: "Roberto",
              5: "Senne"}

iteration = 0
for character in characters.values():
    iteration += 1
    print(f"{iteration}. {character}")

print("You can choose by typing the character name or the number")
chosen_character = input("Choose you character: ")

try:
    if int(chosen_character) in characters.keys():
        chosen_character = characters[int(chosen_character)].lower()
except ValueError:
    if chosen_character.capitalize() in characters.values():
        chosen_character.lower()

# ---- initiating ----
pygame.init()

# windows properties
pygame.display.set_icon(pygame.image.load("src/logo.png"))
pygame.display.set_caption("Five nights at Senne", "Five nights at Senne")
screen = pygame.display.set_mode(size=(SCREEN_WIDTH, SCREEN_HEIGHT),
                                 flags=pygame.RESIZABLE)
screen.fill((255, 248, 220))


# ---- classes ----
class Background(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.bgimage = pygame.image.load("src/background.png")

        self.bgX = 0
        self.bgY = 0

    def render(self):
        screen.blit(self.bgimage, (self.bgX, self.bgY))


class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load(f"src/{chosen_character}.png")
        self.image.convert_alpha()
        self.size = self.image.get_size()  # getting image size

        # scaling the image
        self.image = pygame.transform.scale(self.image,
                                            (int(self.size[0] * ENLARGE),
                                             int(self.size[1] * ENLARGE)))

        self.rect = self.image.get_rect()  # giving player a hitbox

        # position and direction
        self.pos = vec((340, 240))  # position
        self.vel = vec(0, 0)  # velocity
        self.acc = vec(0, 0)  # acceleration
        self.direction = "RIGHT"  # where the character is facing

    def move(self):
        # Returns the current key presses
        pressed_keys = pygame.key.get_pressed()

        # ---- movement ----
        # keypresses
        left_axis = pressed_keys[K_LEFT] or pressed_keys[K_a] or pressed_keys[K_q] or pressed_keys[CONTROLLER_BUTTON_DPAD_LEFT]
        right_axis = pressed_keys[K_RIGHT] or pressed_keys[K_d] or pressed_keys[CONTROLLER_BUTTON_DPAD_RIGHT]

        up_axis = pressed_keys[K_UP] or pressed_keys[K_w] or pressed_keys[K_z] or pressed_keys[CONTROLLER_BUTTON_DPAD_UP]
        down_axis = pressed_keys[K_DOWN] or pressed_keys[K_s] or pressed_keys[CONTROLLER_BUTTON_DPAD_DOWN]

        self.acc = vec(int(right_axis) - int(left_axis),
                       int(down_axis) - int(up_axis))

        # normalizing the acceleration only when it's not 0
        if self.acc.length() != 0:
            self.acc.normalize()

        # physics
        self.acc -= self.vel * FRIC
        self.vel += self.acc
        self.pos += self.vel + 0.5 * self.acc

        # warping player
        if self.pos.x > SCREEN_WIDTH:
            self.pos.x = 0
        if self.pos.x < 0:
            self.pos.x = SCREEN_WIDTH
        if self.pos.y > SCREEN_HEIGHT:
            self.pos.y = 0
        if self.pos.y < 0:
            self.pos.y = SCREEN_HEIGHT

        self.rect.midbottom = self.pos  # Update rect with new pos

    def update(self):
        pass

    def attack(self):
        pass


# creating the objects
background = Background()
player = Player()

# ---- game state ----
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

            # changing dimensions of game area when resizing window
            SCREEN_HEIGHT = event.h
            SCREEN_WIDTH = event.w

        # making the program exitable
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

        # For events that occur upon clicking the mouse (left click)
        if event.type == pygame.MOUSEBUTTONDOWN:
            pass

        # Event handling for a range of different key presses
        if event.type == pygame.KEYDOWN:
            pass

    # ---- rendering ----
    background.render()
    player.move()

    screen.blit(player.image, player.rect)

    pygame.display.update()
