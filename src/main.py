import pygame
import sys

pygame.init()

clock = pygame.time.Clock()

screen = pygame.display.set_mode((800,600))
pygame.display.set_caption('my game')

run = True

while run:
    screen.fill((0,0,0))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
    
    pygame.display.update()
    clock.tick(60)
