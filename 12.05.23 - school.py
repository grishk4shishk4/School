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
        if ord(Usr_Num[0]) >= 48 and ord(Usr_Num[0]) <= 57 and \
            ord(Usr_Num[1]) >= 48 and ord(Usr_Num[1]) <= 57 and \
            ord(Usr_Num[2]) >= 48 and ord(Usr_Num[2]) <= 57 and \
            ord(Usr_Num[3]) >= 48 and ord(Usr_Num[3]) <= 57:
            return Usr_Num
        else:
            print('некоректное число')

for i in range(5):
    usr_number()