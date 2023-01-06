import random

def get_letters():
  player_choice = "fahfoefh"
  while not player_choice == 'X' and not player_choice == 'O':
    player_choice = input("Do you want to play X or O?").upper()
  if player_choice == 'X':
    return 'X', 'O'
  else:
    return 'O', 'X'

def initialize_game():
  player_letter, computer_letter = get_letters()
  turn = 'player'
  board = [' ']*10
  return board, player_letter, computer_letter, turn

def draw_board(board):
  print(f' {board[1]} | {board[2]} | {board[3]}')
  print('------------')
  print(f' {board[4]} | {board[5]} | {board[6]}')
  print('------------')
  print(f' {board[7]} | {board[8]} | {board[9]}')

def is_board_empty(board, box):
  box = int(box)
  if box == 0:
    return False
  if board[box] == ' ':
    return True
  else:
    return False

def player_move(board):
  move = 0
  while move not in ['1', '2', '3', '4', '5', '6', '7', '8', '9'] and not is_board_empty(board, move):
    move = input("What is your next move? Enter a number 1-9:")
  
  return int(move)

def comp_move(board, player_letter):
  if player_letter == 'X':
    computer_letter = 'O'
  else:
    computer_letter = 'X'

  for i in range(10):
    if is_board_empty(board, i):
      board[i] = computer_letter
      if check_winner(board, computer_letter):
        return i
      board[i] = ' '

  for i in range(10):
    if is_board_empty(board, i):
      board[i] = player_letter
      if check_winner(board, player_letter):
        return i
      board[i] = ' '

  move = "0"
  while not is_board_empty(board, move):
    move = random.randint(1,9)
  return move

def check_winner(board, letter):
  return (
    (board[1] == letter and board[2] == letter and board[3] == letter) or 
    (board[4] == letter and board[5] == letter and board[6] == letter) or
    (board[7] == letter and board[8] == letter and board[9] == letter) or
    (board[1] == letter and board[4] == letter and board[7] == letter) or
    (board[2] == letter and board[5] == letter and board[8] == letter) or
    (board[3] == letter and board[6] == letter and board[9] == letter) or
    (board[1] == letter and board[5] == letter and board[9] == letter) or
    (board[7] == letter and board[5] == letter and board[3] == letter)
  )


board, player_letter, comp_letter, turn = initialize_game()
draw_board(board)
game_is_playing = True

while game_is_playing:
  #player move
  move = player_move(board)
  board[move] = player_letter 
  draw_board(board)
  win = check_winner(board, player_letter)

  if win == True:
    print("Congradulations you won!!")
    game_is_playing = False
  else:
    print("This is the computer's move:")

    move = comp_move(board, player_letter)
    board[move] = comp_letter
    draw_board(board)
    win = check_winner(board, comp_letter)

    if win == True:
      print("Computer has won.")
      game_is_playing = False
  


