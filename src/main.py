import pygame
import sys
import random as rand
from dice import Dice

pygame.init()

clock = pygame.time.Clock()

screen = pygame.display.set_mode((1280,720))
pygame.display.set_caption('my game')
run = True

dice = pygame.sprite.Group()
dice.add(Dice('white', 500, 300))



while run:
    screen.fill('dark green')
    dice.update()
    dice.draw(screen)
    print(dice)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    
    
    pygame.display.update()
    clock.tick(60)
