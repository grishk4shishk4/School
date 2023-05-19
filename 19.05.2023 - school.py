import keyboard

symbs = [[0]*3]*3
for i in range(3):
    print('')
    for u in range(3):
        print(symbs[i][u], end=' ')
def user_number():
    while True:
        n = input('Введите число: ')
        try:
            if 48 < ord(n[0]) < 52 and 48 < ord(n[1]) < 52:
                if symbs[ int(n[0]) - 1 ][ int(n[1]) - 1 ] == 0:
                    print(n)
                    return n
            else:
                print('1Неверное число')
        except:
            print('2Неверное число')
for i in range(99):
    user_number()

user_1 = []
user_2 = []

