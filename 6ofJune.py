import pygame
import numpy as np

pygame.init()

# Screen size
width, height = 800, 800
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Game of Life")

# Grid settings
cell_size = 20  # Size of each grid cell
rows = height // cell_size
cols = width // cell_size

# Colors
black = (0, 0, 0)
white = (255, 255, 255)
gray = (200, 200, 200)

def draw_grid(surface):
    for row in range(rows):
        for col in range(cols):
            rect = pygame.Rect(col * cell_size, row * cell_size, cell_size, cell_size)
            pygame.draw.rect(surface, gray, rect, 1)  


running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

 
    screen.fill(black)
    
    draw_grid(screen)
    
    pygame.display.flip()

pygame.quit()