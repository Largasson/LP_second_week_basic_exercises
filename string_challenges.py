# Вывести последнюю букву в слове
word = 'Архангельск'
print(word[-1])
print()

# Вывести количество букв "а" в слове
word = 'Архангельск'
print(word.count('а'))
print(word.lower().count('а')) # если без учета регистра
print()
# Вывести количество гласных букв в слове
word = 'Архангельск'
wolwes = {'а', 'у', 'о', 'ы', 'и', 'э', 'я', 'ю', 'ё', 'е'}
count = 0
for s in word:
    if s.lower() in wolwes:
        count += 1
print(count)
print()

# Вывести количество слов в предложении
sentence = 'Мы приехали в гости'
print(len(sentence.split()))
print()

# Вывести первую букву каждого слова на отдельной строке
sentence = 'Мы приехали в гости'
for word in sentence.split():
    print(word[0])
print()

# Вывести усреднённую длину слова в предложении
sentence = 'Мы приехали в гости'
print(len(sentence.replace(' ', '')) / len(sentence.split()))