from random import randint

def rand_number():
    while True:
        Ai_Num = randint(1000, 9876)
        N = str(Ai_Num)
        if N.count(N[0]) + N.count(N[1]) + N.count(N[2]) + N.count(N[1]) == 4:
            return Ai_Num
        '''
        else:
            return 0

for for i in range(25):
        print(rand_num())
'''
print(f'Быки и коровы')
def usr_number():
    while True:
        Usr_Num = str(input('Введите число: '))
        # почему если условие из 21 строки стоит первым ошибок нету
        # а если его сдвинуть на 5 место - они появляются
        if len(Usr_Num) == 4 and \
            48 <= ord(Usr_Num[0]) <= 57 and \
            48 <= ord(Usr_Num[1]) <= 57 and \
            48 <= ord(Usr_Num[2]) <= 57 and \
            48 <= ord(Usr_Num[3]) <= 57:
            return Usr_Num
        else:
            print('Ошибка: Некоректное число')
'''
for i in range(5):
    usr_number()
'''
attempt = 0
b = 0
ai = str(rand_number())

while b < 4:
    attempt += 1
    b = 0
    k = 0
    user = str(usr_number())
    for i in range(4):
        if user[i] == ai[i]:
            b += 1
        elif user[i] == ai[0] or \
                user[i] == ai[1] or \
                user[i] == ai[2] or \
                user[i] == ai[3]:
            k += 1
    print(user, ai)
    print(b, k)
print(f"Пользователь победил за {attempt} ходов")