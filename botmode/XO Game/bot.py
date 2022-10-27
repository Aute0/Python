import random


def AIMove(field: list, player_field: list, enemy_field: list, win: list):
    if field[4].isdigit():
        return 4
    for pos in win:
        if (enemy_field[pos[0]] and enemy_field[pos[1]]):
            return int(pos[2])
        elif (enemy_field[pos[0]] and enemy_field[pos[2]]):
            return int(pos[1])
        elif (enemy_field[pos[1]] and enemy_field[pos[2]]):
            return int(pos[0])
    for pos in win:
        if (player_field[pos[0]] and player_field[pos[1]]):
            return int(pos[2])
        elif (player_field[pos[0]] and player_field[pos[2]]):
            return int(pos[1])
        elif (player_field[pos[1]] and player_field[pos[2]]):
            return int(pos[0])
    corner = [0,2,6,8]
    random.shuffle(corner)
    for pos in corner:
        if field[pos].isdigit():
            return int(pos)
    while True:
        move = random.randint(0,9)
        if (0 < move < 10) and field[move].isdigit():
            return move



