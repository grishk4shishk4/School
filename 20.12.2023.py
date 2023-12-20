import random
a = random.randint(100, 1000)


def task4(x):
    b = [2, 3]
    for i in range(4, x + 1):
        counter = 0
        for j in b:
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

while True:
    b = int(input('введите число: '))
    if 1 < b < 10:
        break
    print('Число - инвалид')

d = a
c = ''
while a > 0:
    c = str(a % b) + c
    a //= b

print(d, c)
