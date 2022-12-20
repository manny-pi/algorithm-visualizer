import pygame 
from pygame import Surface, time
from bar import Bar

pygame.init()

WINDOW_WIDTH = 1000
WINDOW_HEIGHT = 600
mainWindow = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
running = True
while running:
    for event in pygame.event.get(): 
        if event.type == pygame.QUIT:
            running = False
    
    pygame.display.flip()