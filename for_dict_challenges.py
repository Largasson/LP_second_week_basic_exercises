from collections import defaultdict


def count_max(d):
    return (max(d.items(), key=lambda item: item[1]))[0]

def def_value():
    return 0


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
names = defaultdict(int)
for line in students:
    names[line['first_name']] += 1
for name, count in names.items():
    print(f"{name}: {count}")
print()

print('Задание 2')
# Задание 2
# Дан список учеников, нужно вывести самое часто повторяющееся имя
# Пример вывода:
# Самое частое имя среди учеников: Маша
students = [
    {'first_name': 'Вася'},
    {'first_name': 'Петя'},
    {'first_name': 'Маша'},
    {'first_name': 'Маша'},
    {'first_name': 'Оля'},
]
names = defaultdict(int)

for line in students:
    names[line['first_name']] += 1
print(f"Самое частое имя среди учеников: {count_max(names)}")
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
    ], [  # это – третий класс
        {'first_name': 'Женя'},
        {'first_name': 'Петя'},
        {'first_name': 'Женя'},
        {'first_name': 'Саша'},
    ],
]
names = defaultdict(int)
for clas in school_students:
    for line in clas:
        names[line['first_name']] += 1
    print(f"Самое частое имя среди учеников: {count_max(names)}")
    names = defaultdict(int)
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

is_male_2 = {name: 'boy' if sex else 'girl' for name, sex in is_male.items()}

for school_class in school:
    count_students = defaultdict(int)
    for student in school_class['students']:
        sex_key = is_male_2[student['first_name']]
        count_students[sex_key] += 1
    print(f"{school_class['class']}: девочки {count_students['girl']}, мальчики {count_students['boy']}")
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
# Накопление информации идет не так как в предыдущих примерах.
# Функцию применить наверное можно, но мне кажется, что код еще больше увеличится.
is_male_2 = {name: 'boy' if sex else 'girl' for name, sex in is_male.items()}
girl_max, girl_class = 0, ''
boy_max, boy_class = 0, ''
for clas in school:
    count_students = defaultdict(def_value)
    for student in clas['students']:
        sex_key = is_male_2[student['first_name']]
        count_students[sex_key] += 1
    if count_students['girl'] > girl_max:
        girl_max, girl_class = count_students['girl'], clas['class']
    if count_students['boy'] > boy_max:
        boy_max, boy_class = count_students['boy'], clas['class']
    count_students.clear()
print(f"Больше всего мальчиков в классе {boy_class}")
print(f"Больше всего девочек в классе {girl_class}")
