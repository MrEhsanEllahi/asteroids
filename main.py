# this allows us to use code from
# the open-source pygame library
# throughout this file
import pygame 
from player import Player
from constants import *

def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    Clock = pygame.time.Clock()
    dt = 0 #delta time
    player  = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2) #create player object
    while True:
        screen.fill((0,0,0)) # Fill the screen with black
        player.draw(screen)
        pygame.display.flip()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        dt = Clock.tick(60) / 1000 #time passed since last frame in seconds
        player.update(dt)

if __name__ == "__main__": #if this file is being run directly
    main()