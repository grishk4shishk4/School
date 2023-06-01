#'''
import keyboard

symbs = [[0, 0, 0], [0, 0, 0],[0, 0, 0]]
def symbs_print(symbs):
    for i in range(3):
        print('')
        for u in range(3):
            print(symbs[i][u], end=' ')
    print(end='\n')

symbs_print(symbs)
def user_number(usr):
    while True:
        n = input(f'Ход пользователя - {usr}.|Введите число: ')
        try:
            if 48 < ord(n[0]) < 52 and 48 < ord(n[1]) < 52 and len(n) == 2:
                if symbs[int(n[0]) - 1][int(n[1]) - 1] == 0:
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
    u_round = user_number(1)
    symbs[int(u_round[0]) - 1][int(u_round[1]) - 1] = 1
    symbs_print(symbs)
    if winner_check(1, symbs) == True:
        return True

def user_2_take():
    global symbs
    u_round = user_number(2)
    symbs[int(u_round[0]) - 1][int(u_round[1]) - 1] = 2
    symbs_print(symbs)
    if winner_check(2, symbs) == True:
        return True

def winner_check(user_num, symbs):
    d_list = []
    u_list = [symbs[0, 2], symbs[1, 1], symbs[2, 0]]
    for i in range(3):
        if symbs[i].count(user_num) == 3:
            return True
        elif list(map(lambda x: x[i], symbs)).count(user_num) == 3:
            return True
        d_list.append(symbs[i][i])
    if d_list.count(user_num) == 3 or u_list.count(user_num) == 3:
        return True

    # if symbs[0][0] + symbs[1][1] + symbs[2][2] == user_num * 3:
    #     return True
    # if symbs[2][0] + symbs[1][1] + symbs[0][2] == user_num * 3:
    #     return True
#надо переписать проверку победителя по диагонали

while True:
    if user_1_take() == True:
        print('Пользователь 1 победил!')
        break
    if user_2_take() == True:
        print('Пользователь 2 победил!')
        break
#'''
