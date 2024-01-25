# https://kompege.ru/task
# 9828
#
# def lox(a):
#     b = ''
#     while a > 0:
#         b = str(a % 3) + b
#         a //= 3
#     return b
#
#
# for i in range(10000, 1, -1):
#     b = lox(i)
#
#     if int(b, 3) % 3 == 0:
#         b = '1' + b + '02'
#     else:
#         b += lox((int(b, 3) % 3) * 4)
#
#     if int(b, 3) < 199:
#         print(i, b, int(b))
#         break


# https://kompege.ru/task
# 206

# counter = 0
# for i in range(800, 900):
#     a = sorted(list(str(i)))
#     b1 = int(a[0] + a[1])
#     b2 = int(a[2] + a[1])
#     if b2 - b1 == 30:
#         counter += 1
# print(counter)




# https://kompege.ru/task
# 488
#
# min_num = 10000
# max_num = 0
#
# for i in range(1000, 9999):
#     a = list(str(i))
#     b = []
#     for u in range(len(a) - 1):
#         for y in range(u, len(a)):
#                 if a[u] != '0':
#                     b.append(int(a[u] + a[y]))
#                 if a[y] != '0':
#                     b.append(int(a[y] + a[u]))
#     b = sorted(set(b))
#     if len(b) == 15:
#         min_num = min(min_num, i)
#         max_num = max(max_num, i)
#     print(i, b, len(b))
#
# print(max_num - min_num)



# https://kompege.ru/task
# 5899

#
# for i in range(100, 1000):
#     a = list(str(i))
#     b = []
#     for u in range(len(a) - 1):
#         for y in range(u, len(a)):
#             if

# 2226 7417 924
# https://kompege.ru/task
# 2226

# for i in range(301, 1000):
#     a = '8' * i
#     while '555' in a or '888' in a:
#         a = a.replace('555', '8')
#         a = a.replace('888', '55')
#         print(a)
#
#     print(i)
#     if a.count('8') == 1 and a.count('5') == 1:
#         print(i)
#         break

# https://kompege.ru/task
# 7417

# def f(n):
#     for i in range(2, n):
#         if n % i == 0:
#             return 0
#     return 1
#
#
# for n in range(1, 100):
#     a = '>' + ('0' * 37) + ('1' * n) + ('2' * 37)
#
#     while '>1' in a or '>2' in a or '>0' in a:
#         a = a.replace('>1', '22>')
#         a = a.replace('>2', '2>')
#         a = a.replace('>0', '1>')
#
#     b = int(a[:-1])
#     c = 0
#     for i in str(b):
#         c += int(i)
#     if f(c) == 1:
#         print(n)
#         break


# https://kompege.ru/task
# 924
counter = 0
for i in range(250, 1, -1):
    for u in range(250, 1, -1):
        a = ('1' * i) + ('3' * u)
        while '12' in a or '13' in a:
            a = a.replace('12', '21')
            a = a.replace('31', '23')
            a = a.replace('13', '23')

        if a.count('1') == 0 and sum(map(lambda x: int(x), list(a))) == 404:
            print(i + u)
            counter = 1
            break
    if counter == 1:
        break