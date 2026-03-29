from constraint import Problem, AllDifferentConstraint

# Making grid of 3x3 dimesnsion to make the sudoku to easy to understand
def print_board(board):
    for i in range(9):
        if i % 3 == 0 and i != 0:
            print("-" * 21)

        for j in range(9):
            if j % 3 == 0 and j != 0:
                print("|", end=" ")

            print(board[i][j], end=" ")

        print()


# AI usage to make constraints
def solve_sudoku(puzzle):
    problem = Problem()

    cells = [(r, c) for r in range(9) for c in range(9)]

    for cell in cells:
        problem.addVariable(cell, range(1, 10))

    for r in range(9):
        problem.addConstraint(AllDifferentConstraint(), [(r, c) for c in range(9)])

    for c in range(9):
        problem.addConstraint(AllDifferentConstraint(), [(r, c) for r in range(9)])

    for br in range(3):
        for bc in range(3):
            box = [(r, c) for r in range(br*3, br*3+3)
                           for c in range(bc*3, bc*3+3)]
            problem.addConstraint(AllDifferentConstraint(), box)

    for r in range(9):
        for c in range(9):
            if puzzle[r][c] != 0:
                problem.addConstraint(
                    lambda var, val=puzzle[r][c]: var == val,
                    [(r, c)]
                )

    solution = problem.getSolution()

    if solution:
        return [[solution[(r, c)] for c in range(9)] for r in range(9)]
    return None


# We give input of one row and this will update it and show the entry of each input
def get_input():
    print("Enter Sudoku row by row (Use 0 for empty cells):")
    print("PLease enter space between the numbers")
    puzzle = []

    for i in range(9):
        while True:
            row = input(f"Row {i+1}: ").split()

            if len(row) != 9:
                print(" Enter exactly 9 numbers")
                continue

            try: 
                row = list(map(int, row))
            except:
                print(" Enter only numbers")
                continue

            if any(num < 0 or num > 9 for num in row):
                print(" Numbers must be between 0 and 9")
                continue

            puzzle.append(row)

            #  Show row confirmation
            print(f"\n Row {i+1} recorded: {row}")

            #  Show live grid
            print("\nCurrent Sudoku:")
            temp_board = puzzle + [[0]*9]*(8-i)
            print_board(temp_board)
            print()

            break

    return puzzle


#  Main Program
puzzle = get_input()

print("\n Final Input Sudoku:\n")
print_board(puzzle)

solution = solve_sudoku(puzzle)

if solution:
    print("\n Solution Sudoku:\n")
    print_board(solution)
else:
    print(" Sorry either you have given wrong input or the number you entere has repeted somewhere ")