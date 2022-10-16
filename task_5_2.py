# Создайте программу для игры с конфетами человек против человека.
# Условие задачи: На столе лежит 2021 конфета. Играют два игрока делая ход друг после друга. Первый ход определяется жеребьёвкой. 
# За один ход можно забрать не более чем 28 конфет. Все конфеты оппонента достаются сделавшему последний ход. 
# Сколько конфет нужно взять первому игроку, чтобы забрать все конфеты у своего конкурента?
# a) Добавьте игру против бота
# b) Подумайте как наделить бота ""интеллектом""

import random

# Возможно, эти две функции, что называется, YAGNI, но хотелось, чтобы текст смотрелся аккуратнее для всех числовых значений. 
# Буду рад комментам о том, насколько адекватно это реализовано. 
def nom_case_plural(x):
    if x % 10 == 1 and x % 100 != 11:
        return "конфета"
    elif x % 10 == 0 or x % 10 > 4 or x % 100 > 4 and (x % 100) % 10 > 4 or x % 100 > 10 and x % 100 < 21:  
        return "конфет"
    else:
        return "конфеты"
    
def acc_case_plural(x):
    if x % 10 == 1 and x % 100 != 11:
        return "конфету"
    elif x % 10 == 0 or x % 10 > 4 or x % 100 > 4 and (x % 100) % 10 > 4 or x % 100 > 10 and x % 100 < 21:   
        return "конфет"
    else:
        return "конфеты"

print("Привет! Это игра '2021 конфета'. \n \nПравила игры: каждый игрок по очереди берет от 1 до 28 конфет. \n\
Побеждает тот, кто забрал последнюю конфету. \n2021 конфета - это очень много, поэтому их количество будет не больше 300 и оно будет определяться случайным образом.")


candy_number = random.randint(200, 300)


press_enter = input("Давайте решим, кто начинает первым. Кинем кубик. Просто нажмите кнопку 'enter'.")
# while press_enter != "":
#     press_enter = input("Ничего вводить не надо, просто нажми кнопку 'enter'.")
dice_one = random.randint(1, 6)
print(f"Вы выкинули {dice_one}.")
dice_two = random.randint(1, 6)
print(f"Ваш соперник выкинул {dice_two}")

count = 0

while dice_one == dice_two:
    press_enter = input("вы выкинули одинаковые значения. Кидайте кубик еще раз. Просто нажмите 'enter'.")
    # if press_enter == "":
    dice_one = random.randint(1, 6)
    print(f"Вы выкинули {dice_one}.")
    dice_two = random.randint(1, 6)
    print(f"Ваш соперник выкинул {dice_two}")

if dice_one > dice_two:
    print(f"Итак, вы начинаете первым. На столе {candy_number} конфеты.")

else:
    print("Ваш соперник начинает первым.\n")
    user_2 = candy_number - count - int((candy_number - count) / 29) * 29
    # для разнообразия поставил "интеллекту" рандомное число, если игрок делает все правильно и берет остаток от деления числа конфет на 29. 
    if user_2 == 0:
        user_2 = random.randint(1, 29)

    print(f"Ваш соперник взял {user_2} {acc_case_plural(user_2)}.")
    count += user_2
    print(f"Осталось {candy_number - count} {nom_case_plural(candy_number - count)}.\n")


while count < candy_number:
    user_1 = input("Сколько конфет вы возьмете: ")
    while not user_1.isdigit():
        user_1 = input("Введите число от 1 до 28. Сколько конфет вы возьмете: ")
    while int(user_1) > 28 or int(user_1) < 1:
            user_1 = input(f"Можно взять не меньше 1 и не больше 28 конфет. Попробуйте еще, осталось {candy_number - count} {nom_case_plural(candy_number - count)}: ")
    count += int(user_1)
    if count >= candy_number:
        print("Конфет больше не осталось. Поздравляю, вы выиграли...\n")
        break

    # Собственно, отсюда начинается "искусственный интеллект".
    # я добавил переменную chance и проверку на нее, чтобы компьютер ошибся и дал игроку небольшой шанс, особенно если он начинает вторым.
    # но чтобы компьютер не тупил, когда остается мало конфет я добавил условие, что шанс выпадает, когда конфет больше 58.  
    chance = random.randint(1, 5)
    if chance == 5 and candy_number - count > 58:
        user_2 = random.randint(1, 29)
    else:
        user_2 = candy_number - count - int((candy_number - count) / 29) * 29
    # для разнообразия поставил "интеллекту" рандомное число, если игрок делает все правильно и берет остаток от деления числа конфет на 29. 
    if user_2 == 0:
        user_2 = random.randint(1, 29)

    print(f"Ваш соперник взял {user_2} {acc_case_plural(user_2)}.")
    count += user_2

    if count >= candy_number:
        print("Конфет больше не осталось. Вы проиграли.\n")
        break

    print(f"Осталось {candy_number - count} {nom_case_plural(candy_number - count)}.\n")