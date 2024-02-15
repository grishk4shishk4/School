def f(x, y, h):
    if 107 < (x + y) < 170 and h == 2:
        return 1
    if 107 < (x + y) < 170 and h < 2:
        return 0
    if (x + y) < 107 and h == 2 or (x + y) > 170 and h == 2:
        return 0
