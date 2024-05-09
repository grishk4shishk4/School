# https://kompege.ru/variant?kim=25049996


# # 19
#
# def f(x, y, h):
#     if x + y < 123 and h == 2:
#         return 0
#     if x + y >= 123 and h < 2:
#         return 0
#     if x + y >= 123 and h == 2:
#         return 1
#     else:
#         if h % 2 == 1:
#             return f(x + 1, y, h + 1) or f(x, y + 1, h + 1) or f(x * 2, y, h + 1) or f(x, y * 2, h + 1)
#         else:
#             return f(x + 1, y, h + 1) or f(x, y + 1, h + 1) or f(x * 2, y, h + 1) or f(x, y * 2, h + 1)
#
# for i in range(1, 109):
#     if f(13, i, 0) == 1:
#         print(i)
#
# # ans - 28


# # 20
#
# def f(x, y, h):
#     if x + y < 123 and h == 3:
#         return 0
#     if x + y >= 123 and h < 3:
#         return 0
#     if x + y >= 123 and h == 3:
#         return 1
#     else:
#         if h % 2 == 0:
#             return f(x + 1, y, h + 1) or f(x, y + 1, h + 1) or f(x * 2, y, h + 1) or f(x, y * 2, h + 1)
#         else:
#             return f(x + 1, y, h + 1) and f(x, y + 1, h + 1) and f(x * 2, y, h + 1) and f(x, y * 2, h + 1)
#
# for i in range(1, 109):
#     if f(13, i, 0) == 1:
#         print(i)
#
# # ans - 48 54


# # 21
#
# def f(x, y, h):
#     if x + y >= 123 and (h == 4 or h == 2):
#         return 1
#     if x + y < 123 and h == 4:
#         return 0
#     if x + y >= 123 and h < 4:
#         return 0
#     else:
#         if h % 2 == 0:
#             return f(x + 1, y, h + 1) and f(x, y + 1, h + 1) and f(x * 2, y, h + 1) and f(x, y * 2, h + 1)
#         else:
#             return f(x + 1, y, h + 1) or f(x, y + 1, h + 1) or f(x * 2, y, h + 1) or f(x, y * 2, h + 1)
#
#
# def g(x, y, h):
#     if (x + y >= 123) and h == 2:
#         return 1
#     if (x + y < 123) and h == 2:
#         return 0
#     if (x + y >= 123) and h < 2:
#         return 0
#     else:
#         if h % 2 == 0:
#             return g(x + 1, y, h + 1) or g(x, y + 1, h + 1) or g(x * 2, y, h + 1) or g(x, y * 2, h + 1)
#         else:
#             return g(x + 1, y, h + 1) or g(x, y + 1, h + 1) or g(x * 2, y, h + 1) or g(x, y * 2, h + 1)
#
#
# for i in range(1, 109):
#     if f(13, i, 0) == 1:
#         print(i)
#
# print('-------------------')
#
# for i in range(1, 109):
#     if g(13, i, 0) == 1:
#         print(i)
# # ans - 47
#
# # # 0 - вызов пети
# # # 1 - вызов вани


# # 23
#
# def f(x, s):
#     if x > s:
#         return 0
#     if x == s:
#         return 1
#     if x < s:
#         return f(x + 1, s) + f(x * 2, s)
#
# print(f(4, 8) * f(10, 15))
#
# # and - 2


# a = open('C:/Users/Gregoriy Mukhin/Downloads/24_15339.txt').readline()
#
# for i in 'ABC':
#     a = a.replace(i, '1')
# for i in '6789':
#     a = a.replace(i, '0')
#
# print(a)
#
# max_lenth = 0
# counter = 0
# for i in range(len(a) - 1):
#     if a[i] != a[i + 1]:
#         counter += 1
#     else:
#         max_lenth = max(max_lenth, counter)
#         counter = 1
#
# print(max_lenth)
#
# # ans - 22


# 27

a = open('C:/Users/Gregoriy Mukhin/Downloads/27B_15342.txt').readlines()
print(a)
