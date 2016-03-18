from random import randint

board = []

for x in range(5):
    board.append(["O"] * 5)

def print_board(board):
    for row in board:
        print " ".join(row)

print "Let's play Battleship!"
print_board(board)

def random_row(board):
    return randint(0, len(board) - 1)

def random_col(board):
    return randint(0, len(board) - 1)

str(ship_row) = random_row(board)
str(ship_col) = random_col(board)
#print ship_row
#print ship_col

for turn in range(4):
    #guess_test = raw_input("guess test: ")
    guess_row = int(raw_input("Guess Row:")) - 1
    guess_col = int(raw_input("Guess Col:")) - 1

    if guess_row == ship_row and guess_col == ship_col:
        print "Congratulations! You sunk my battleship!" 
        break
        
    elif guess_row not in range(5) or  \
    guess_col not in range(5) or type(guess_row) == "":
        print "Oops, that's not even in the ocean."
    
    
    elif(board[guess_row][guess_col] == "X"):
        print "You guessed that one already."
        if turn == 3:
            print "Game Over"
    
    else:
        print "You missed my battleship!"
        board[guess_row][guess_col] = "X"
        if turn == 0:
            print 'You have had 1 turn'
            turn + 1
        elif turn == 1:
            print 'You have had 2 turns'
            turn + 1
        elif turn == 2:
            print 'You have had 3 turns, 1 more remaining:'
            turn + 1
        print_board(board)
        if turn == 3:
            print "Game Over"