from collections import Counter

file = open('bird.txt')
data = file.read().lower()
words = data.split()
uniq = set(words)
print(f'Общее количество слов: {len(words)}')
print(f'Количество уникальных слов: {len(uniq)}')

dict_words = Counter(words)
list_dict_words = list(dict_words.items())
list_dict_words.sort(key=lambda i: i[1], reverse=True)

for i in list_dict_words[:10]:
    print(f'Слово "{i[0]}" встречается {i[1]} раз(а), {round((i[1] / len(words) * 100), 2)} % от общего количества слов') 
