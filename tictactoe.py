def display_board(board):
    print('\n' * 100)
    print(board[7] + '|' + board[8] + '|' + board[9])
    print(board[4] + '|' + board[5] + '|' + board[6])
    print(board[1] + '|' + board[2] + '|' + board[3])


def player_input():
    marker = ''

    while marker != 'X' and marker != 'O':
        marker = input('Player1! Choose a marker X or O: ').upper()

    player1 = marker

    if player1 == 'O':
        player2 = 'X'
    else:
        player2 = 'O'

    return (player1, player2)


def place_marker(board,marker,position):
    board[position] = marker


def win_check(board,marker):
    return ((board[7]==board[8]==board[9]==marker) or (board[4]==board[5]==board[6]==marker) or
           (board[1]==board[2]==board[3]==marker) or (board[7]==board[4]==board[1]==marker) or
           (board[8]==board[5]==board[2]==marker) or (board[9]==board[6]==board[3]==marker) or
           (board[1]==board[5]==board[9]==marker) or (board[7]==board[5]==board[3]==marker))


import random


def choose_first():
    if random.randint(0, 1) == 0:
        return 'Player2'
    else:
        return 'Player1'


def space_check(board, position):
    return board[position] == ' '


def full_board_check(board):
    for i in range(1, 10):
        if space_check(board, i):
            return False
    return True


def player_choice(board):
    position = 0

    while position not in range(1, 10) or not space_check(board, position):
        position = int(input('Choose your position [1-9]: '))

    return position


def replay():
    return input('Do you want to play again: y/n ').lower().startswith('y')


print('Welcome to Tic Tac Toe')

while True:
    theboard = [' '] * 10
    player1_marker, player2_marker = player_input()
    turn = choose_first()
    print(turn + ' will go first')

    play_game = input('Ready to play! Yes or No ')

    if play_game.lower()[0] == 'y':
        game_on = True
    else:
        game_on = False

    while game_on:
        if turn == 'Player1':

            display_board(theboard)
            position = player_choice(theboard)
            place_marker(theboard, player1_marker, position)

            if win_check(theboard, player1_marker):
                display_board(theboard)
                print("Congratulations! Player1 has won the game")
                game_on = False
            else:
                if full_board_check(theboard):
                    display_board(theboard)
                    print('The game is a Tie!')
                    break
                else:
                    turn = 'Player2'

        else:

            display_board(theboard)
            position = player_choice(theboard)
            place_marker(theboard, player2_marker, position)

            if win_check(theboard, player2_marker):
                display_board(theboard)
                print('PLayer2 has won the game')
                game_on = False

            else:
                if full_board_check(theboard):
                    display_board(theboard)
                    print("The game is a tie")
                    break
                else:
                    turn = 'Player1'

    if not replay():
        break