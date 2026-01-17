import test12
import sys

test12.init()

w, h = 800,600
screen = test12.display.set_mode((w, h))

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

def BLA(x1, y1, x2, y2):
    dx = abs(x2 - x1)
    dy = abs(y2 - y1)

    if x2 > x1:
        lx = 1
    else:
        lx = -1

    if y2 > y1:
        ly = 1
    else:
        ly = -1

    x = x1
    y = y1

    screen.set_at((x, y), WHITE)

    if dx > dy:
        pk = 2 * dy - dx

        for i in range(1,dx+1):
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

        for i in range(1,dy+1):
            if pk < 0:
                y += ly
                pk += 2 * dx
            else:
                x += lx
                y += ly
                pk += 2 * dx - 2 * dy

            screen.set_at((x, y), WHITE)

def main():
    while True:
        for event in test12.event.get():
            if event.type == test12.QUIT:
                test12.quit()
                sys.exit()

        screen.fill(BLACK)


        BLA(355, 210, 355, 390)
        BLA(445, 210, 445, 390)
        BLA(335, 250, 465, 250)
        BLA(335, 350, 465, 350)

        test12.display.update()


if __name__ == "__main__":
    main()
