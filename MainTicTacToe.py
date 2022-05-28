from Othello import Othello
import copy
t = Othello(8)

print()


def testBoard():
    for i in range(1, 65):
        if(i == 28 or i == 37):
            print("|{:>3}|".format('X'), end=' ')
            continue
        if(i == 29 or i == 36):
            print("|{:>3}|".format('O'), end=' ')
            continue
        print("|{:>3}|".format(i), end=' ')
        if i % 8 == 0:
            print()


def move_ia():
    max_score = -1000
    best_move = 0
    copy_board = copy.deepcopy(t.getBoard())
    copy_2 = copy.deepcopy(copy_board)
    for key in copy_board.keys():
        if copy_board[key] == ' ' and t.validate_rules(key, movIa, True):
            print("key: " + str(key))
    return best_move

# MinMax


def minmax(board, depth, isMax):
    if t.fullBoard() or depth == 0:
        return 0
    if isMax:
        best_score = -100
        for key in board.keys():
            if board[key] == ' ' and t.validate_rules(key, movIa, True):
                board[key] = movIa
                score = minmax(board, depth-1, False)
                board[key] = ' '
                if score > best_score:
                    best_score = score
        return best_score

    else:
        best_score = 800
        for key in board.keys():
            if board[key] == ' ' and t.validate_rules(key, movHuman, True):
                board[key] = movHuman
                score = minmax(board, depth-1, True)
                board[key] = ' '
                if score < best_score:
                    best_score = score
        return best_score

def ia(mov):
    pos = move_ia()
    print("POS IA " + mov + " :", pos)
    t.insert_move(pos, mov)


def human(mov):
    pos = int(input("POS Human " + mov + " :"))
    t.insert_move(pos, mov)


movHuman = 'O'  # Negro
movIa = 'X'  # Blanco
#while t.fullBoard() == False:
   #t.print_board()
   #print()
   #testBoard()
   #human(movHuman)    
   #ia(movIa)


# 20

testBoard()
print()
t.print_board()
print()
move_ia()