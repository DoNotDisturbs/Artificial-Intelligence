def TicTacToe():
  board = [1, 2, 3, 4, 5, 6, 7, 8, 9]
  end = False
  MagicSquare = [4, 9, 2, 3, 5, 7, 8, 1, 6]

  def PrintBoard():
    print()
    print('', board[0], "|", board[1], "|", board[2])
    print("---|---|---")
    print('', board[3], "|", board[4], "|", board[5])
    print("---|---|---")
    print('', board[6], "|", board[7], "|", board[8])
    print()

  def GetNumber():
    while True:
      number = input()
      try:
        number  = int(number)
        if number in range(1, 10):
          return number
        else:
          print("\nNumber not on board")
      except ValueError:
        print("\nThat's not a number. Try again")
        continue

  def Turn(player):
    placing_index = GetNumber() - 1
    if board[placing_index] == "X" or board[placing_index] == "O":
      print("\nBox already occupied. Try another one")
      Turn(player)
    else:
      board[placing_index] = player

  def CheckWin(player):
    count = 0

    for x in range(9):
      for y in range(9):
        for z in range(9):
          if x != y and y != z and z != x:
            if board[x] == player and board[y] == player and def generateSquare(n):
 
    # 2-D array with all
    # slots set to 0
    magicSquare = [[0 for x in range(n)]
                   for y in range(n)]
 
    # initialize position of 1
    i = n // 2
    j = n - 1
 
    # Fill the magic square
    # by placing values
    num = 1
    while num <= (n * n):
        if i == -1 and j == n:  # 3rd condition
            j = n - 2
            i = 0
        else:
 
            # next number goes out of
            # right side of square
            if j == n:
                j = 0
 
            # next number goes
            # out of upper side
            if i < 0:
                i = n - 1
 
        if magicSquare[int(i)][int(j)]:  # 2nd condition
            j = j - 2
            i = i + 1
            continue
        else:
            magicSquare[int(i)][int(j)] = num
            num = num + 1
 
        j = j + 1
        i = i - 1  # 1st condition
 
    # Printing magic square
    print("Magic Square for n =", n)
    print("Sum of each row or column",
          n * (n * n + 1) // 2, "\n")
 
    for i in range(0, n):
        for j in range(0, n):
            print('%2d ' % (magicSquare[i][j]),
                  end='')
 
        print()
 

 
# Works only when n is odd
n = 3
generateSquare(n)