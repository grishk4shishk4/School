# flag = 1 -  игрок +1
# flag = 2 -  игрок +2
# flag = 3 -  игрок *2

# https://kompege.ru/task
# тип 19 - 21 №2574

# 19
# def f(x, h, flag):
#     if h == 3 and x < 43:
#         return 0
#     if h < 3 and x >= 43:
#         return 0
#     if h == 3 and x >= 43:
#         return 1
#     else:
#         if h % 2 == 1:
#             if flag == 0:
#                 return f(x + 1, h + 1, 1) and f(x + 2, h + 1, 2) and f(x * 2, h + 1, 3)
#             if flag == 1:
#                 return f(x + 2, h + 1, 2) and f(x * 2, h + 1, 3)
#             if flag == 2:
#                 return f(x + 1, h + 1, 1) and f(x * 2, h + 1, 3)
#             if flag == 3:
#                 return f(x + 1, h + 1, 1) and f(x + 2, h + 1, 2)
#         else:
#             if flag == 1:
#                 return f(x + 2, h + 1, 2) or f(x * 2, h + 1, 3)
#             if flag == 2:
#                 return f(x + 1, h + 1, 1) or f(x * 2, h + 1, 3)
#             if flag == 3:
#                 return f(x + 1, h + 1, 1) or f(x + 2, h + 1, 2)
#
#
# for i in range(1, 43):
#     if f(i, 1, 0) == 1:
#         print(i)


# 20
# def f(x, h, flag):
#     if h == 4 and x < 43:
#         return 0
#     if h < 4 and x >= 43:
#         return 0
#     if h == 4 and x >= 43:
#         return 1
#     else:
#         if h % 2 == 0:
#             if flag == 0:
#                 return f(x + 1, h + 1, 1) and f(x + 2, h + 1, 2) and f(x * 2, h + 1, 3)
#             if flag == 1:
#                 return f(x + 2, h + 1, 2) and f(x * 2, h + 1, 3)
#             if flag == 2:
#                 return f(x + 1, h + 1, 1) and f(x * 2, h + 1, 3)
#             if flag == 3:
#                 return f(x + 1, h + 1, 1) and f(x + 2, h + 1, 2)
#         if h == 1:
#             if flag == 0:
#                 return f(x + 1, h + 1, 1) or f(x + 2, h + 1, 2) or f(x * 2, h + 1, 3)
#             if flag == 1:
#                 return f(x + 2, h + 1, 2) or f(x * 2, h + 1, 3)
#             if flag == 2:
#                 return f(x + 1, h + 1, 1) or f(x * 2, h + 1, 3)
#             if flag == 3:
#                 return f(x + 1, h + 1, 1) or f(x + 2, h + 1, 2)
#         else:
#             if flag == 1:
#                 return f(x + 2, h + 1, 2) or f(x * 2, h + 1, 3)
#             if flag == 2:
#                 return f(x + 1, h + 1, 1) or f(x * 2, h + 1, 3)
#             if flag == 3:
#                 return f(x + 1, h + 1, 1) or f(x + 2, h + 1, 2)
#
#
# for i in range(1, 42):
#     if f(i, 1, 0) == 1:
#         print(i)


# # 21
# def f(x, h, flag):
#     if h == 5 and x < 43:
#         return 0
#     if h < 5 and x >= 43:
#         return 0
#     if (h == 5 or h == 3) and x >= 43:
#         return 1
#     else:
#         if h % 2 == 1:
#             if flag == 0:
#                 return f(x + 1, h + 1, 1) and f(x + 2, h + 1, 2) and f(x * 2, h + 1, 3)
#             if flag == 1:
#                 return f(x + 2, h + 1, 2) and f(x * 2, h + 1, 3)
#             if flag == 2:
#                 return f(x + 1, h + 1, 1) and f(x * 2, h + 1, 3)
#             if flag == 3:
#                 return f(x + 1, h + 1, 1) and f(x + 2, h + 1, 2)
#         # if h == 2:
#         #     if flag == 0:
#         #         return f(x + 1, h + 1, 1) or f(x + 2, h + 1, 2) or f(x * 2, h + 1, 3)
#         #     if flag == 1:
#         #         return f(x + 2, h + 1, 2) or f(x * 2, h + 1, 3)
#         #     if flag == 2:
#         #         return f(x + 1, h + 1, 1) or f(x * 2, h + 1, 3)
#         #     if flag == 3:
#         #         return f(x + 1, h + 1, 1) or f(x + 2, h + 1, 2)
#         else:
#             if flag == 0:
#                 return f(x + 1, h + 1, 1) or f(x + 2, h + 1, 2) or f(x * 2, h + 1, 3)
#             if flag == 1:
#                 return f(x + 2, h + 1, 2) or f(x * 2, h + 1, 3)
#             if flag == 2:
#                 return f(x + 1, h + 1, 1) or f(x * 2, h + 1, 3)
#             if flag == 3:
#                 return f(x + 1, h + 1, 1) or f(x + 2, h + 1, 2)
#
#
# # def f2(x, h, flag):
# #     if h == 2 and x < 43:
# #         return 0
# #     if h < 2 and x >= 43:
# #         return 0
# #     if h == 2 and x >= 43:
# #         return 1
# #     else:
# #         if h % 2 == 1:
# #             if flag == 0:
# #                 return f(x + 1, h + 1, 1) and f(x + 2, h + 1, 2) and f(x * 2, h + 1, 3)
# #             if flag == 1:
# #                 return f(x + 2, h + 1, 2) and f(x * 2, h + 1, 3)
# #             if flag == 2:
# #                 return f(x + 1, h + 1, 1) and f(x * 2, h + 1, 3)
# #             if flag == 3:
# #                 return f(x + 1, h + 1, 1) and f(x + 2, h + 1, 2)
# #         else:
# #             if flag == 0:
# #                 return f(x + 1, h + 1, 1) or f(x + 2, h + 1, 2) or f(x * 2, h + 1, 3)
# #             if flag == 1:
# #                 return f(x + 2, h + 1, 2) or f(x * 2, h + 1, 3)
# #             if flag == 2:
# #                 return f(x + 1, h + 1, 1) or f(x * 2, h + 1, 3)
# #             if flag == 3:
# #                 return f(x + 1, h + 1, 1) or f(x + 2, h + 1, 2)
#
#
# for i in range(1, 42):
#     if f(i, 1, 0) == 1:
#         print(i)
#
#     # print(i, f(i, 1, 0))


# https://kompege.ru/task
# тип 19 - 21 №7720


# 19
def f(x, h, SUPER):

    a = []
    for i in range(2, x):
        if x % i == 0:
            a.append(i)
    SUPER_a = sum(a)


    if h == 2 and x < 43:
        return 0
    if h == 2 and x >= 43:
        return 1
    if h < 2 and x >= 43:
        return 0
    if h < 2 and x < 43:
        if SUPER == 0:
            if h % 2 == 1:
                return f(x + SUPER_a, h + 1, 1) and f(x + 1, h + 1, 0) and f(x + 4, h + 1, 0)
            else:
                return f(x + SUPER_a, h + 1, 1) or f(x + 1, h + 1, 0) or f(x + 4, h + 1, 0)
        else:
            if h % 2 == 0:
                return f(x + 1, h + 1, 1) and f(x + 4, h + 1, 1)
            else:
                return f(x + 1, h + 1, 1) or f(x + 4, h + 1, 1)


for i in range(1, 42):
    if f(i, 0, 0) == 1:
        print(i)


# # 20
# def f(x, h, SUPER):
#
#     a = []
#     for i in range(2, x):
#         if x % i == 0:
#             a.append(i)
#     SUPER_a = sum(a)
#
#
#     if h == 3 and x < 43:
#         return 0
#     if h == 3 and x >= 43:
#         return 1
#     if h < 3 and x >= 43:
#         return 0
#     if h < 3 and x < 43:
#         if SUPER == 0:
#             if h % 2 == 1:
#                 return f(x + SUPER_a, h + 1, 1) and f(x + 1, h + 1, 0) and f(x + 4, h + 1, 0)
#             else:
#                 return f(x + SUPER_a, h + 1, 1) or f(x + 1, h + 1, 0) or f(x + 4, h + 1, 0)
#         else:
#             if h % 2 == 1:
#                 return f(x + 1, h + 1, 1) and f(x + 4, h + 1, 1)
#             else:
#                 return f(x + 1, h + 1, 1) or f(x + 4, h + 1, 1)
#
#
# for i in range(1, 42):
#     if f(i, 0, 0) == 1:
#         print(i)


# 21
# def f(x, h, SUPER):
#
#     a = []
#     for i in range(2, x):
#         if x % i == 0:
#             a.append(i)
#     SUPER_a = sum(a)
#
#
#     if h == 1 and x < 43:
#         return 0
#     if h == 1 and x >= 43:
#         return 1
#     if h < 1 and x >= 43:
#         return 0
#     if h < 1 and x < 43:
#         if SUPER == 0:
#             if h % 2 == 1:
#                 return f(x + SUPER_a, h + 1, 1) and f(x + 1, h + 1, 0) and f(x + 4, h + 1, 0)
#             else:
#                 return f(x + SUPER_a, h + 1, 1) or f(x + 1, h + 1, 0) or f(x + 4, h + 1, 0)
#         else:
#             if h % 2 == 1:
#                 return f(x + 1, h + 1, 1) and f(x + 4, h + 1, 1)
#             else:
#                 return f(x + 1, h + 1, 1) or f(x + 4, h + 1, 1)
#
# a = []
# for i in range(1, 43):
#     if f(i, 0, 0) == 1:
#         a.append(i)
# print(len(a))


