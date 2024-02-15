# b = 0
# a = [int(i) for i in open('C:/Users/Gregoriy Mukhin/Downloads/27-A_12257.txt')]
# for i in range(len(a) - 1):
#     for j in range(i, len(a)):
#         if sum(a[i:j]) % 113 == 0:
#             b = max(b, j - i)
#             # print(f'{i - j}')
# print(b)

# a = [int(i) for i in open('C:/Users/Gregoriy Mukhin/Downloads/27-A_12257.txt')]
# b = (sum(a) % 113)
# c1 = []
# c2 = []
# for i in range(100):
#     c1.append(a[i] % 113)
#     c2.append((len(a) - i) % 113)
#
# min_d = 100
# d = 0
# for i in range(len(c2)):
#     for j in range(len(c2)):
#         d = (sum(c1[:i]) + sum(c2[:j])) % 113
# print(i, j)