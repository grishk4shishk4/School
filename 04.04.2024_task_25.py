a = open('C:/Users/Gregoriy Mukhin/Desktop/нахрен/prime_numbers.txt').readline()
a = a.split(' ')
a = list(map(lambda x: int(x), a))

def divider(x, a):
    for i in range(len(a), 1, -1):
        if x % a[i] == 0 and a[i] % 7 == 0 and a[i] != x:
            return 1
        if x % a[i] == 0 and a[i] % 7 > 0 and a[i] != x:
            return 0



def polindrom(a):
    a = str(a)
   # if a[:int(len(a)/2//1) + 2] == a[int(len(a)/2//1) + 1::-1]:
    if a==a[::-1]:
        counter = 0
        for i in range(1, len(a)):
            if int(a[i]) % 2 == int(a[i - 1]) % 2:
                print(int(a[i]) % 2, int(a[i + 1]) % 2)
                return 0
        return 1
    return 0

for i in range(10**9, 10**11):
    if polindrom(i) == 1 or divider(i, a) == 1:
        print('a', i)
    else:
        print('b', i)