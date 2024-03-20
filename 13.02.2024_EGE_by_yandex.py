# # 2
# print(f'w x y z f1')
# for w in range(2):
#     for x in range(2):
#         for y in range(2):
#             for z in range(2):
#                 f1 = (((1 == w) == (not((w and x) or y))) <= z)
#                 if (((1 == w) == (not((w and x) or y))) <= z) == 1:
#                     print(w, x, y, z, f1)
# # x z y w


# # 5
# for i in range(10000):
#     N = bin(i)[2:]
#     if i % 2 == 0:
#         N += ('0' * N.count('0'))
#     else:
#         N = ('1' * N.count('1')) + N
#     R = int(N, 2)
#     if R > 2000:
#         print(i, N, R)
#         break


# К А Б И Н Е Т
# С Г С Г С Г С
# с - 4   г - 3


# 12
# c = 0
# for i in range(10000, 3, -1):
#     a = '8' + i * '4'
#     while '4444' in a or '844' in a or '84' in a:
#         a = a.replace('4444', '884', 1)
#         a = a.replace('844', '488', 1)
#         a = a.replace('84', '3343', 1)
#
#     print(i)
#     if len(a) < 20:
#         c = i
#         break
# print(c)
# # 15


# # 14
# counter = 0
# for i in range(200):
#     a = i
#     b = ''
#     while a > 0:
#         b = str(a % 4) + b
#         a //= 4
#
#     if b[-3:] == '123':
#         counter += 1
#         print(i, b)
# print(counter)


# # 16
# import sys
# from functools import lru_cache
# sys.setrecursionlimit(10_000)
#
# a = []
# @lru_cache(128, typed=False)
# def f(n):
#     if n >= 2024:
#         return 1
#     else:
#         return f(n+2) + f(n+4)
#
# for i in range(1, 2025):
#     a.append(f(i))
#
# a = set(a)
# print(len(a))


# # 17
#
# # 968
# max_num = 0
# counter = 0
# a = [int(i) for i in open('C:/Users/Gregoriy Mukhin/Downloads/17 (2).txt')]
# for i in range(len(a)-1):
#     # if len(str(abs(a[i]))) == 3:
#     #     max_num = max(max_num, a[i])
#     b = abs(a[i] ** 2 - a[i + 1] ** 2)
#     c = sum(list(map(lambda x: int(x), (list(str(abs(a[i])))))))
#     d = sum(list(map(lambda x: int(x), (list(str(abs(a[i + 1])))))))
#     print(c, d, a[i], a[i+1])
#     if ((c % 5 == 0 and d % 5 != 0) or (c % 5 != 0 and d % 5 == 0)) and (b >= 968 ** 3):
#     # if (c) % 5 == 0 and  % 5 != 0) or \
#     #     (sum(list(map(lambda x: int(x), (list(str(abs(a[i]))))))) % 5 != 0 and sum(list(map(lambda x: int(x), (list(str(abs(a[i]))))))) % 5 == 0)) and \
#     #    (b >= 968 ** 3):
#         counter += 1
#         max_num = max(max_num, a[i] + a[i + 1])
# print(counter, max_num)


# # 19
#
# def f(x, y, h):
#     if (x + y >= 189) and h < 2:
#         return 0
#     if (x + y < 189) and h == 2:
#         return 0
#     if (x + y >= 189) and h == 2:
#         return 1
#     else:
#         if h % 2 == 1:
#             return f(x + y, y, h + 1) or f(x, y + x, h + 1) or f(max(x, y), max(x, y), h + 1)
#         else:
#             return f(x + y, y, h + 1) or f(x, y + x, h + 1) or f(max(x, y), max(x, y), h + 1)
#
# for i in range(189):
#     if f(5, i, 0) == 1:
#         print(i)
#         break


# 20

def f(x, y, h):
    if (x + y >= 189) and h == 2:
        return 1
    elif (x + y >= 189) and h < 2:
        return 0
    elif (x + y < 189) and h == 2:
        return 0
    else:
        if h % 2 == 0:
            return g(x + y, y, h + 1) and g(x, y + x, h + 1) and g(max(x, y), max(x, y), h + 1)
        else:
            return g(x + y, y, h + 1) or g(x, y + x, h + 1) or g(max(x, y), max(x, y), h + 1)


def g(x, y, h):
    if (x + y >= 189) and (h == 4 or h == 2):
        return 1
    elif (x + y >= 189) and h < 4:
        return 0
    elif (x + y < 189) and h == 4:
        return 0

    else:
        if h % 2 == 0:
            return g(x + y, y, h + 1) and g(x, y + x, h + 1) and g(max(x, y), max(x, y), h + 1)
        else:
            return g(x + y, y, h + 1) or g(x, y + x, h + 1) or g(max(x, y), max(x, y), h + 1)


for i in range(189):
    if f(5, i, 0) == 1:
        print(i)
print('----------')
for i in range(189):
    if g(5, i, 0) == 1:
        print(i)
        break