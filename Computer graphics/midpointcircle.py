def midpoint_circle(xc, yc, r):
    x = 0
    y = r
    p = 1 - r  

    while x <= y:
        
        print(xc + x, yc + y)
        print(xc - x, yc + y)
        print(xc + x, yc - y)
        print(xc - x, yc - y)
        print(xc + y, yc + x)
        print(xc - y, yc + x)
        print(xc + y, yc - x)
        print(xc - y, yc - x)

        x += 1
        if p < 0:
            p += 2 * x + 1
        else:
            y -= 1
            p += 2 * (x - y) + 1



a = int(input("ENTER THE X-axis of CENTRE: "))
b = int(input("ENTER THE Y-axis of CENTRE: "))
c = int(input("ENTER the radius of circle: "))

midpoint_circle(a, b, c)
