# print(f'w x y z')
# for w in range(2):
#     for x in range(2):
#         for y in range(2):
#             for z in range(2):
#                 if ((x or not(y)) and (y != z) and (not(w))) == 1:
#                     print(w, x, y, z)
# # x z y w

# counter = 0
# for i in range(10, 10000):
#     a = i
#     n = ''
#     while a > 0:
#         n = str(a % 3) + n
#         a //= 3
#     n2 = n
#     if i % 5 == 0:
#         n += n[-3:]
#     else:
#         a = (i % 5) * 5
#         n1 = ''
#         while a > 0:
#             n1 = str(a % 3) + n1
#             a //= 3
#         n = n + n1
#
#     if len(str(int(n, 3))) == 4:
#         counter += 1
#         print(i, n2, n, int(n, 3))
# print(counter)


# counter = 0
# for i in range(10, 100):
#     a = '4' + i* '5'
#     while '45' in a or '222' in a:
#         if '45' in a:
#             a = a.replace('45', '2')
#         if '222' in a:
#             a = a.replace('222', '4')
#     a = list(map(lambda x: int(x), list(a)))
#     if sum(a) % 2 == 0:
#         counter += 1
# print(counter)


# for x in range(36):
#     a = '0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ'
#     a1 = 'I' + str(a[x])
#     a2 = 'L' + str(a[x]) + 'VE'
#     a3 = 'ANIME'
#     b = int(a1, 36) + int(a2, 36) + int(a3, 36)
#     if b % 25 == 0:
#         print(b / 25)


# for A in range(10000, 0, -1):
#     counter = 0
#     for x in range(10000):
#         if (x % 10 == 0) <= ((x > 70) or (A < x + 10)):
#             counter += 1
#     if counter == 100:
#         print(A)
#         break

