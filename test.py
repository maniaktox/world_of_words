# import pymorphy2

# morph = pymorphy2.MorphAnalyzer()
# x = morph.parse('чтобы')[0]
# print(x.tag)


files_str = input('Input files: ')

files = files_str.split(' ') # ['file1', 'file2']
text = ''


for file in files:
    
    f = open(file + '.txt')
    text = text + f.read()



print(text)