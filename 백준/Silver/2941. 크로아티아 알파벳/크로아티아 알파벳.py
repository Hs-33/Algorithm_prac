word = input()
cro_words = ['c=', 'c-', 'dz=', 'd-', 'lj', 'nj', 's=', 'z=']

for i in cro_words:
    if i in word:
        word = word.replace(i, '@')
    else:
        continue
print(len(word))