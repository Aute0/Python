# Pam Qian 2016 Fall CS 112 Python Midterm Project II
# Tic Tack Toe

def main():
    # The main function
    introduction = intro()
    board = create_grid()
    pretty = printPretty(board)
    player1, player2 = sym()
    # The function that starts the game is also in here.
    full = isFull(board, player1, player2)

def intro():
    # введем правила игры
    print("Привет! Это мой вариант игры в крестики-нолики. Я собрала его из нескольких вариантов из интернета\
        и постаралась разобраться в них. Приятной игры!")
    print("--------------------------------------------------------------------------------------------------")
    print("Правила: Игроки 1 и 2 принимают решения по очереди за Х и О выбирая место на сетке размером 3 на 3.\
        Тот, кто соберет три крестика или три нолика по горизонтали, вертикали или по\
             диагонали - выйграл!")
    print("--------------------------------------------------------------------------------------------------")
    input("Нажми enter и поехали!")
    print("--------------------------------------------------------------------------------------------------")

def create_grid():
    # Создаем игровое поле
    print("Это у нас игровое поле: ")
    board = [[" ", " ", " "],
             [" ", " ", " "],
             [" ", " ", " "]]
    return board

def sym():
    # Выберем символы для игроков
    player1 = input("Игрок 1, ты за Х или за О? ")
    if player1 == "X":
        player2 = "O"
        print("Игрок 2, тебе остался нолик О.")
    else:
        player2 = "X"
        print("Игрок 2, ты будешь играть Х. ")
    input("Жми enter!")
    print("\n")
    return (player1, player2)

def start(board, player1, player2, count):
    # Начинаем игру
    # Определяем ход
    if count % 2 == 0:
        player = player1
    elif count % 2 == 1:
        player = player2
    print("Игрок " + player + ", твой ход. ")
    row = int(input("Выбери строку:"
                    "[верхняя: жми 0, средняя: жми 1, нижняя: жми 2]:"))
    column = int(input("Выбери столбец:"
                       "[левый: жми 0, средний: жми 1, правый: жми 2]"))
    # расположим символ игрока на поле
    if player == player1:
        board[row][column] = player1

    else:
        board[row][column] = player2

    return (board)

def isFull(board, player1, player2):
    count = 1
    winner = True
# Проверка есть ои место на поле. До тех пор пока счет до 10 и нет победителя - играем!
    while count < 10 and winner == True:
        gaming = start(board, player1, player2, count)
        pretty = printPretty(board)
        if count == 9: # счет подошел к концу - игра окончена
            print("The board is full. Game over.")
            if winner == True:
                print("There is a tie. ") # Ничья!
        # Проверка, есть ли победитель
        winner = isWinner(board, player1, player2, count)
        count += 1
    if winner == False:
        print("Game over.")
    # Результат игры
    report(count, winner, player1, player2)

def printPretty(board):
    # Пусть будет красивое поле ^_^
    rows = len(board)
    cols = len(board)
    print("---+---+---")
    for r in range(rows):
        print(board[r][0], " |", board[r][1], "|", board[r][2])
        print("---+---+---")
    return board

def isWinner(board, player1, player2, count):
    # Проверка выйгрыша
    winner = True
    # Проверим строчки
    for row in range(0, 3):
        if (board[row][0] == board[row][1] == board[row][2] == player1):
            winner = False
            print("Игрок " + player1 + ", ты победил!")
        elif (board[row][0] == board[row][1] == board[row][2] == player2):
            winner = False
            print("Игрок " + player2 + ", ты победил!")
    # Проверим колонки
    for col in range(0, 3):
        if (board[0][col] == board[1][col] == board[2][col] == player1):
            winner = False
            print("Игрок " + player1 + ", ты победил!")
        elif (board[0][col] == board[1][col] == board[2][col] == player2):
            winner = False
            print("Игрок " + player2 + ", ты победил!")
    # Проверим дмагонали
    if board[0][0] == board[1][1] == board[2][2] == player1:
        winner = False
        print("Игрок " + player1 + ", ты победил!")
    elif board[0][0] == board[1][1] == board[2][2] == player2:
        winner = False
        print("Игрок " + player2 + ", ты победил!")
    elif board[0][2] == board[1][1] == board[2][0] == player1:
        winner = False
        print("Игрок " + player1 + ", ты победил!")
    elif board[0][2] == board[1][1] == board[2][0] == player2:
        winner = False
        print("Игрок " + player2 + ", ты победил!")
    return winner

def report(count, winner, player1, player2):
    print("\n")
    input("Жми enter чтобы увидеть результат. ")
    if (winner == False) and (count % 2 == 1):
        print("Победил : Игрок " + player1 + ".")
    elif (winner == False) and (count % 2 == 0):
        print("Победил : Игрок " + player2 + ".")
    else:
        print("There is a tie. ")

# Call Main
main()
