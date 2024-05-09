# # 9753
# # https://kompege.ru/task
#
# a = open('C:/Users/Gregoriy Mukhin/Downloads/24_9753.txt').readline()
#
# for i in 'TUVWXZ':
#     a = a.replace(i, '0')
# a = a.replace('Y', '1')
#
# max_len = 0
# end = 1
# for i in range(len(a)):
#     print(i, max_len)
#     while a[i:end].count('1') < 150:
#         end += 1
#         max_len = max(max_len, len(a[i:end]))
#
# print(max_len)


#

a = [a for a in open('C:/Users/Gregoriy Mukhin/Downloads/24__3091.txt')]

for u in a:
    for i in range(len(u) - 2):
        b = u[i: i + 7]
        if len(set(list(b))) > 4:
            for i in range(7):
