

def printField(game_field: list):
    print(f'{game_field[0]:^5}|{game_field[1]:^5}|{game_field[2]:^5}')
    print('-----------------')
    print(f'{game_field[3]:^5}|{game_field[4]:^5}|{game_field[5]:^5}')
    print('-----------------')
    print(f'{game_field[6]:^5}|{game_field[7]:^5}|{game_field[8]:^5}\n\n')

def playerTurn(game_field: list, mark, name) -> int:
    while True:
        move = int(input(f'{name} делайте ваш ход: '))
        if (0 < move < 10) and game_field[move-1].isdigit():
            game_field[move-1] = mark
            return move
        else:
            print('Эта клетка занята! Сделайте другой ход')

def playerName():
    name = input('Введите имя игрока: ')
    return name



