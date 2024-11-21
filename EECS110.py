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
