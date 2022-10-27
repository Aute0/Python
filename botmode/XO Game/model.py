

game_field = ['1','2','3','4','5','6','7','8','9']
player_field = [0, 0, 0, 0, 0, 0, 0, 0, 0]
enemy_field = [0, 0, 0, 0, 0, 0, 0, 0, 0]
mark = 'X'
win = [(0,1,2), (3,4,5), (6,7,8), (0,3,6),
            (1,4,7), (2,5,8), (0,4,8), (2,4,6)]
name = ''


def getMark() -> str:
    global mark
    return mark

def changeMark():
    global mark
    if mark == 'O':
        mark = 'X'
    else:
        mark = 'O'

def getName():
    global name
    return name

def setName(new_name: str):
    global name
    name = new_name

def getField():
    global game_field
    return game_field

def setPlayerMove(move:int):
    global player_field
    player_field[move-1] = 1

def setEnemyMove(move:int):
    global enemy_field
    enemy_field[move] = 1

def getPlayerField():
    global player_field
    return player_field

def getEnemyField():
    global enemy_field
    return enemy_field

def win_condition(field: list):
    global win
    for move in win:
        if field[move[0]] == field[move[1]] == field[move[2]] == 1:
            return True