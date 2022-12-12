# Создайте программу для игры с конфетами человек против человека.
# Условие задачи: На столе лежит 2021 конфета. Играют два игрока делая ход друг после друга. Первый ход определяется жеребьёвкой. За один ход можно забрать не более чем 28 конфет. Все конфеты оппонента достаются сделавшему последний ход. Сколько конфет нужно взять первому игроку, чтобы забрать все конфеты у своего конкурента?
# a) Добавьте игру против бота
# b) Подумайте как наделить бота ""интеллектом""
import os
clear = lambda: os.system('cls')
clear()
from random import *
import os

def player_vs_player():
    candies_total = 2021
    max_take = 28
    count = 0
    player_1 = input('Введите имя первого играка: ')
    player_2 = input('Введите имя второго играка: ')
    print()
    x = randint(1, 2)
    if x == 1:
        Winner = player_1
        loser = player_2
    else:
        Winner = player_2
        loser = player_1
    print(f'{Winner} вы ходишь первым!')

    while candies_total > 0:
        if count == 0:
            step = int(input(f'\nВаш ход {Winner} = '))
            if step > candies_total or step > max_take:
                step = int(input(f'\nЗа один ход можно забрать не более чем {max_take} конфет {Winner}, попробуй еще раз: '))
            candies_total = candies_total - step
        if candies_total > 0:
            print(f'\nна кону осталость еще {candies_total}')
            count = 1
        else:
            print('Все кончились конфетки')

        if count == 1:
            step = int(input(f'\nВаш ход  {loser} = '))
            if step > candies_total or step > max_take:
                step = int(input(f'\nЗа один ход можно забрать не более чем {max_take} конфет {loser}, попробуй еще раз: '))
            candies_total = candies_total - step
        if candies_total > 0:
            print(f'\nна кону осталость еще {candies_total}')
            count = 0    
    print()
    if count == 1:
        print(f'{loser} ПОБЕДИЛ')
    if count == 0:
        print(f'{Winner} ПОБЕДИЛ')


player_vs_player()
print()
input('Нажмите Enter для выхода ...')