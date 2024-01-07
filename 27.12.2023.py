# # 51993
# a = open('C:/Users/Gregoriy Mukhin/Downloads/24.txt').readline().split('F')
# max_str = 0
# count = 1
# for i in range(len(a)):
#     if a[i].count('A') <= 2:
#         count += len(a[i]) + 1
#         max_str = max(max_str, count)
#     else:
#         count = 1
# print(max_str)
# mx = 0
# count = 1
# for i in range(len(s)):
#     if s[i].count('A') <= 2:
#         count += len(s[i]) + 1
#         mx = max(mx, count)
#     else:
#         count = 1
# print(mx)



# # 59729
# a = open('C:/Users/Gregoriy Mukhin/Downloads/1_24.txt').readline()










#
# print(f'x y z w f1')
# for x in range(2):
#     for y in range(2):
#         for z in range(2):
#             for w in range(2):
#                 if (((x <= y) or (z == x)) and (w <= z)) == 0:
#                     print(x, y, z, w, 0)
#                 if ((((x <= y) or (z == x)) and (w <= z)) == 1) and (((x == 1) or (w == 1)) and (z == 0)):
#                     print(x, y, z, w, 1)



for i in range(123437, 10**10, 137):
    if (str(i)[:4] == '1234'):
        a = int(str(i)[4:])
        s = 0
        for u in str(a):
            s += int(u)
        if a % (u ** 3) == 0:
            print(i)

