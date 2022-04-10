def greet():
    print('*************************************')
    print('******** Добро пожаловать! **********')
    print('**             Игра                **')
    print('**        Крестики Нолики          **')
    print('**        x - номер строки         **')
    print('**        y - номер столбца        **')
    print('*************************************')

def field():
    print("-------------")
    print(f"    0 | 1 | 2")
    print('_______________')
    for i, row in enumerate(box):
        row_str = f"{i} | {' | '.join(row)} |"
        print(row_str)
        print('_______________')
    print()

def ask():
  while True:
        cords = input("     Ваш ход:").split()

        if len(cords) != 2:
            print("Введите 2 координаты!")
            continue

        x, y = cords

        if not (x.isdigit()) or not (y.isdigit()):
            print("Введите числа!")
            continue

        x, y = int(x), int(y)

        if 0 > x or x > 2 or 0 > y or y > 2:
            print("Координаты вне диапазона")
            continue

        if box[x][y] != " ":
            print("Клетка занята!")
            continue

        return x, y

def check_win():
    win_cord = [((0, 0), (0, 1), (0, 2)), ((1, 0), (1, 1), (1, 2)), ((2, 0), (2, 1), (2, 2)), ((0, 2), (1, 1), (2, 0)), ((0, 0), (1, 1), (2, 2)), ((0, 0), (1, 0), (2, 0)), ((0, 1), (1, 1), (2, 1)), ((0, 2), (1, 2), (2, 2))]
    for card in win_cord:
        symbols = []
        for c in card:
            symbols.append(box[c[0]][c[1]])
            if symbols == ["X", "X", "X"]:
                print("Выйграл X!!!")
                return True
            if symbols == ["0", "0", "0"]:
                print("Выйграл 0!!!")
                return True
        return False

greet()
box = [[" "] * 3 for i in range(3)]
count = 0
while True:
    count += 1
    field()
    if count % 2 == 1:
        print("Ходит крестик!")
    else:
        print("Ходит нолик!")
    x, y = ask()
    if count % 2 == 1:
        box[x][y] = "X"
    else:
        box[x][y] = "0"

    if check_win():
        break

    if count == 9:
        print("Ничья!")
        break