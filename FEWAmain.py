import pygame, math, random, time
from pygame.locals import *

#Main loading screen

pygame.init()

#Initalize Main Screen
screen_width=1024
screen_height=600
screen=pygame.display.set_mode([screen_width,screen_height])
pygame.display.set_caption('FEWAP')

#Color the screen
background = pygame.Surface(screen.get_size())
background = background.convert()
background.fill((250, 250, 250))

#Display main text
font = pygame.font.Font(None, 36)
text = font.render("Welcome to FEWA!", 1 , (10, 10, 10))
textpos = text.get_rect()
textpos.centerx = background.get_rect().centerx
background.blit(text, textpos)

#Blit it to the screen
screen.blit(background, (0, 0))
pygame.display.flip()

#Play music
pygame.mixer.music.load('FEWA.ogg')
pygame.mixer.music.play(-1, 0.0)

#Loop time
while 1:
    for event in pygame.event.get():
        if event.type == QUIT:
            quit()

    screen.blit(background, (0, 0))
    pygame.display.flip()


if __name__ == '__main__': main()
