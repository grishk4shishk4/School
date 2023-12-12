# a_str = '3333'
# for i in range(100, 9, -1):
#     b_str = a_str + '7' * i
#     # print(b_str)
#     while '27' in b_str or '377' in b_str or '777' in b_str:
#         if '27' in b_str:
#             b_str = b_str.replace('27', '7', 1)
#         if '377' in b_str:
#             b_str = b_str.replace('377', '72', 1)
#         if '777' in b_str:
#             b_str = b_str.replace('777', '3', 1)
#
#     if b_str.count('2') == 0 and b_str.count('3') == 0:
#         print(i)
#         break

# for i in range(2, 1000):
#     a = i
#     N = ''
#     while i > 0:
#         N = str(i % 7) + N
#         i //= 7
#     N = (N[len(N) - 1:] + N[1:-1] + N[:1])
#     if int(N, 7) == 2024:
#         print(a, N, int(N, 7))


"А Е И К Н М Х"
"1 2 3 4 5 6 7"

"М Е Х А Н И К"
"6 2 7 1 5 3 4"

"А Н И М Е К Х"
"1 5 3 6 2 4 7"


print((int('1536247', 7)[2:]) - (int('6271834', 7)[2:]))