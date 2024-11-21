import string
import random
#display the board
def display_board(board, player):
  """Displays the input board, typically the human player."""
  if player is False:
    print("Opponents board:")
    print()
  cols = [" ", "1", "2", "3", "4", "5"] # confusing why is there a space on the front?
  rows = [" ", "A", "B", "C", "D", "E"]
  for row in range(6):
    for col in range(6):
      if row == 0:
        print(cols[col], end=" ")
      elif col == 0:
        print(rows[row], end="|")
      else:
        if player:
          print(board[row - 1][col - 1], end="|")
        else:
          if board[row - 1][col - 1] != "*":
            print(board[row - 1][col - 1], end="|")
          else:
            print(" ", end="|")
    print()
  print()
  print("KEY: Hit = X, Miss = O, Boat = *")
  print()
# Testing display board functions

# You should make sample inputs to test in your functions
# in this case we are making boards to test in our display board function

# general test cases
print("TESTING EMPTY GRID CASE")
empty_grid =  [[" ", " ", " ", " ", " "],
               [" ", " ", " ", " ", " "],
               [" ", " ", " ", " ", " "],
               [" ", " ", " ", " ", " "],
               [" ", " ", " ", " ", " "]]
               # 2D list of strings
print("display_board() INPUT: empty grid")
# we should expect an empty grid to display an empty grid for both functions
print("display_board() EXPECTED OUTPUT: empty grid, True for player board")
print("display_board() ACTUAL OUPUT:")
display_board(empty_grid, True)
print()
print("display_board() INPUT: empty grid, False for player board")
print("display_board() EXPECTED OUTPUT: empty grid")
print("display_board() ACTUAL OUTPUT:")
display_board(empty_grid, False)
print()

print("TESTING TYPICAL GRID CASE")
sample_grid = [[" ", "*", "*", " ", " "],
               ["X", "O", " ", " ", " "],
               ["*", " ", "X", "X", "X"],
               ["*", " ", " ", " ", " "],
               [" ", " ", " ", " ", " "]]
# we should expect this random but possible grid to display according to the function descriptions (showing vs. not showing boats)
print("display_board() INPUT: sample grid, True for player board")
# we should expect an empty grid to display an empty grid for both functions
print("display_board() EXPECTED OUTPUT: grid should display all the input grids boats ('*') and also all the hits and misses made by the opponent")
print("display_board() ACTUAL OUPUT:")
display_board(sample_grid, True)
print()
print("display_board() INPUT: sample grid, False for player board")
print("display_board() EXPECTED OUTPUT: grid should display only the hits and misses made, should not be able to see where the opponents boats are")
print("display_board() ACTUAL OUTPUT:")
display_board(sample_grid, False)
print()

def convert_to_index(position):
  """Converts input postion (ie. "A4") to a row and column."""
  alphabet_idx_conversion = {"A": 0, "B": 1, "C": 2, "D":3, "E":4, "F":5, "G":6, "H":7, "I":8, "J":9, "K":10, "L":11, "M":12,
                             "N":13, "O":14, "P":15, "Q":16, "R":17, "S":18, "T":19, "U":20, "V":21, "W":22, "X":23, "Y":24, "Z":25}
  row = position[0]
  col = position[1]

  row = alphabet_idx_conversion[row]
  col = int(col) - 1
  return row, col
  def validate_boat(board, position, horizontal, size):
  """Validates a potential boat and orientation on the input board."""
  row, col = convert_to_index(position)

  # horizontal
  if horizontal:
    # check to the right
    if board[row][col:col+size] == [" "] * size:
      return True, "right"

    # check to the left
    if board[row][col-size+1:col+1] == [" "] * size:
      return True, "left"

    return False, None

  # vertical
  else:
    # check above
    potential_boat = []
    if row - size + 1 >= 0:
      for row in range(row - size + 1, row + 1):
        if board[row][col] == " ":
          potential_boat.append(" ")
      if potential_boat == [" "] * size:
        return True, "up"

    # check below
    potential_boat = []
    if row + size - 1 <= 4:
      for row in range(row, row + size):
        if board[row][col] == " ":
          potential_boat.append(" ")
      if potential_boat == [" "] * size:
        return True, "down"

    return False, None

def check_guess(current_opponent_board : list, guess):
  """TODO: replace with short description of function."""
  # TODO: Write check_guess()
  index = ["A1", "A2", "A3", "A4", "A5", "B1", "B2", "B3", "B4", "B5", "C1", "C2","C3", "C4", "C5", "D1","D2","D3","D4","D5","E1","E2","E3","E4","E5"]
  if guess in index :
    [row,col] = convert_to_index(guess) # convert guess to index
    if 0 <= row and row < 5 and 0 <= col and col < 5 :
      if current_oppnenet_board(row,col) == " ":
        current_oppnenet_board(row,col) == "O" #miss
        return True
      elif current_oppnenet_board(row,col) == "*":
        current_oppnenet_board(row,col) == "X" # hit
        return True
      elif current_oppnenet_board(row,col) == "O":
        return False
      elif current_oppnenet_board(row,col) == "X":
        return False



def check_for_winner(board):
  """TODO: replace with short description of function."""
  # TODO: Write check_for_winner()

# Checks through column
  for col in board:

    # Checks for any remaining boats within columns, return false if there is.
    if '*' in col:
     return False

  return True


# Checks through row
  for row in board:

     #Checks any remaining boats between rows, and returns false if it encounters one.
    if '*' in row:
      return False

  return True


