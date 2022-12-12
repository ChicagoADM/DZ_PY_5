# Создайте программу для игры в ""Крестики-нолики"".
import os
clear = lambda: os.system('cls')
clear()
import os

field = [1, 2, 3, 4, 5, 6, 7, 8, 9]
player = 'X'
victory = 0
i = 0

while i < 10:
    print('-'*13)
    print(f'| {field[0]} | {field[1]} | {field[2]} |')
    print('-'*13)
    print(f'| {field[3]} | {field[4]} | {field[5]} |')
    print('-'*13)
    print(f'| {field[6]} | {field[7]} | {field[8]} |')
    print('-'*13)
    if victory == 0 and i == 9:
        print('Ничья')
        break
    if victory == 1:
        if player == '0':
            print(f'Победа [X] !!!!!!!')
        else:
            print(f'Победа [0] !!!!!!!')
        break    
    if victory == 0:
        num = int(input(f'{player} Введите номер поля: '))
        if num > 0 and num < 10:
            if field[num - 1] != 'X' and field[num - 1] != '0':
                if player == '0':
                    field[num - 1] = '0'
                    player = 'X'
                else:
                    field[num - 1] = 'X'
                    player = '0'
                i += 1
            else:
                print(f'{player} Поле зането! Введите другой номер.')
        else:
            print(f'{player} Поле не существует! Введите другой номер.')
            
        if num > 0 and num < 10:
            if (field[0] == 'X' and field[1] == 'X' and field[2] == 'X') or (field[0] == '0' and field[1] == '0' and field[2] == '0'):
                victory = 1
            if (field[3] == 'X' and field[4] == 'X' and field[5] == 'X') or (field[3] == '0' and field[4] == '0' and field[5] == '0'):
                victory = 1
            if (field[6] == 'X' and field[7] == 'X' and field[8] == 'X') or (field[6] == '0' and field[7] == '0' and field[8] == '0'):
                victory = 1
            if (field[0] == 'X' and field[3] == 'X' and field[6] == 'X') or (field[0] == '0' and field[3] == '0' and field[6] == '0'):
                victory = 1
            if (field[1] == 'X' and field[4] == 'X' and field[7] == 'X') or (field[1] == '0' and field[4] == '0' and field[7] == '0'):
                victory = 1
            if (field[2] == 'X' and field[5] == 'X' and field[8] == 'X') or (field[2] == '0' and field[5] == '0' and field[8] == '0'):
                victory = 1
            if (field[0] == 'X' and field[4] == 'X' and field[8] == 'X') or (field[0] == '0' and field[4] == '0' and field[8] == '0'):
                victory = 1
            if (field[2] == 'X' and field[4] == 'X' and field[6] == 'X') or (field[2] == '0' and field[4] == '0' and field[6] == '0'):
                victory = 1
print()
input('Нажмите Enter для выхода ...')