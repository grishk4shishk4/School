# def t(n,m,k):
#     return max(n,m,k) < n + m + k - max(n,m,k)
# def f(A,x):
#     return t(x,10,20) <= (not((max(x,8) > 24)) == (not t(3,A,x)))
# for A in range(1000):
#     if all (f(A,x) for x in range(1000)):
#         print(A)
#
# for A in range(300, 0, -1):
#     counter = 0
#     b = 200
#     for x in range(b):
#         for y in range(b):
#             if (x + 2 * y > A) or (x > 13) or (y < 44):
#                 counter += 1
#     if counter == b ** 2:
#         print(A)
#         break


for i in range(2):
    for u in range(2):
        # if i < u:
        #     print(i, u)
        if i and u == 1:
            print(i, u)