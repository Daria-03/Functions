def check_rhythm(poem):
 lines = poem.split() # Разделяем стихотворение на отдельные фразы
syllables = [] # Список для хранения количества слогов в каждой фразе

# Перебираем все фразы в стихотворении
for line in lines:
  words = line.split('-') # Разделяем фразу на отдельные слова
count = 0 # Счетчик слогов в фразе

# Перебираем все слова в фразе
for word in words:
  vowels = 0 # Счетчик гласных букв в слове

# Перебираем все буквы в слове
for letter in word:
 if letter.lower() in 'aeiouаеёиоуыэюя': # Проверяем, является ли буква гласной
  vowels += 1

count += vowels # Увеличиваем счетчик слогов на количество гласных в слове

syllables.append(count) # Добавляем количество слогов в текущей фразе в список

# Проверяем, одинаковое ли количество слогов в каждой фразе
if len(set(syllables)) == 1:
 return "Парам пам-пам"
else:
 return "Пам парам"

# Пример использования
try:
 poem = input("Введите стихотворение Винни-Пуха: ")
result = check_rhythm(poem)
print(result)
except KeyboardInterrupt:
print("Программа была прервана пользователем.")