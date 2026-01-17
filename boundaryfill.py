import pygame
import sys

pygame.init()
WIDTH, HEIGHT = 600, 400
screen = pygame.display.set_mode((WIDTH, HEIGHT))

BLACK = (0, 0, 0)
BLUE = (0, 0, 255)
GREEN = (0, 255, 0)

screen.fill(BLACK)
pygame.draw.rect(screen, BLUE, (150, 100, 300, 200))

def flood_fill(x, y, old_color, new_color):
    if x < 0 or x >= WIDTH or y < 0 or y >= HEIGHT:
        return

    current = screen.get_at((x, y))[:3]

    if current == old_color and current != new_color:
        screen.set_at((x, y), new_color)

        flood_fill(x + 1, y, old_color, new_color)
        flood_fill(x - 1, y, old_color, new_color)
        flood_fill(x, y + 1, old_color, new_color)
        flood_fill(x, y - 1, old_color, new_color)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        if event.type == pygame.MOUSEBUTTONDOWN:
            mx, my = event.pos
            flood_fill(mx, my, BLUE, GREEN)

    pygame.display.flip()
