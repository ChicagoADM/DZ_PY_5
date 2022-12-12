# Реализуйте RLE алгоритм: реализуйте модуль сжатия и восстановления данных.
import os
clear = lambda: os.system('cls')
clear()
import os

with open('file_encode.txt', 'w') as data:
    data.write('sdasadsaIYtytYTyiusxckhjyuyuiyiuyiuyhxzxzuiyuiyiu')

with open('file_encode.txt', 'r') as data:
    string = data.readline()

def rle_encode(decoded_str):
    encoded_string = ''
    count = 1
    char = decoded_str[0]
    for i in range(1, len(decoded_str)):
        if decoded_str[i] == char:
            count += 1
        else:
            encoded_string = encoded_string + str(count) + char
            char = decoded_str[i]
            count = 1
            encoded_string = encoded_string + str(count) + char
    return encoded_string


def rle_decode(encoded_string):
    decoded_str = ''
    char_amount = ''
    for i in range(len(encoded_string)):
        if encoded_string[i].isdigit():
            char_amount += encoded_string[i]
        else:
            decoded_str += encoded_string[i] * int(char_amount)
        char_amount = ''
    print(decoded_str)

    return decoded_str


with open('file_encode.txt', 'r') as file:
    decoded_str = file.read()

with open('file_decode.txt', 'w') as file:
    encoded_string = rle_encode(decoded_str)
    file.write(encoded_string)

print('Декодированная строка: \t' + decoded_str)
print()
print('Закодированная строка: \t' + rle_encode(decoded_str))
print()
input('Нажмите Enter для выхода ...')