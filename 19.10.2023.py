def f(x, y, h):
    if h == 2 and (x + y) <= 20:
        return 1
    if h == 2 and (x + y) > 20:
        return 0
    if h < 2 and (x + y) > 20:
        if x % 2 == 0 and y % 2 == 0:
            return f(x, y / 2, h + 1) or f(x, y - 1, h + 1) or f(x / 2, y, h + 1) or f(x + 1, y, h + 1)
        if x % 2 == 1 and y % 2 == 0:
            return f(x, y / 2, h + 1) or f(x, y - 1, h + 1) or f(x + 1, y, h + 1)
        if x % 2 == 0 and y % 2 == 1:
            return f(x, y - 1, h + 1) or f(x / 2, y, h + 1) or f(x + 1, y, h + 1)
        if x % 1 == 1 and y % 2 == 1:
            return f(x, y - 1, h + 1) or f(x + 1, y, h + 1)



for i in range(11, 100):
    if f(10, i, 1) == 1:
        print(i)