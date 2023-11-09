# for w in range(2):
#     for x in range(2):
#         for y in range(2):
#             for z in range(2):
#                 f1 = (w == x) and (y <= z)
#                 f2 = (w <= x) <= (y == z)
#                 '''if (w == x) and (y <= z) == 1:
#                     a = 1
#                 else:
#                     a = 0
#                 if (w <= x) <= (x == z) == 1:
#                     b = 1
#                 else:
#                     b = 0'''
#                 print(w, x, y, z, int(f1), int(f2))

a = []
for N in range(35_000_000, 50_000_000):
    n1 = bin(N)[2:]
    n1 += bin(N % 3)[2:]
    n1 += bin(int(n1, 2) % 5)[2:]
    if int(n1, 2) > 1_222_222_222 and int(n1, 2) < 1_555_555_666:
        if a.count(n1) == 0:
            a.append(n1)

print(len(a))



# def f(x, h):
#     if x > 107 and h == 5:
#         return 1
#     elif x <= 107 and h == 5:
#         return 0
#     elif x > 107 and h < 5:
#         return 0
#     else:
#         if h%2==0:
#             if x%2==0:
#                 return f(x + 1, h + 1) or f(int(x * 1.5), h + 1)
#             else:
#                 return f(x + 1, h + 1) or f(x * 2, h + 1)
#         else:
#             if x%2==0:
#                 return f(x + 1, h + 1) and f(int(x * 1.5), h + 1)
#             else:
#                 return f(x + 1, h + 1) and f(x * 2, h + 1)
#
#
# '''
# def g(x, h):
#     if x > 107 and h == 3:
#         return 1
#     elif x <= 107 and h == 3:
#         return 0
#     elif x > 107 and h < 3:
#         return 0
#     else:
#         if h%2==0:
#             if x%2==0:
#                 return f(x + 1, h + 1) or f(int(x * 1.5), h + 1)
#             else:
#                 return f(x + 1, h + 1) or f(x * 2, h + 1)
#         else:
#             if x%2==0:
#                 return f(x + 1, h + 1) or f(int(x * 1.5), h + 1)
#             else:
#                 return f(x + 1, h + 1) or f(x * 2, h + 1)
# '''
#
#
# for i in range(1,108):
#     if f(i, 1) == 1 or g(i, i) == 1:
#         print(i)
