print('\nЗадание №1 \n********Создание списка**********')
list_var = [1, True, "string_1", 3.14, (1, 2, 3), {'a': 'а', 'b': 'б', 'c': 'ц'}, {'q', 'w', 'e', 'r', 'e'}]
for el in list_var:
    print(type(el))

print('\nЗадание №2 \n*********Обмен значений***********')
input_var = None
input_list = []
# создание списка
while True:
    input_var = input('Введите один элемент списка. Для отмены нажмите ".": ')
    if input_var == '.':
        break
    input_list.append(input_var)
# Обмен значений
for i in range(0, len(input_list) - 1, 2):
    input_list[i], input_list[i + 1] = input_list[i + 1], input_list[i]
print(input_list)

print('\nЗадание №3 \n**********Времена года************')
dict_seasons = {1: "Зима", 2: "Зима",
                3: "Весна", 4: "Весна", 5: "Весна",
                6: "Лето", 7: "Лето", 8: "Лето",
                9: "Осень", 10: "Осень", 11: "Осень",
                12: "Зима"}

input_var = int(input('Введите номер месяца:  '))
# Вывод через словарь
dict_seasons = {((input_var == 12) or (1 <= input_var <= 2)): "Зима",
                3 <= input_var <= 5: "Весна",
                6 <= input_var <= 8: "Лето",
                9 <= input_var <= 11: "Осень"}
print(f"это {dict_seasons.get(True)}")

# Вывод через список
list_seasons = ["Зима", "Весна", "Лето", "Осень"]
el = None
if (input_var == 12) or (1 <= input_var <= 2):
    el = 0
elif 3 <= input_var <= 5:
    el = 1
elif 6 <= input_var <= 8:
    el = 2
elif 9 <= input_var <= 11:
    el = 3
else:
    print("Вы ввели некорректные данные")

if el is not None:
    print(f"это {list_seasons[el]}")

print('\nЗадание №4 \n**********Вывод слов************')
input_str = input('Введите строку из нескольких слов:  ')
list_str = input_str.split(' ')
for i in range(len(list_str)):
    print(f'{i}. {list_str[i][:10]}')

print('\nЗадание №5 \n************Рейтинг**************')
rating_list = [7, 5, 3, 3, 2]
input_el = input('Введите номер позиции рейтинга:  ')
el_pos = None
if input_el.isnumeric():
    input_num = int(input_el)
    # Если введено число, меньшее любого в списке, добавляем его в конец списка
    if input_num <= min(rating_list):
        rating_list.append(input_num)
        el_pos = len(rating_list)
    # Иначе ищем для него место
    else:
        for i, el in enumerate(rating_list):
            if input_num > el:
                rating_list.insert(i, input_num)
                el_pos = i
                break
else:
    print("Вы ввели некорректные данные")
print(f'новый рейтинг {rating_list} с новым элементом с индексом {el_pos}')

print('\nЗадание №6 \n************Рейтинг**************')
parameters = ['название', 'цена', 'количество', 'eд']
products_struct_list = []  # структура данных
while True:  # в каждой итерации добавляем один товар
    param_list = []  # значения параметров
    for param in parameters:  # заполняем значения параметров
        param_list.append(input(f'Введите {param} товара: '))
    param_dict = dict(zip(parameters, param_list))  # создаём словарь параметров {'параметр':'значение'}
    # создаём tuple с номером товара и его словарём параметров
    products_struct = tuple([len(products_struct_list) + 1, param_dict])
    # добавляем tuple в структру данных
    products_struct_list.append(products_struct)

    to_continue = input("Добавить следующий товар? (y|n) ")
    if to_continue == 'n':
        break

print(products_struct_list)

# исходим из условия, что нам не известны параметры товаров
param_list = []  # список параметров
analytics_dict = dict()  # структура с аналитикой

# извлекаем все параметры из структуры товаров
for product in products_struct_list:
    param_list.extend(list(list(product)[1].keys()))
# удаляем дубликаты
param_list = list(set(param_list))

# создаём структуру с аналитикой

# для каждого найденного параметра
for parameter in param_list:
    # обходим структуру товаров и получаем список значений
    param_values_list = []
    for product in products_struct_list:
        param_values_list.append(list(product)[1].get(parameter))
    # добавляем в структуру с аналитикой
    analytics_dict[parameter] = list(set(param_values_list))

print(analytics_dict)
