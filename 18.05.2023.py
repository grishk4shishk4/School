'''
counter = 1
def x(a):
    global counter
    a = 1/(1 - a)
    if counter <= 300:
        counter += 1
        print(counter, a)
        return x(a)
print(x(-1))
'''
'''
for i in range(1, 150):
    if (1111/i) % 1 == 0:
        print(i, 1111/i)
'''
'''
import sys
sys.setrecursionlimit(3000**2)

#3000 = 70
counter = 0
x1 = int(input('x'))
y1 = int(input('y'))

# c_list = [[[''] * 3000]]
# for i in range(3000):
#     for u in range(70):
#         c_list(i)(u) = 0
def a(x, y):
    global counter
    if x == x1 or y == y1 and counter > 0:
        print(counter)
    counter += 1
    # if x == 0:
    #     print(f'{x, y} - ошибка')

    print(counter)
    if x - 1 > 0:
        if y - 1 > 0:
            x -= 1
            y -= 1
#            print(f'x{x}, y{y}')
            a(x, y)
        else:
            y = 70
#            print(f'x{x}, y{y}')
            a(x, y)
    else:
        x = 3000
#        print(f'x{x}, y{y}')
        a(x, y)


a(x1, y1)
'''
a = 0
summ = 1
while 3000 % summ != 0:
    if summ + 71 > 3000:
        summ = summ - 3000
        a += 1
    else:
        summ += 71
        a += 1
print()