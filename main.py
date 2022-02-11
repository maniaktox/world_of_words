from collections import Counter
from prettytable import PrettyTable
import re
import pymorphy2

table = PrettyTable() 
table.field_names = ["СЛОВО", "КОЛИЧЕСТВО В ТЕКСТЕ", "% ОТ ОБЩЕГО ЧИСЛА СЛОВ"]
table_list = []
while True:
    try:
        files_str = input('Введите имя одного или нескольких файлов через пробел и без расширения: ')
        list_of_files = files_str.split(' ')
        data = ''
        for file in list_of_files:
            
            f = open(file + '.txt')
            data += f.read().lower()
              
    except FileNotFoundError:
        print('Файл не найден')
        continue
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

def percent(count, words): # функция для вычисления % от общего числа слов
    perc = round((count / len(words) * 100), 2)
    return perc

x = 0
how_many = int(input('Сколько самых популярных слов хотите увидеть? '))
for word, count in list_dict_words:
    if x == how_many:
        break
    w = morph.parse(word)[0]
    if w.tag.POS in exc_words:
        continue
    table_list = [word, count, percent(count, words)]
    table.add_rows([table_list])
    #print(f'Слово "{word}" встречается {count} раз(а), {percent(count, words)} % от общего количества слов') 
    #print(table_list)
    x += 1

print(table)