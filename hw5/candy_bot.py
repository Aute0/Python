# Игра с конфетами. Дано N конфет. Каждый игрок за каждый ход может взять не более M конфет.
# Побеждает игрок,забравший последнюю конфету.

# man vs bot

from random import randint, choice

greeting = ('Здравствуйте! Игра "Забери все конфеты!" '
            'Нам будет дано некоторое количество конфет, '
            'за один ход мы можем взять не более того количества, '
            'о котором договоримся. '
            'Итак, поехали!')

messages = ['Ваша очередь брать конфеты', 'возьмите конфеты', 'Ваш ход']

def introduce_players():
    player1 = input('Как Вас зовут?\n')
    player2 = 'Бот'
    print(f'Очень приятно, меня зовут {player2}')
    return [player1, player2]

def get_rules(players):
    n = int(input('Сколько конфет будем разыгрывать?\n '))
    m = int(input('Сколько будем брать конфет за один ход?\n '))
    first = int(input(
        f'{players[0]}, если хотите ходить первым, нажмите 1, если нет, любую другую клавишу\n'))
    if first != 1:
        first = 0
    return [n, m, int(first)]

def play_game(rules, players, messages):
    count = rules[2]
    while rules[0] > 0:
        if not count % 2:
            move = randint(1, rules[1])
            print(f'Я забираю {move}')
        else:
            print(f'{players[0]}, {choice(messages)}')
            move = int(input())
        rules[0] = rules[0] - move
        if rules[0] > 0:
            print(f'Осталось {rules[0]} конфет')
        else:
            print('Все конфеты разобраны.')
        count += 1
    return players[count % 2]

print(greeting)

players = introduce_players()
rules = get_rules(players)

winer = play_game(rules, players, messages)
if not winer:
    print('У нас нет победителя.')
else:
    print(
        f'Поздравляю! В этот раз победил {winer}! Ему достаются все конфеты!')