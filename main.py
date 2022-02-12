#!.venv/bin/python

from collections import Counter
from prettytable import PrettyTable
import re
import pymorphy2

table = PrettyTable() 
table.field_names = ["СЛОВО", "КОЛИЧЕСТВО В ТЕКСТЕ", "% ОТ ОБЩЕГО ЧИСЛА СЛОВ"]
table_list = []

while True:
    try:
        files_str = input('Введите относительный или абсолютный путь файлов: ')
        list_of_files = files_str.split(' ')
        data = ''
        for file in list_of_files:
            f = open(file)
            data += f.read().lower()
    except FileNotFoundError:
        print('Файл не найден!')
        continue
    except IsADirectoryError:
        print('Ошибка! Вы ввели имя директории')
        continue
    except PermissionError:
        print('Невозможно открыть файл! Нет прав доступа')
        continue
    except Exception:
        print('Ошибка!')
    break    

words = re.sub(r'[^\w\s]', '', data)
words = words.split()
uniq = set(words)
morph = pymorphy2.MorphAnalyzer() 

print(f'Общее количество слов: {len(words)}')
print(f'Количество уникальных слов: {len(uniq)}')

dict_words = Counter(words)
list_dict_words = list(dict_words.items())
list_dict_words.sort(key=lambda i: i[1], reverse=True)

exc_words = ['CONJ', 'PRCL', 'INTJ', 'NPRO', 'PRED', 'PREP'] # части речи, которые мы хотим исключить из выборки

def percent(x, y): # функция для вычисления % одного числа от другого
    return round((x / y * 100), 2)
    
x = 0
while True:
    try:
        how_many = int(input('Сколько самых популярных слов хотите увидеть? '))
        if how_many <= 0:
            print('Нужно ввести положительное число (больше, чем 0)')
            continue
        
            
    except ValueError:
        print('Вы ввели не целое положительное число (без плавающей точки)')  
        continue  

    break
for word, count in list_dict_words:
    if x == how_many:
        break
    w = morph.parse(word)[0]
    if w.tag.POS in exc_words:
        continue
    table_list = [word, count, percent(count, len(words))]
    table.add_rows([table_list])
    x += 1

print(table)