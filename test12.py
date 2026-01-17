import pygame
import sys

pygame.init()

white = (255, 255, 255)
black = (0, 0, 0)

w, h = (800, 600)
screen = pygame.display.set_mode((w, h))

def main():
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        screen.fill(black)
        screen.set_at((300, 300), white)

        pygame.display.flip()

if __name__ == "__main__":
    main()
