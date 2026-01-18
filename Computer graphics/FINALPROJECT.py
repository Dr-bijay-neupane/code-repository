import pygame
import sys

pygame.init()

w, h = 800, 600
screen = pygame.display.set_mode((w, h))

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

def BLA(x1, y1, x2, y2):
    dx = abs(x2 - x1)
    dy = abs(y2 - y1)

    lx = 1 if x2 > x1 else -1
    ly = 1 if y2 > y1 else -1

    x = x1
    y = y1

    screen.set_at((x, y), WHITE)

    if dx > dy:
        pk = 2 * dy - dx
        for i in range(dx):
            if pk < 0:
                x += lx
                pk += 2 * dy
            else:
                x += lx
                y += ly
                pk += 2 * dy - 2 * dx
            screen.set_at((x, y), WHITE)
    else:
        pk = 2 * dx - dy
        for i in range(dy):
            if pk < 0:
                y += ly
                pk += 2 * dx
            else:
                x += lx
                y += ly
                pk += 2 * dx - 2 * dy
            screen.set_at((x, y), WHITE)

def main():
    x1 = 355
    y1 = 210
    x2 = 355
    y2 = 390

    last_move = pygame.time.get_ticks()

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        current_time = pygame.time.get_ticks()

        if current_time - last_move >= 10:
            x1 += 1
            x2 += 1
            last_move = current_time

        screen.fill(BLACK)
        BLA(x1, y1, x2, y2)

        pygame.display.update()

if __name__ == "__main__":
    main()
