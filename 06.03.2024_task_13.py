# https://kompege.ru/task
# 12922
#
# k = 0
# for i in range(256):
#     if (248 & i == 16) and not ('101' in bin(i)[2:]):
#         k += 1
# print(k)


# 12467
#
# for A in range(256):
#     if bin(252 & A)[2:].count('1') > 3:
#         break
# print(A)


# 12088

# counter = 0
# for i in range(256):
#     for u in range(4):
#         b4 = bin(i)[2:].count('1')
#         b3 = bin(u)[2:].count('1')
#         print(i, u, b3 + b4)




