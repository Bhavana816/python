board = {
    'top-l': ' ', 'top-m': ' ', 'top-r': ' ',
    'mid-l': ' ', 'mid-m': ' ', 'mid-r': ' ',
    'low-l': ' ', 'low-m': ' ', 'low-r': ' '
}
def printboard(board):
    print(board['top-l'] + '|' + board['top-m'] + '|' + board['top-r'])
    print('-+-+-')
    print(board['mid-l'] + '|' + board['mid-m'] + '|' + board['mid-r'])
    print('-+-+-')
    print(board['low-l'] + '|' + board['low-m'] + '|' + board['low-r'])
def check_winner(board):
    for row in ['top', 'mid', 'low']:
        if board[f'{row}-l'] == board[f'{row}-m'] == board[f'{row}-r'] != ' ':
            return board[f'{row}-l']
    for col in ['l', 'm', 'r']:
        if board[f'top-{col}'] == board[f'mid-{col}'] == board[f'low-{col}'] != ' ':
            return board[f'top-{col}']
    if board['top-l'] == board['mid-m'] == board['low-r'] != ' ':
        return board['top-l']
    if board['top-r'] == board['mid-m'] == board['low-l'] != ' ':
        return board['top-r']
    return None
turn = 'X'
for i in range(9):
    printboard(board)
    print('Turn for ' + turn + ' - move on which space?')
    move = input().strip()
    while board[move] != ' ':
        print('Invalid move. Space already taken. Choose again:')
        move = input().strip()
    board[move] = turn
    winner = check_winner(board)
    if winner:
        printboard(board)
        print(f'Player {winner} wins!')
        break
    if turn == 'X':
        turn = 'O'
    else:
        turn = 'X'
if not winner:
    printboard(board)
    print('It\'s a tie!')
