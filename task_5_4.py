# Создайте программу для игры в "Крестики-нолики".

# Возможно, сделано грубовато (на курсе по C# мы проходили матрицы из двухуровневого массива), но здесь мне так показалось проще.

my_list = ['1', '2', '3', '4', '5', '6', '7', '8', '9'] 
turn = 0


# Далее функция, которая определяет, выполняются ли условия победы в игре. Опять же, выглядит это не очень профессионально, но работает
# Буду рад комментам, как можно это все упростить или оптимизировать, например избежать длинных фраз после if/elif или возвращать значение True/False, а не строку "win".
def win_condition():
    if my_list[0] == my_list[1] == my_list[2] or my_list[3] == my_list[4] == my_list[5] or my_list[6] == my_list[7] == my_list[8]:
        return "win"
    elif my_list[0] == my_list[3] == my_list[6] or my_list[1] == my_list[4] == my_list[7] or my_list[2] == my_list[5] == my_list[8]:
        return "win"
    elif my_list[0] == my_list[4] == my_list[8] or my_list[2] == my_list[4] == my_list[6]:
        return "win"
    elif turn == 9:
        return "draw"
    else:
        return " " 

# Гуглил, но не нашел, как в Питоне реализовать очистку консоли перед каждым последующим выводом, чтобы для пользователя было видно только одно "игровое поле"
def print_result():
    return f' {my_list[0]} {my_list[1]} {my_list[2]} \n {my_list[3]} {my_list[4]} {my_list[5]} \n {my_list[6]} {my_list[7]} {my_list[8]}'

print(print_result())

while True:
    my_input = int(input('ИГРОК 1. Укажите номер клетки, где вы хотите поставить КРЕСТИК: '))
    
    while my_list[my_input - 1] != str(my_input):
        my_input = int(input('Эта клетка уже занята, попробуйте сделать другой ход: '))
    my_list[my_input - 1] = "X"
    turn += 1

    print(print_result())
    if win_condition() == "win":
        print("Победил 1 игрок!")
        break
    elif win_condition() == "draw":
        print("Игра окончена с ничейным результатом.")
        break

    my_input = int(input('ИГРОК 2. Укажите номер клетки, где вы хотите поставить НОЛИК: '))
    
    while my_list[my_input - 1] != str(my_input):
        my_input = int(input('Эта клетка уже занята, попробуйте сделать другой ход: '))
    my_list[my_input - 1] = "0"
    turn += 1

    print(print_result())
    if win_condition() == "win":
        print("Победил 2 игрок!")
        break
    elif win_condition() == "draw":
        print("Игра окончена с ничейным результатом.")
        break
    