# for num in range(1, 10):
#     print(('IX' * (num // 9)) +
#           ((num % 9) // 5 * 'V') +
#           ((num % 9) % 5) * 'I')
#
# list1 =['1', '2', '3', '4']
# list2 =['1', '2', '3', '4']
# list3 =['1', '2', '3', '4']
# list4 =['1', '2', '3', '4']
#
#
# a = '1341'
# for i in range(len(a)):
#     if i == 0:
#         print(list1[a[i]])
#

#
# dic = {
#     'nomer1': 3,
#     'nomer2': 'khgjgj',
#
# }
# print(dic['nomer2'])
# '''
# a = lambda x: x ** 2
# print(a(2))
# num_list = range(20)
# map(a, num_list)
# print(num_list)
# '''

# a = open('C:/Users/Gregoriy Mukhin/Downloads/24_demo.txt').readline()
#
# counter = 0
# max_len = 0
# for i in range(len(a)):
#     if (a[i] == 'X' and counter%3 == 0) or (a[i] == 'Y' and counter%3 == 1) or (a[i] == 'Z' and counter%3 == 2):
#         counter += 1
#         max_len = max(max_len, counter)
#     elif a[i] == 'X':
#         counter = 1
#     else:
#         counter = 0
# print(max_len)
#
#
#
# a = open
#
#
# # 5, 6, 7, 16, 18, 29, 25, 27, 35


# def f(x, y):
#     return (False or x == y)
# for i in range(-10, 10):
#     for u in range(-5, 5):
#         print(i, u, f(i, u))


#
# for a in range(1000, 5000):
#     b = 0
#     c = 0
#     for i in str(a):
#         b += int(i)
#     for i in str(b):
#         c += int(i)
#     if a + b + c == 2022:
#         print(a, b, c)


a = 'abcdefgt'
print(a[:int(len(a)/2//1) + 2], a[int(len(a)/2//1) + 1::-1])