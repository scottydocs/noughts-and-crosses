# Note this is a work in progess.

# Welcome message introducing players to the game.
print('Welcome to Noughts & Crosses!'

# Defines the outline and layout of the board
from IPython.display import clear_output

def display_board(board):
    print(board[7] + ' | ' + board[8] + ' | ' + board[9])
    print('--|---|--')
    print(board[4] + ' | ' + board[5] + ' | ' + board[6])
    print('--|---|--')
    print(board[1] + ' | ' + board[2] + ' | ' + board[3])

test_board = [' '] * 10
display_board(test_board)

# Prompts the first player to select their marker
def player_input():
  marker = ''
  
  while marker != 'X' and marker != 'O':
      marker = input('Player1: Choose X or O: ').upper()
      
      if marker == 'X':
      
          return ('X','O')
      else:
          return ('O','X')

player1_marker, player2_marker = player_input()

def place_marker(board, marker, postion)
    board[position] = marker
    
test_board

def win_check(board, mark):
    return ((board[4] == board[5] == board[6] == mark) or
    (board[7] == board[8] == board[9] == mark) or
    (board[1] == board[2] == board[3] == mark) or
    (board[1] == board[4] == board[7] == mark) or
    (board[2] == board[5] == board[8] == mark) or
    (board[3] == board[6] == board[9] == mark) or
    (board[7] == board[5] == board[3] == mark) or
    (board[9] == board[5] == board[1] == mark))
