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

a = lambda x: x ** 2
print(a(2))
num_list = range(20)
map(a, num_list)
print(num_list)