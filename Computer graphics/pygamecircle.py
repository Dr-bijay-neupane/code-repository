import pygame
import sys

pygame.init()

w, h = 800, 600
screen = pygame.display.set_mode((w, h))
pygame.display.set_caption("Midpoint Circle Algorithm")

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

def midpoint_circle(xc, yc, r):
    x = 0
    y = r
    p = 1 - r

    while x <= y:
        # 8 symmetric points
        screen.set_at((xc + x, yc + y), WHITE)
        screen.set_at((xc - x, yc + y), WHITE)
        screen.set_at((xc + x, yc - y), WHITE)
        screen.set_at((xc - x, yc - y), WHITE)
        screen.set_at((xc + y, yc + x), WHITE)
        screen.set_at((xc - y, yc + x), WHITE)
        screen.set_at((xc + y, yc - x), WHITE)
        screen.set_at((xc - y, yc - x), WHITE)

        x += 1
        if p < 0:
            p += 2 * x + 1
        else:
            y -= 1
            p += 2 * (x - y) + 1

def semi_circle(xc, yc, r):
    x = 0
    y = r
    p = 1 - r

    while x <= y:
        
        screen.set_at((xc + x, yc + y), WHITE)
        screen.set_at((xc + y, yc + x), WHITE)
        screen.set_at((xc - x, yc + y), WHITE)
        screen.set_at((xc - y, yc + x), WHITE)
 

        x += 1
        if p < 0:
            p += 2 * x + 1
        else:
            y -= 1
            p += 2 * (x - y) + 1


def main():


    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
                \
        screen.fill(BLACK)  
        midpoint_circle(300, 300, 100)
        midpoint_circle(250,270, 20) 
        midpoint_circle(350,270 , 20) 
        semi_circle(300, 315, 50)
        pygame.display.flip()


if __name__ == "__main__":
    main()
