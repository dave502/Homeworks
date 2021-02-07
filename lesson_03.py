print('\nЗадание №1 \n************* Функция деления *************')


def division(dividend, divider):
    """Производит деление аргументов

    :param dividend: int or float - делимое
    :param divider: int or float - делитель
    :return: float - результат деления dividend / divider
    """
    try:
        dividend = float(dividend)
        divider = float(divider)

        if divider != 0:
            return dividend / divider
        else:
            print('На ноль делить нельзя')
        # или
        # try:
        #     return dividend / divider
        # except ZeroDivisionError:
        #     print('Ошибка! На ноль делить нельзя.')

    except ValueError:
        print('Вы ввели значения, не являющиеся числами')

    return


a = input('Введите число (делимое): ')
b = input('Введите число (делитель): ')
print(division(a, b))

print('\nЗадание №2 \n**** Функция вывода данных пользователя ****')


def print_personal_data(name, surname, year_of_birth, city, email, phone):
    """Выводит данные о пользоветеле одной строкой

    :param name: str
    :param surname: str
    :param year_of_birth: str
    :param city: str
    :param email: str
    :param phone: str
    :return: None
    """
    print(f'{name:15} | {surname:15} | {year_of_birth:10} | {city:15} | {email:20} | {phone:13}')


print_personal_data(surname='Иванов', name='Витя', city='Иваново',
                    phone='899112345678', email='ivanov2000@mail.ru', year_of_birth='2000')

print('\nЗадание №3 \n**** Сумма двух максимальных значений ****')


def my_func(var1, var2, var3):
    """Возвращает сумму двух максимальных аргументов

    :param var1: int or float
    :param var2: int or float
    :param var3: int or float
    :return: float
    """
    numeric_list = []

    try:
        # на случай, если было переданно не числовое значение
        numeric_list = list(map(float, [var1, var2, var3]))
    except ValueError:
        print('Вы ввели значения, не являющиеся числами')
        return

    # сортируем список по возрастанию и суммируем второе и третье значение, исключая наименьшее
    return sum(sorted(numeric_list, reverse=True)[:2])


print(my_func(9.6, 6, '8'))

print('\nЗадание №4 \n**** Возведение в степень ****')


def my_func(x: float, y: int):
    """Возведение в отрицательную степень (с помощью оператора **)

    :param x: float positive
    :param y: int negative
    :return: float
    """
    try:
        x = float(x)
        y = int(y)

        if (type(x) == float) & (x > 0) & (type(y) == int) & (y < 0):
            return x ** y
        else:
            print("Некорретный тип данных. Ожидаются действительное "
                  "положительное число x и целое отрицательное число y")
    except ValueError:
        print("Некорретный тип данных. Ожидаются действительное "
              "положительное число x и целое отрицательное число y")


print(my_func(5, '-3'))


def my_func1(x: float, y: int):
    """Возведение в отрицательную степень (с помощью цикла)

    :param x: float positive
    :param y: int negative
    :return: float
    """
    try:
        x = float(x)
        y = int(y)

        if (type(x) == float) & (x > 0) & (type(y) == int) & (y < 0):
            epx_x = x
            for i in range(abs(y) - 1):
                epx_x *= x
            return 1 / epx_x
        else:
            print("Некорретный тип данных. Ожидаются действительное "
                  "положительное число x и целое отрицательное число y")
    except ValueError:
        print("Некорретный тип данных. Ожидаются действительное "
              "положительное число x и целое отрицательное число y")


print(my_func1(5, '-3'))

print('\nЗадание №5 \n**** Сумма чисел из строки ****')


def sum_str():
    result = 0
    continue_cycle = True
    while continue_cycle:
        str_numbers = []
        list_numbers = []
        input_string = input('Введите строку чисел, разделенных пробелом. '
                             'Для завершения введите "/": ')
        # ищем в строке символ остановки
        pos_end = input_string.find('/')
        # если найден - это последний цикл, обрезаем строку
        if pos_end >= 0:
            continue_cycle = False
            input_string = input_string[:pos_end]

        str_numbers = input_string.strip().split(' ')

        # если строка не пустая
        if len("".join(str_numbers)):
            try:
                # на случай, если было переданно не числовое значение
                list_numbers = list(map(float, str_numbers))
            except ValueError:
                print('Вы ввели значения, не являющиеся числами')
                return

            result += sum(list_numbers)

        print(f'Сумма введённых чисел: {result}')


sum_str()

print('\nЗадание №6 \n**** Слова с заглавными буквами ****')


def int_func(in_string: str):
    """Возвращает слово с заглавной буквой

    :param in_string: str
    :return:  str
    """
    # удаляем лишние пробелы
    in_string = in_string.strip()

    if in_string.isalpha():
        return in_string.title()
    else:
        print("Введены некорректные данные")
        return None


print(int_func('JHJKJG'))

sentence = input('Введите предложение из нескольких слов: ')

next_word = True  # условие продолжения цикла
start_with = 0  # начало следующего слова
end_word = 0  # конец следующего слова
sentence = sentence.strip()  # удаляем лишние пробелы
new_sentence = ""  # переменная для нового предложения

while next_word:
    # ищем следующий пробел - конец слова, начиная с найденного предыдущего прибела
    end_word = sentence.find(' ', start_with)
    # если нашли - передаём слово перед пробелом в функцию
    if end_word >= 0:
        new_sentence += int_func(sentence[start_with:end_word].strip()) + ' '
        # следующий поиск пробела начнётся с позиции, следующей после найденного в этом цикле пробела
        start_with = end_word + 1
    # если не нашли - значит это последнее слово, заканчиваем цикл
    else:
        new_sentence += int_func(sentence[start_with:].strip())
        next_word = False

print(new_sentence)

# или более простой способ
# создаём список слов из предложения
words_list = [i.strip() for i in sentence.split(' ')]
# делаем заглавными буквы всех слов
title_words_list = list(map(int_func, words_list))
# разделяем слова пробелами и ковертируем в предложение
new_sentence = "".join(list(map(lambda x: x+' ', title_words_list))).strip()

print(new_sentence)

