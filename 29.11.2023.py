counter = 0
for i in range(10_000, 99_999):
    if str(i).count('7') == 0 and\
            str(i).count('8') == 0 and\
            str(i).count('9') == 0:

        n = str(i)
        if str(n).count('6') == 1:
            n1 = 0
            n2 = 0
            for i in n:
                if int(i) % 2 == 0:
                    n2 += int(i)
                else:
                    n1 += int(i)
            if n1 > n2:
                counter += 1
print(counter)