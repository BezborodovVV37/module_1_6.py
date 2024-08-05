my_dict = {'Василий': 1993, 'Алина': 1998}
print(my_dict)
my_dict.update({'Игорь': 2001, 'Катя': 2003})
print(my_dict)
print(my_dict.get('Екатерина', 'Такого значения нет'))
my_dict = {'Папа': 1972, 'Мама': 1973}
print(my_dict)
my_dict.pop('Мама')
print(my_dict)
my_set = {9, 8, 7, 6, 9, 8, 7, 6, (1, 2, 3, 4,), "Привет"}
print(my_set)
my_set.update({32, 61, 42})
print(my_set)
(my_set.discard(32))
print(my_set)



