import pygame

pygame.init()

width = 800
height = 600
screen = pygame.display.set_mode((width, height))
clock = pygame.time.Clock()

x = 400
y = 100
radius = 15

vx = 3
vy = 0
gravity = 0.5
bounce = 0.8

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    vy += gravity
    x += vx
    y += vy

    if y + radius >= height:
        y = height - radius
        vy = -vy * bounce

    if x - radius <= 0 or x + radius >= width:
        vx = -vx

    screen.fill((0, 0, 0))
    pygame.draw.circle(screen, (255, 255, 255), (int(x), int(y)), radius)
    pygame.display.flip()

    clock.tick(60)

pygame.quit()
