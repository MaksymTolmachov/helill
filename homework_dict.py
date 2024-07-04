"""
зауважте, що значення, що зберігається в кожному елементі - теж словник, і доступ до вкладеного списку 
здійснюється за механізмом 
student[outer_dict_key][inner_dict_key]

Є дані студентів (комбінація імені та прізвища унікальна), що зберігаються за допомогою словника
1 - програмно добавити одного студента, з заповненням усіх полів (вік - від 18 до 40, цілочисельне значення, 
    бал від 0 до 100 (інт чи флоат)
2 - створити і вивести на екран список студентів (імя та прізвище та середній бал), у яких середній бал більше 90
    сам формат наповнення цього списку up to you
3 - визначити середній бал по групі
4 - при відсутності номеру телефону у студента записати номер батьків (номер на ваш вибір)

не забувайте виводити інформаційні повідомлення щодо інформації, яку ви виводите
"""
students = {
    'Іван Петров': {
        'Пошта': 'Ivan@gmail.com',
        'Вік': 14,
        'Номер телефону': '+380987771221',
        'Середній бал': 95.8
    },
    'Женя Курич': {
        'Пошта': 'Geka@gmail.com',
        'Вік': 16,
        'Номер телефону': None,
        'Середній бал': 64.5
    },
    'Маша Кера': {
        'Пошта': 'Masha@gmail.com',
        'Вік': 18,
        'Номер телефону': '+380987126621',
        'Середній бал': 80
    },
}
# ваш код нижче !!!!!!!! вище нічого не змінюємо
from pywebio.input import input_group,slider, textarea, select, checkbox, radio, FLOAT, DATE, PASSWORD, DATETIME, input as input_pw
from pywebio.output import put_success, put_error, put_warning, put_html,put_table, put_image
from pywebio.session import run_js
from pywebio import start_server
from pprint import pprint

students["Alex Kolesnuk"] = {
    'Пошта': 'Alex.Kolesnuk2005@gmail.com',
    'Вік': 19,
    'Номер телефону': '+380096347829',
    'Середній бал': 74
}
#I DON'T KNOW WHAT TO DO
lowest_scour = 90
for student_name, data in students.items():
    print(student_name)
    if data["Середній бал"] >= lowest_scour :
        print(f"{student_name}, {data['Середній бал']}")

    # two_students_scours_1 = "Alex Kolesnuk"['Середній бал'] + "Маша Кера"['Середній бал']
    # print(two_students_scours_1)