''' 
    Привет Яна! попал к вам на поток т.к не успевал за своим из-за некоторых своих заморочек 
    надеюсь у вас успею всё!
    Не присутствовал на вебинарах (по вполне прозрачным причинам) поэтому буду общятся и задавать вопросы
    через свой код - домашние задание. 
'''
# функция вывода данных о пользователе

def print_user_info(name: str, sure_name: str, age: int):
    # если имя или фамилия введены не с занлавной буковки 
    name = name[0].capitalize() + name[1:]
    sure_name = sure_name[0].capitalize() + sure_name[1:]
    # вывод данных
    print(f"Меня зовут {name} {sure_name}. Мой возраст - {age}")

'''
# Немного обо мне.
my_name = 'Артём'
my_sure_name = 'Ващенко'
my_age = 15
print_user_info(my_name, my_sure_name, my_age)
'''

user_name = str(input("Введите ваше имя - "))
user_sure_name = str(input("Введите вашу фамилию - "))
user_age = int(input("Введите ваш возраст - "))

print_user_info(user_name, user_sure_name, user_age)

