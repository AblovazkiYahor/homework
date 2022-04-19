# - Запрашивает у пользователя имя и возраст;
# - Проверяет минимальный возраст 14;
# - Проверяет, что имя введено и минимальное количество символов в имени — 3;
# - Проверяет возраст на отрицательное число или 0;
# - Проверяет имя на пустоту;
# * Проверяет, что:
# - возраст возраст 16-17 лет и нужно не забыть получить первый паспорт;
# - возраст 25-26 лет и нужно заменить паспорт;
# - возраст 45-46 лет и нужно второй раз заменить паспорт;
# - Выводит либо текст с ошибкой (по каждому условию разный текст ошибки), либо приветствие пользователя с его именем (с заглавной буквы), указанием возраста и *советом получить/заменить паспорт (если совет актуален).
# * Совет с паспортом выводить только в том случае, если отображается приветствие.
#


name = str(input('What is your name?'))
age = int(input('How old are you?'))
btn1 = str('')

if name == btn1:
    res = 'Name field is not inputed!'
elif len(name) < 4:
    res = '[Error_name]: Input valid name (Min minimum number of characters - 3)'
elif age <= 0:
    res = '[Error_age_1]: You entered a negative number or zero'
elif 0 > age < 14:
    res = f'[Error_age_2]: Hi {name}! You are under 14 years old, you will not be able to get a passport'
elif 14 >= age < 26:
    res = f'[Age_info_2]: Hi, {name}.You are {age} old! Don_t forget to change your passport at 25'
else:
    res = f'[MESS_OK]: Hi, {name}! You are {age} old!'
print(res)













