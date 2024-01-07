import math
import random


a = random.randint(100, 1000)
a1 = random.randint(100, 1000)


def task4(x):
    b = [2, 3]
    for i in range(4, x + 1):
        counter = 0
        for j in b:
            if j > (i / 2) + 1:
                break
            if i % j == 0:
                counter += 1
                break
        if counter == 0:
            b.append(i)
    return b


# # 1
# b = []
# for i in range(1, int((a + 1)//1)):
#     if a % i == 0:
#         b.append(i)
# print(b, a)

# # 2
# d = a
# b = task4(a)
# c = []
# while a > 1:
#     for i in b:
#         if a % i == 0:
#             a /= i
#             c.append(i)
# print(d, c)


# # 3
# b = task4(a)
# if b.count(a) == 1:
#     print(a, 'Простое')
# else:
#     print(a, 'Не простое')


# 4
# print(f'{a} , {task4(a)}')

# 5
#
# while True:
#     b = int(input('введите число: '))
#     if 1 < b < 36:
#         break
#     print('Число - инвалид')
#
# d = a
# c = ''
# e = '0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ'
# # print(e[b])
# while a > 0:
#     c = str(e[a % b]) + c
#     a //= b
#
# print(d, c)


# 1
# print(a, a1)
#
# # НОД
# b = min(a, a1)
# c = task4(b)
# c.sort(reverse = True)
# c.append(1)
# for i in c:
#     if a % i == 0 and a1 % i == 0:
#         print(f'{a, a1} - {i}')
#         d = i
#         break
#
#
# # НОК
# print(int((a * a1)/i))


# # 2
# b = task4(1000)
# for i in b:
#     print(i ** 4)

# # 3
# b = ['']
# for i in range(10):
#     b.append(str(i))
# for i in range(10):
#     for i1 in range(10):
#         b.append(str(i) + str(i1))
# for i in range(10):
#     for i1 in range(10):
#         for i2 in range(10):
#             b.append(str(i) + str(i1) + str(i2))
# print(b)


# 4
# summ = 0
# for i in str(a):
#     summ += int(i)
# print(a, summ)

# d = a
# summ = 0
# while d > 0:
#     summ += int(d % 10)
#     d //= 10
# print(summ)


# print(a)
# print(sum(list(map(lambda x: int(x), list(str(a))))))

# 5
# b = []
# for i in range(20):
#     for j in range(20):
#         if 10 ** 8 < (2 ** i * 3 ** j) < 10 ** 9:
#             b.append(2**i * 3**j)
# print((b))

# 6
# for i in range(-5, 20):
#     for i in
