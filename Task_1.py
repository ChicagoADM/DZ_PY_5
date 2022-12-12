# Напишите программу, удаляющую из текста все слова, содержащие ""абв""
import os
clear = lambda: os.system('cls')
clear()
text_to_edit_in = 'Напишите програбвмму, удаляющуюабв из текабвста все слова, содержащие ""абв"'

def del_words(text_to_edit):
    text_to_edit = list(filter(lambda x: 'абв' not in x, text_to_edit.split()))
    return " ".join(text_to_edit)
text_to_edit = del_words(text_to_edit_in)
print(text_to_edit)
print()
input('Нажмите Enter для выхода ...')