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