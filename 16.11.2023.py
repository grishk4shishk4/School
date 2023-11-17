# def n3(a):
#     b = ''
#     while a > 0:
#         b = str(a % 3) + b
#         a //= 3
#     return b
#
# c = 100000
#
# for i in range(1000):
#     N = bin(i)[2:]
#
#     summ = 0
#     for u in str(n3(i)):
#         summ += int(u)
#
#     if int(summ) % 4 == 0:
#         N = ('1' + N)[:2]
#
#     else:
#         N += n3((int(summ) % 4) * 3)
#
#     if int(N, 3) > 353:
#         c = min(c, int(N, 3))
#         print(int(N, 3))
# print(f'----- {c}')


