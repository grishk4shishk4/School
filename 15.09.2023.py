# print(f'x,y,z,w')
# for x in range(2):
#     for y in range(2):
#         for z in range(2):
#             for w in range(2):
#                 if ((x or (not(y))) and (not(w == z)) and w) == 1:
#                     print(x, y, z, w)
#
# min_N = 10000
# for N in range(1000):
#     cur_summ = 0
#     N = str(bin(N)[2:])
#     N += N[-1:]
#     # print(N)
#     for i in str(N):
#         cur_summ += int(i)
#     N += str(bin(cur_summ % 2)[2:])
#     N = int(N, 2)
#     if N > 105:
#         min_N = min(N, min_N)
# print(min_N)
