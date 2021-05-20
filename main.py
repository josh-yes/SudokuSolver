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
	for i in range(9):
		if i % 3 == 0 and i != 0:
			print("---+---+---")
		for j in range(9):
			if j % 3 == 0 and j != 0:
				print("|" + str(board[i][j]), end="")
			elif j == 8:
				print(board[i][j])
			else:
				print(board[i][j], end="")			

def solveBoard(board):
	if not findEmpty(board):
		return True
	else:
		i, j = findEmpty(board)
	
	for n in range(1, 10):
		if isValid(board, n, i, j):
			board[i][j] = n
			
			if solveBoard(board):
				return True
			
			board[i][j] = 0
	return False


def findEmpty(board):
	for i in range(9):
		for j in range(9):
			if board[i][j] == 0:
				return i,j				
	return None

def isValid(board, val, i, j):
	for x in range(9): # check row
		if board[i][x] == val:
			return False
	for y in range(9): # check column
		if board[y][j] == val:
			return False
	return checkSquare(board, val, i, j)

def checkSquare(board, val, i, j):
	square_x = j // 3
	square_y = i // 3

	for y in range(square_y * 3, square_y * 3 + 3):
		for x in range(square_x * 3, square_x * 3 + 3):
			if board[y][x] == val:
				return False
	return True

printBoard(board)
print()

solveBoard(board)

printBoard(board)
