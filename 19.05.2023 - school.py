import keyboard

symbs = [[0, 0, 0], [0, 0, 0],[0, 0, 0]]
def symbs_print(symbs):
    for i in range(3):
        print('')
        for u in range(3):
            print(symbs[i][u], end=' ')
    print(end='\n')

symbs_print(symbs)
def user_number():
    while True:
        n = input('Введите число: ')
        try:
            if 48 < ord(n[0]) < 52 and 48 < ord(n[1]) < 52 and len(n) == 2:
                if symbs[ int(n[0]) - 1 ][ int(n[1]) - 1 ] == 0:
                    print(n)
                    return n
                else:
                    print('Эта клетка уже занята')
            else:
                print('1Неверное число')
        except:
            print('2Неверное число')

def user_1_take():
    global symbs
    u_round = user_number()
    symbs[int(u_round[0]) - 1][int(u_round[1]) - 1] = 1
    symbs_print(symbs)
    if winner_check(1, symbs) == 1:
        return None

def user_2_take():
    pass

def winner_check(user_num, symbs):

    for i in range(3):
        if symbs[i].count(user_num) == 3:
            return 11

    pass

user_1 = []
user_2 = []
for i in range(10):
    user_1_take()