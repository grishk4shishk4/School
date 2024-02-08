# 12468 12246 - easy
# 1071 2235 - not so easy
# 828 9918 - not easy at all

# https://kompege.ru/task
# 12468
#
# for x in '0123456789ABCDEFGHI':
#     a1 = int('78' + x + '79643', 19)
#     a2 = int('25' + x + '43', 19)
#     a3 = int('63' + x + '5', 19)
#     if (a1 + a2 + a3) % 18 == 0:
#         print((a1 + a2 + a3) // 18)
#         break


# https://kompege.ru/task
# 12246

# a = (2*729**333 + 2 * 243**334 - 81**335 + 2 * 27**336 - 2 * 9**337 - 338)
# b = ''
# while a > 0:
#     b = str(a % 9) + b
#     a //= 9
#
# # print(b)
# print(len(b) - b.count('0'))


# https://kompege.ru/task
# 12246
#
# for x in range(10000):
#     a = (125**200) - (5**x) + 74
#     b = ''
#     while a > 0:
#         b = str(a % 5) + b
#         a //= 5
#
#     if b.count('4') == 100:
#         print(x)
#         break


# https://kompege.ru/task
# 2235
#
# a = (11 * 15**65) + (18 * 15**38) - (14*15**17) + (19*15**11) + 18338
# b = ''
# c = '0123456789ABCDE'
# while a > 0:
#     b = c[a % 15] + b
#     a //= 15
#
# print(len(set(list(b))))


# https://kompege.ru/task
# 9918

# a = []
# for x in range(10, 67):
#     for y in range(x):
#         a.append(7 * 67 ** 4 + 3 * 67 ** 3 + x * 67 ** 2 + 76 + y + 4 * x ** 3 + 9 * x ** 2 + y * x + 6)
# print(len(set(a)))


# https://kompege.ru/task
# 828

# a = 7 ** 103 + 49 ** 98 - 7 ** 120 - 7 * 33
# x = ''
# while a > 0:
#     x = (str(a % 7)) + x
#     a //= 7
# for y in range()
#
# for i in range(15, 31):
#     print(bin(i), bin(11), i&11)