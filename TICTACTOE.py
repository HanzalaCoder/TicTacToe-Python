from random import choice
board = [" ", " ", " ",
         " ", " ", " ",
         " ", " ", " "]

PLAYER_ONE = "O"
PLAYER_TWO = "X"
CURRENT_PLAYER = choice(PLAYER_ONE + PLAYER_TWO)
MOVES = 0


def print_board():
    print(board[0] + "|" + board[1] + "|" + board[2] + "|")
    print("+-+-+-+")
    print(board[3] + "|" + board[4] + "|" + board[5] + "|")
    print("+-+-+-+")
    print(board[6] + "|" + board[7] + "|" + board[8] + "|")


def players_input():
    global MOVES
    while True:
        play = input(f"IT's {CURRENT_PLAYER} TURN SELECT FROM 1 TO 9: ")
        if play.isnumeric():
            try:
                play = int(play)
                if board[play - 1] == " ":
                    board[play - 1] = CURRENT_PLAYER
                    MOVES += 1
                    break
                else:
                    print("space taken")
            except IndexError:
                print("INVALID COMMAND!")
                continue


def check_tie():
    global MOVES
    if MOVES >= 9:
        return True
    else:
        return False


def switch():
    global CURRENT_PLAYER
    if CURRENT_PLAYER == PLAYER_ONE:
        CURRENT_PLAYER = PLAYER_TWO
        return CURRENT_PLAYER
    else:
        CURRENT_PLAYER = PLAYER_ONE
        return CURRENT_PLAYER


def check_win():
    if board[0] == board[1] == board[2] and board[1] != " ":
        return True
    elif board[3] == board[4] == board[5] and board[3] != " ":
        return True
    elif board[6] == board[7] == board[8] and board[6] != " ":
        return True
    elif board[0] == board[3] == board[6] and board[0] != " ":
        return True
    elif board[1] == board[4] == board[7] and board[1] != " ":
        return True
    elif board[2] == board[5] == board[8] and board[2] != " ":
        return True
    elif board[0] == board[4] == board[8] and board[0] != " ":
        return True
    elif board[2] == board[4] == board[6] and board[2] != " ":
        return True
    else:
        return False


def main():
    while True:
        print_board()
        players_input()
        if check_win() is True:
            print(f"WELL PLAYED {CURRENT_PLAYER} HAS WON The GAME")
            print_board()
            break
        elif check_tie() is True:
            print("IT's TIE WELL PLAYED")
            print_board()
            break
        switch()


if __name__ == "__main__":
    main()
