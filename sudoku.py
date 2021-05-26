import random
random.seed()

class Solver:
        def __init__(self, choice):
                self.board = self.initializeBoard(choice)
        
        def initializeBoard(self, choice):                
                board = []

                if choice == "MANUAL INPUT":
                        for i in range(9):
                                stringRow = input("row " + str(i + 1) + ":")
                                row = []
                                
                                for char in stringRow:
                                        row.append(int(char))
                                
                                board.append(row)
                elif choice == "EXAMPLE PUZZLE":
                        f = open("examplePuzzles.txt")
                        puzzleNum = random.randrange(5)
                        f.seek(puzzleNum * 91)
                        
                        for i in range(9):
                                stringRow = f.read(9)
                                f.seek(f.tell() + 1)
                                row = []

                                for char in stringRow:
                                        row.append(int(char))

                                board.append(row)
                        f.close()
                else:
                        print("Error: invalid something or other")
                        quit()
                return board

        def printBoard(self):
                for i in range(9):
                        if i % 3 == 0 and i != 0:
                                print("---+---+---")
                        for j in range(9):
                                if j % 3 == 0 and j != 0:
                                        print("|" + str(self.board[i][j]), end="")
                                elif j == 8:
                                        print(self.board[i][j])
                                else:
                                        print(self.board[i][j], end="")
        
        def solveBoard(self):
                if not self.findEmpty():
                        return True
                else:
                        i, j = self.findEmpty()
        
                for n in range(1, 10):
                        if self.isValid(n, i, j):
                                self.board[i][j] = n
                                
                                if self.solveBoard():
                                        return True
                                
                                self.board[i][j] = 0
                
                return False

        def findEmpty(self):
                for i in range(9):
                        for j in range(9):
                                if self.board[i][j] == 0:
                                        return i,j				
                return None

        def isValid(self, val, i, j):
                for x in range(9): # check row
                        if self.board[i][x] == val:
                                return False
                for y in range(9): # check column
                        if self.board[y][j] == val:
                                return False
                return self.checkSquare(val, i, j)

        def checkSquare(self, val, i, j):
                square_x = j // 3
                square_y = i // 3

                for y in range(square_y * 3, square_y * 3 + 3):
                        for x in range(square_x * 3, square_x * 3 + 3):
                                if self.board[y][x] == val:
                                        return False
                return True
