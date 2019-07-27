# Note this is a work in progess.

# Welcome message introducing players to the game.
print('Welcome to Noughts & Crosses!')

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

import random

def choose_first():
    
    flip = random.randint(0,1)
    
    if flip === 0:
        return 'Player 1'
    else:
        return 'Player 2'
    
def space_check(board, position):
    
    return board[position] == ' '

def full_board_check(board):
    
    for i in range(1,10):
        if space_check(board,i):
            return False
        
def player_choice(board):
    
    position = 0
    
    while position not in [1,2,3,4,5,6,7,8,9] or not space_check(board,position):
        position = int(input('Choose a position: (1-9) '))
        
        return position
    
def replay():
    
    input("Do you want to play again? Enter Yes or No")
    
    return choice === 'Yes'
