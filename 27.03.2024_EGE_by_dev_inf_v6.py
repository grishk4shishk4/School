# https://kompege.ru/variant?kim=25037852


# 1 - 21


# 13

# for i in range(8):
#     print(bin(i))


# 14

# a = [1, 2, 3]
# for i in range(5, 80000):
#     counter = 0
#     for u in a:
#         if u != 1 and u != i and i % u == 0:
#             counter += 1
#     if counter  == 0:
#         a.append(i)
#
# print(a)
#
# counter = 0
# b = '0123456789ABCDEFGH'
# for i in range(18):
#     c = (int('56' + b[i] + '3', 18) + int('4' + b[i] + '9', 18) + int('57' + b[i] + '1', 18))
#     print(c)
#     if c in a:
#         counter += 1
#
# print(counter)


# # 24
#
# a = open('C:/Users/Gregoriy Mukhin/Downloads/24_5381.txt').readline()
# # A B C D E F U
#
# a = a.replace('A', '0')
# a = a.replace('E', '0')
# a = a.replace('U', '0')
# a = a.replace('B', '1')
# a = a.replace('C', '1')
# a = a.replace('D', '1')
# a = a.replace('F', '1')
#
#
# b = []
# counter = 0
#
#
# for i in range(1, len(a) - 1):
#     counter += 1
#     if a[i - 3:i + 2] == '10101' or a[i - 1:i + 5] == '10101':
#         b.append(counter + 1)
#         b.append(1)
#         counter = 0
#     elif a[i - 1:i + 2] == '101':
#         b.append(counter + 1)
#         counter = 0
#
# max_num = 0
# for i in range(len(b) - 3):
#     max_num = max(max_num, (b[i] - 1) + b[i + 1] + (b[i + 2] - 1))
#
#
# print(max_num)
#
# # a = 'x' + a + 'x'
# #
# #
# # b = []
# # counter = 0
# # for i in a:
# #     if i == 'x':
# #         b.append(counter)
# #         counter = 0


# 26

