import pygame
import sys

pygame.init()

w = 600
h = 500

screen = pygame.display.set_mode((w, h))

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

def DDA(x1, y1, x2, y2):
    dx = x2 - x1
    dy = y2 - y1

    if abs(dx) > abs(dy):
        steps = abs(dx)
    else:
        steps = abs(dy)

    xinc = dx / steps
    yinc = dy / steps

    x = x1
    y = y1

    for i in range(steps + 1):
        screen.set_at((round(x), round(y)), BLACK)
        x = x + xinc
        y = y + yinc

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    screen.fill(WHITE)

    DDA(300, 150, 400, 250)

    pygame.display.update()
