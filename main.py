board = [
	[7,8,0,4,0,0,1,2,0],
        [6,0,0,0,7,5,0,0,9],
	[0,0,0,6,0,1,0,7,8],
	[0,0,7,0,4,0,2,6,0],
	[0,0,1,0,5,0,9,3,0],
	[9,0,4,0,6,0,0,0,5],
	[0,7,0,3,0,0,0,1,2],
	[1,2,0,0,0,7,4,0,0],
	[0,4,9,2,0,6,0,0,7]
]

def printBoard(board):
	for row in board:
		print(row)

printBoard(board)

def solveBoard(board):
	i,j = findEmpty(board)
	

def findEmpty(board):
	for i in range(9):
		for j in range(9):
			if board[i][j] == 0:
				return i,j				

def isValid(board, i, j):
	for x in range(9): # check row
		if board[i][x] == board[i][j] and x != j:
			return false
	for y in range(9): # check column
		if board[y][j] == board[i][j] and y != i:
			return false
	return checkSquare(board, i, j) # check square

def checkSquare(board, i, j):
	if i < 3:
		if j < 3: # top left
			# do something
		elif j < 6: # top middle
			# do something
		else: # top right
			# do something
	elif i < 6:
		if j < 3: # middle left
			# do something
		elif j < 6: # middle middle
			# do something
		else: # middle right
			#do something
	else:
		if j < 3: # bottom left
			# do something
		elif j < 6: # bottom middle
			# do something
		else: # bottom right
			# do something
		
