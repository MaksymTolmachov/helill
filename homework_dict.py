﻿"""
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


students["Alex Kolesnuk"] = {
    'Пошта': 'Alex.Kolesnuk2005@gmail.com',
    'Вік': 19,
    'Номер телефону': '+380096347829',
    'Середній бал': 90
}

lowest_scour = 90
total_coumlate_score = 0
for student_name, data in students.items():
    if data["Середній бал"] >= lowest_scour :
        print(f"{student_name}, {data['Середній бал']}, {data['Вік']} years old")

    all_scores_altogether = total_coumlate_score =+ data["Середній бал"]
    result = all_scores_altogether / len(students)



    if data['Номер телефону'] is None:
        data['Номер телефону'] = "+380096875201"
        print(data['Номер телефону'])
print(total_coumlate_score)














