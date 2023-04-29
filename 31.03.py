'''
for N in range(9999, 1000, -1):
    summ = []
    for u in range(3):
        print(N)
        summ.append(int(str(N[u]) + (str(N[u + 1]))))
'''
'''
numbers = [2, 3]
end = int(input())

for i in range(5, end, 2):
    counter = 0
    for u in numbers:
        if i % u == 0:
            counter = 1
            break
    if counter == 0:
        numbers.append(i)
print(numbers)
print(len(numbers))
'''
'''
import random
a = []
for i in range(5):
    a.append(random.randint(-10, 10))

print(a)


'''
'''
for i in range(5):
    for u in range(i, 5):
        if a[i] > a[u]:
            a[i], a[u] = a[u], a[i]
print(a)
'''

'''
for i in range(5):
    for i in range(4):
        if a[i] > a[i + 1]:
            a[i], a[i + 1] = a[i + 1], a[i]
            print(a[i], a[i + 1])
        print(i, a)
print(a)

'''
'''
a = '7' * 2022
while ('777' in a) or ('333' in a):
    a = a.replace('777', '3', 1)
    a = a.replace("333", '7', 1)
print(a)
'''
'''
for x in range(2):
    for y in range(2):
        for z in range(2):
            for w in range(2):
                if not((x <= y) and ((not x) <= (not z)) or
                       w):
                    print(x, y, z, w)

'''
'''
for n in range(1, 1000):
    a = str(bin(n))
    a = a[2]
    print(n)

    if n % 2 == 1:
        a += '11'
    else:
        a += '10'

    if ('1' in a) % 2 == 1:
        a += '0'
    else:
        a += '1'

    R = int(a)
    if R > 53:
        break
print(R)

'''
'''
# +1 +4 *5
# 1 - 62

def f(h, x):
    if h == 3 and x >= 63:
        return 1
    elif h == 3 and x < 63:
        return 0
    elif h >= 3 and x >= 63:
        return 0
    else:
        if h % 2 == 0:
            return f(h+1, x+1) or f(h+1, x+4) or f(h+1, x*5)
        else:
            return f(h+1, x+1) or f(h+1, x+4) or f(h+1, x+5)

for i in range(1, 63):
    if f(1, i) == 1:
        print(i)
        break
'''

import random

n = 7
l = [[0] * n for i in range(n)]
for i in range(n):
    for u in range(n):
        if i == u - 1 or u == i - 1 and u % 2 == 1 or i % 2 == 1:
            l[i][u] = 1

        print(l[i][u], end=' ')
    print()

'''
1
        if i % 2 == 1:
            l[i][u] = 1
2
        if i == 0 or i == n - 1 or u == 0 or u == n - 1:
            l[i][u] = 1
3
        if i == 0 and u == n - 1 or i == n - 1 and u == n - 1 or i == 0 and u == 0 or i == n - 1 and u == 0:
            l[i][u] = 1
        if i > 0 and i <n - 1 and u > 0 and u < n - 1:
            l[i][u] = 1
4
        if (u + i) % 2 == 1:
            l[i][u] = 1
5
        if i % 2 == 0:
            l[i][u] = 1
        if (i + 1) % 4 != 0 and u == n - 1 or (i + 1) % 4 == 0 and u == 0:
            l[i][u] = 1
'''

