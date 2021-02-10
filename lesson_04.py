from sys import argv
from functools import reduce
from itertools import cycle, count

print('\nЗадание №1 \n************* Расчет зарплаты *************')


def salary_calc(working_hours, hour_cost, add_bonus):
    """Salary calculation

    :param working_hours: float
    :param hour_cost: float
    :param add_bonus: float
    :return: float
    """
    return working_hours * hour_cost + add_bonus


# если были переданы параметры - выполнить функцию расчет зарплаты
if len(argv) > 1:
    hours, cost, bonus = argv[1:4]
    print(salary_calc(float(hours), float(cost), float(bonus)))


print('\nЗадание №2 \n****** Список с бОльшими элементами *******')
digits_list = [300, 2, 12, 44, 1, 1, 4, 10, 7, 1, 78, 123, 55]
new_list = [el for i, el in enumerate(digits_list) if (i > 0) & (digits_list[i] > digits_list[i-1])]
print(new_list)


print('\nЗадание №3 \n********** кратные 20 и 21 ***********')
print(f'числа от 20 до 240, кратные 20 и 21: {[el for el in range(20, 241) if (el % 20 == 0) | (el % 21 == 0)]}')

print('\nЗадание №4 \n****** элементы без повторений *******')
digits_list_1 = [2, 2, 2, 7, 23, 1, 44, 44, 3, 2, 10, 7, 4, 11]
new_digits_list_1 = [el for el in digits_list_1 if digits_list_1.count(el) == 1]
print(new_digits_list_1)


print('\nЗадание №5 \n************ reduce *************')
# получаем список четных чисел от 100 до 1000
list_100_1000 = [el for el in range(100, 1001) if el % 2 == 0]
# выводим произведение всех чисел списка
print(reduce(lambda x, y: x*y, list_100_1000))

print('\nЗадание №6 \n************ итераторы *************')
end_of_cycle = 10
for el in count(3):
    print(el)
    if el == end_of_cycle:
        break

counter = 1
rh_list = ["раз", "два", "три", "четыре", "пять"]
for el in cycle(rh_list):
    print(el)
    # закончим вывод элементов после трёх проходов
    if counter == len(rh_list) * 3:
        break
    counter += 1

print('\nЗадание №7 \n********** yield factorial ***********')


# генератор факториала
def fact(x):
    res_fact = 1
    for el in range(1, x+1):
        res_fact = el * res_fact
        yield res_fact


for el in fact(4):
    print(el)
