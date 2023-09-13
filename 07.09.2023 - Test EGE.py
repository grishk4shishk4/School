'''
print(f'w x y z')
for w in range(2):
    for x in range(2):
        for y in range(2):
            for z in range(2):
                if ((x and (not (y))) or (y == z) or (not(w)))==0:
                    print(w, x, y, z)
'''
counter = []
for N in range(100):
    N1 = bin(N)[2:]
    if N % 3 == 0:
        N1 += N1[-3:]
    else:
        N1 += bin((N % 3)*3)[2:]
    R = int(N1,2)
    if R > 151:
        print(N, N1, R)
