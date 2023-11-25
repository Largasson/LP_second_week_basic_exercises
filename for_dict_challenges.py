# Задание 1
# Дан список учеников, нужно посчитать количество повторений каждого имени ученика
# Пример вывода:
# Вася: 1
# Маша: 2
# Петя: 2
print('Задание 1')
students = [
    {'first_name': 'Вася'},
    {'first_name': 'Петя'},
    {'first_name': 'Маша'},
    {'first_name': 'Маша'},
    {'first_name': 'Петя'},
]
names = {}
for line in students:
    names[line['first_name']] = names.setdefault(line['first_name'], 0) + 1

for name, count in names.items():
    print(f"{name}: {count}")
print()

print('Задание 2')
# Задание 2
# Дан список учеников, нужно вывести самое часто повторящееся имя
# Пример вывода:
# Самое частое имя среди учеников: Маша
students = [
    {'first_name': 'Вася'},
    {'first_name': 'Петя'},
    {'first_name': 'Маша'},
    {'first_name': 'Маша'},
    {'first_name': 'Оля'},
]
names = {}
for line in students:
    names[line['first_name']] = names.setdefault(line['first_name'], 0) + 1
max_value, target_name = 0 , ''
for name, value in names.items():
    if value > max_value:
        max_value, target_name = value, name
print(f"Самое частое имя среди учеников: {target_name}")
print()

print('Задание 3')
# Задание 3
# Есть список учеников в нескольких классах, нужно вывести самое частое имя в каждом классе.
# Пример вывода:
# Самое частое имя в классе 1: Вася
# Самое частое имя в классе 2: Маша

school_students = [
    [  # это – первый класс
        {'first_name': 'Вася'},
        {'first_name': 'Вася'},
    ],
    [  # это – второй класс
        {'first_name': 'Маша'},
        {'first_name': 'Маша'},
        {'first_name': 'Оля'},
    ],[  # это – третий класс
        {'first_name': 'Женя'},
        {'first_name': 'Петя'},
        {'first_name': 'Женя'},
        {'first_name': 'Саша'},
    ],
]
names = {}
for clas in school_students:
    for line in clas:
        names[line['first_name']] = names.setdefault(line['first_name'], 0) + 1
    max_value, target_name = 0 , ''
    for name, value in names.items():
        if value > max_value:
            max_value, target_name = value, name
    print(f"Самое частое имя среди учеников: {target_name}")
    names.clear()
print()

print('Задание 4')
# Задание 4
# Для каждого класса нужно вывести количество девочек и мальчиков в нём.
# Пример вывода:
# Класс 2a: девочки 2, мальчики 0
# Класс 2б: девочки 0, мальчики 2

school = [
    {'class': '2a', 'students': [{'first_name': 'Маша'}, {'first_name': 'Оля'}]},
    {'class': '2б', 'students': [{'first_name': 'Олег'}, {'first_name': 'Миша'}]},
    {'class': '2в', 'students': [{'first_name': 'Даша'}, {'first_name': 'Олег'}, {'first_name': 'Маша'}]},
]
is_male = {
    'Олег': True,
    'Маша': False,
    'Оля': False,
    'Миша': True,
    'Даша': False,
}

for clas in school:
    sex = {False: 0, True: 0}
    for student in clas['students']:
       sex[is_male[student['first_name']]] = sex.setdefault(is_male[student['first_name']], 0) + 1
    print(f"{clas['class']}: девочки {sex[False]}, мальчики {sex[True]}")
    sex.clear()
print()

print('Задание 5')
# Задание 5
# По информации о учениках разных классов нужно найти класс, в котором больше всего девочек и больше всего мальчиков
# Пример вывода:
# Больше всего мальчиков в классе 3c
# Больше всего девочек в классе 2a

school = [
    {'class': '2a', 'students': [{'first_name': 'Маша'}, {'first_name': 'Оля'}]},
    {'class': '3c', 'students': [{'first_name': 'Олег'}, {'first_name': 'Миша'}]},
]
is_male = {
    'Маша': False,
    'Оля': False,
    'Олег': True,
    'Миша': True,
}
gerl_max, gerl_class = 0, ''
boy_max, boy_class = 0, ''
for clas in school:
    sex = {False: 0, True: 0}
    for student in clas['students']:
       sex[is_male[student['first_name']]] = sex.setdefault(is_male[student['first_name']], 0) + 1
    if sex[False] > gerl_max:
        gerl_max, gerl_class = sex[False], clas['class']
    if sex[True] > boy_max:
        boy_max, boy_class = sex[True], clas['class']
    sex.clear()
print(f"Больше всего мальчиков в классе {boy_class}")
print(f"Больше всего девочек в классе {gerl_class}")