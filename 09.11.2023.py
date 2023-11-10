# a = []
# mx = 0
# for i in range(len(a), 1, -1):
#     if a[i] % 100 == 19:
#         mx = a[i]
#         break
# counter1 = 0
# for i in range(len(a) - 2):
#     counter = 0
#     if 999 < a[i] < 10000:
#         counter += 1
#     if 999 < a[i + 1] < 10000:
#         counter += 1
#     if 999 < a[i + 2] < 10000:
#         counter += 1
#     if counter == 2:
#         if a[i] % 3 == 0 or a[i + 1] % 3 == 0 or a[i + 2] % 3 == 0:
#             if

#
# def f(x, h):
#     if x >= 108 and h == 3:
#         return 1
#     if x < 108 and h == 3:
#         return 0
#     if x >= 108 and h < 3:
#         return 0
#     if h % 2 == 0:
#         if x % 2 == 0:
#             return f(x + 1, h + 1) or f((x * 3) // 2, h + 1)
#         else:
#             return f(x + 1, h + 1) or f(x * 2, h + 1)
#     else:
#         if x % 2 == 0:
#             return f(x + 1, h + 1) and f((x * 3) // 2, h + 1)
#         else:
#             return f(x + 1, h + 1) and f(x * 2, h + 1)
#
# for i in range(1, 108):
#     if f(i, 1) == 1:
#         print(i)

# def f(x, h):
#     if x >= 108 and (h == 5 or h == 3):
#         return 1
#     if x < 108 and h == 3:
#         return 0
#     if x >= 108 and h < 3:
#         return 0
#     if h % 2 == 0:
#         if x % 2 == 0:
#             return f(x + 1, h + 1) or f((x * 3) // 2, h + 1)
#         else:
#             return f(x + 1, h + 1) or f(x * 2, h + 1)
#     else:
#         if x % 2 == 0:
#             return f(x + 1, h + 1) and f((x * 3) // 2, h + 1)
#         else:
#             return f(x + 1, h + 1) and f(x * 2, h + 1)
#
# for i in range(1, 108):
#     if f(i, 1) == 1:
#         print(i)


