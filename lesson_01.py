
print('\nЗадание №1 \n***************************************')

а = 10
b = 'string'
c = 3.14
d = False
print(f'{а=}, {b=}, {c=}, {d=}')

а = int(input('Введите число '))
b = input('Введите строку ')
c = float(input('Ещё раз число '))
d = bool(int(input('Продолжать? (0/1) ')))

print(f'Теперь переменные равны {а=}, {b=}, {c=}, {d=}')

print('\nЗадание №2 \n***************************************')
total_seconds = int(input('Введите количество секунд '))
hours = total_seconds // (60 * 60)
minutes = (total_seconds - hours * 60 * 60) // 60
seconds = (total_seconds - hours * 60 * 60 - minutes * 60) % 60

print('Время {:02d}:{:02d}:{:02d}'.format(hours, minutes, seconds))

print('\nЗадание №3 \n***************************************')
num = input('Введите число ')
a, b, c = int(num), int(num * 2), int(num * 3)
print(f'n + nn + nnn = {a + b + c}')

print('\nЗадание №4 \n***************************************')
num = int(input('Введите число '))
max_num = 0
while True:

    high_num = num // 10
    digit = num - high_num * 10
    if digit > max_num:
        max_num = digit

    if high_num == 0:
        break
    else:
        num = high_num

print(f'Самая большая цифра из числа - {max_num}')

print('\nЗадание №5 \n***************************************')
proceeds = float(input('Введите размер выручки '))
costs = float(input('Введите размер издержек '))

if proceeds > costs:
    print('Фирма работает в прибыль. Рентабельность - %.2f' % (proceeds/costs))

    stuff = int(input('Введите количество сотрудников '))
    print('Прибыль на каждого сотрудника - %.2f у.е.' % ((proceeds-costs) / stuff))

elif proceeds < costs:
    print('Фирма работает в убыток')
elif proceeds == costs:
    print('Фирма работает в 0')


print('\nЗадание №6 \n***************************************')
first_distance = float(input('Сколько км спортсмен пробежал в первый день? '))
end_distance = float(input('Сколько км спортсмен должен пробежать в n-ый день? '))
n_distance = first_distance
day = 1

while n_distance < end_distance:
    n_distance = n_distance * 1.1
    day += 1
print(f'На {day}-й день спортсмен пробежит {n_distance:.2f} км')
