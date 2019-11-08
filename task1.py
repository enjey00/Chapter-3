words = list(input('Введите слово: '))

list1 = []
list2 = []

for letter in words:
    if letter.isupper():
        list1.append(letter)
    elif letter.islower():
        list2.append(letter)

sum_of_upper_letters = len(list1)
sum_of_lower_letters = len(list2)
sum_of_all_letters = len(words)

percent_of_upper = round((sum_of_upper_letters/sum_of_all_letters)*100, 2)
percent_of_lower = round((sum_of_lower_letters/sum_of_all_letters)*100, 2)

print(f'Всего в слове {sum_of_all_letters} букв.')
print(f'Из них {percent_of_upper}% написаны в вверхнем регистре.')
print(f'А {percent_of_lower}% написаны в нижнем регистре.')