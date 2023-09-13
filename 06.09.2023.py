'''
from random import randint as rnd

num_list = []
for i in range(100):
    num_list.append(rnd(1, 100))
'''
'''
summ1 = []
summ2 = []
counter = 0
while True:
    summ1.append((num_list[counter]) % 3)
    print(111, (num_list[counter]) % 3)
    counter += 1
    if summ1.count(1) == 2 or summ1.count(1) == 1 and summ1.count(2) == 1:
        break

while True:
    summ2.append(num_list[(len(num_list) - counter) % 3])
    print(222, (len(num_list) - counter) % 3)
    counter += 1
    if summ2.count(1) == 2 or summ2.count(1) == 1 and summ2.count(2) == 1:
        break

print(summ1, summ2)

'''
'''
import math

print(f'task 1 {sum(num_list)}')
summ = 0
for i in num_list:
    summ += i
print(f'task 1 {summ}')


counter = 1
for i in num_list:
    if i % 2 == 0:
        counter += 1
print(f'task 2 {counter}')


num_list2 = sorted(num_list)
print(f'task 3 {len(num_list2), num_list2}')


print(f'task 4 {int(summ / 100) + 1} ', end='')

a = int(summ / 100) + 1
for i in range(a - 1, 0, -1):
    if a % i == 0:
        print(i)
        break

counter = 0
for i in num_list:
    if len(bin(i)) == 8:
#        print(i, bin(i))
        counter += 1
print(f'task 5 {counter}')
'''
#'''
import random

num_list =[]
for i in range(20):
    num_list.append(random.randint(1, 100))
print(num_list)

nums17 = 0
num_list17 = []
nums2 = 0
num_list2 = []
nums34 = 0
num_list34 = []
for IDi, i in enumerate(num_list):
    if i % 34 == 0:
        print(f'ЧИСЛО 34 {i, IDi}')
        nums34 += 1
        num_list34.append(i)
    elif i % 2 == 0:
        print(f'ЧИСЛО 2 {i, IDi}')
        nums2 += 1
        num_list2.append(i)
    elif i % 17 == 0:
        print(f'ЧИСЛО 17 {i, IDi}')
        nums17 += 1
        num_list.append(i)

# a = max(num_list17, num_list2, num_list34)
# print(a)
S = nums2 * nums17 + nums34(len(num_list) - nums34) + (nums34 * (nums34 - 1)) / 2
print(S)
#'''
open('C:\Users\Gregoriy Mukhin\Downloads\тайминги в нс')