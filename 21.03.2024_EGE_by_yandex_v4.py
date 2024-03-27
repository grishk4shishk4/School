# https://education.yandex.ru/ege/variants/7e480ec2-3b8f-4261-83ac-f01cee1cca75/task/19

# 19 - 80
# 20 - 62 3

# def f(x, y, h):
#     if (x + y >= 180) and h == 3:
#         return 1
#     elif (x + y >= 180) and h < 3:
#         return 0
#     elif (x + y < 180) and h == 3:
#         return 0
#     else:
#         if h % 2 == 1:
#             return f(x + 2, y, h + 1) and f(x, y + 2, h + 1) and f(x + y, y, h + 1) and f(x, x + y, h + 1)
#         else:
#             return f(x + 2, y, h + 1) or f(x, y + 2, h + 1) or f(x + y, y, h + 1) or f(x, x + y, h + 1)
#
#
# counter = 0
# for i in range(180):
#     if f(18, i, 0) == 1:
#         print(i)
#         counter += 1
#
# print(counter, 'end')

#
# # 21 - 77
#
#
# def f(x, y, h):
#     if (x + y >= 180) and h == 2:
#         return 1
#     elif (x + y >= 180) and h < 2:
#         return 0
#     elif (x + y < 180) and h == 2:
#         return 0
#     else:
#         if h % 2 == 0:
#             return f(x + 2, y, h + 1) and f(x, y + 2, h + 1) and f(x + y, y, h + 1) and f(x, x + y, h + 1)
#         else:
#             return f(x + 2, y, h + 1) or f(x, y + 2, h + 1) or f(x + y, y, h + 1) or f(x, x + y, h + 1)
#
#
# def g(x, y, h):
#     if (x + y >= 180) and (h == 4 or h == 2):
#         return 1
#     elif (x + y >= 180) and h < 4:
#         return 0
#     elif (x + y < 180) and h == 4:
#         return 0
#     else:
#         if h % 2 == 0:
#             return g(x + 2, y, h + 1) and g(x, y + 2, h + 1) and g(x + y, y, h + 1) and g(x, x + y, h + 1)
#         else:
#             return g(x + 2, y, h + 1) or g(x, y + 2, h + 1) or g(x + y, y, h + 1) or g(x, x + y, h + 1)
#
#
# for i in range(180):
#     if f(18, i, 0) == 1:
#         print(i)
# print('-----------')
# for i in range(180):
#     if g(18, i, 0) == 1:
#         print(i)
#         break


# 26
# 600 -  первая строка

def f(x, a):
    pass
    for i in range(a.)

a = sorted([int(i) for i in open('C:/Users/Gregoriy Mukhin/Downloads/26 (3).txt')])
print(a)


for i in range(sum(a)):
