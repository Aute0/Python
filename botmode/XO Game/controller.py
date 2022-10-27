import bot
import model
import view

def intro():
    name = view.playerName()
    model.setName(name)


def printField():
    field = model.getField()
    view.printField(field)

def playerTurn():
    field = model.getField()
    mark = model.getMark()
    name = model.getName()
    move = view.playerTurn(field, mark, name)
    model.setPlayerMove(move)
    printField()
    player_field = model.getPlayerField()
    if model.win_condition(player_field):
        print(f'Победил {name}!')
        return
    model.changeMark()
    enemyTurn()

def enemyTurn():
    field = model.getField()
    mark = model.getMark()
    enemy_field = model.getEnemyField()
    player_field = model.getPlayerField()
    move = bot.AIMove(field, player_field, enemy_field, model.win)

    field[move] = mark
    model.setEnemyMove(move)
    printField()
    enemy_field = model.getEnemyField()
    if model.win_condition(enemy_field):
        print('Победил компутер!')
        return
    model.changeMark()
    playerTurn()
