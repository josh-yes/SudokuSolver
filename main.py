from sudoku import Solver

choice = input("Would you like to manually input board (0) or pick a random example puzzle (1)? ")

while choice != "0" and choice != "1":
    print("That wasn't one of the options, stupid.")
    choice = input("Would you like to manually input board (0) or pick a random example puzzle (1)? ")

if choice == "0":
    sudokuSolver = Solver("MANUAL INPUT")
else:
    sudokuSolver = Solver("EXAMPLE PUZZLE")

sudokuSolver.printBoard()
print()
sudokuSolver.solveBoard()
sudokuSolver.printBoard()


if sudokuSolver.isValidBoard():
    print("Woohoo!")
else:
    print("You fucked up...")
