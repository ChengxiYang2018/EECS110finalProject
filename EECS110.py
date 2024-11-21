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
