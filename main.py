from sudoku_solver import SudokuSolver

test_board = [[9, 0, 0, 0, 0, 0, 0, 0, 0],
              [0, 0, 0, 1, 0, 0, 5, 0, 0],
              [0, 3, 2, 0, 0, 6, 0, 8, 0],
              [6, 0, 0, 0, 0, 0, 0, 9, 0],
              [0, 7, 9, 0, 5, 0, 8, 0, 0],
              [4, 0, 0, 0, 0, 7, 0, 0, 0],
              [0, 0, 0, 0, 6, 0, 0, 0, 3],
              [0, 4, 0, 0, 0, 0, 0, 0, 0],
              [0, 8, 7, 0, 0, 3, 0, 2, 0]]


solver = SudokuSolver(test_board)
if not solver.validate_board():
    raise ValueError("Not a valid board.")

if solver.solve():
    print(solver)
else:
    print("Not solvable.")

