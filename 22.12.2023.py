# print(f'w x y z f1')
# for w in range(2):
#     for x in range(2):
#         for y in range(2):
#             for z in range(2):
#                 if (not(x <= w) or (y == z) or y) == 0:
#                     print(w, x, y, z)
#     #z x w y

#
# for i in range(100):
#     N = bin(i)[2:]
#     for i in range(2):
#         N += str((sum(list(map(lambda x: int(x), list(N))))) % 2)
#     print(i, N, int(N, 2))

# a = '1' + '8'*99 + '1'
# while ('81' in a) or ('882' in a) or ('8883' in a):
#     if '81' in a:
#         a = a.replace('81', '2', 1)
#     else:
#         if '882' in a:
#             a = a.replace('882', '3', 1)
#         else:
#             a = a.replace('8883', '1', 1)
# print(a)

a11 = int(input('x1: '))
a12 = int(input('y1: '))
a21 = int(input('x2: '))
a22 = int(input('y2: '))
b11 = int(input('x3: '))
b12 = int(input('y3: '))
b21 = int(input('x4: '))
b22 = int(input('y4: '))


