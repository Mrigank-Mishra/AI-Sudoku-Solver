# Problem statement

Sudoku is a widely known logic-based puzzle where the objective is to fill a 9×9 grid so that each row, column, and 3×3 subgrid contains numbers from 1 to 9 without repetition. Solving Sudoku manually can be time-consuming and difficult, especially for complex puzzles.

Many users struggle to solve Sudoku efficiently or verify whether a given puzzle is valid. There is a need for a simple, reliable tool that can take a Sudoku puzzle as input, validate it, and generate a correct solution automatically.

This project aims to develop a console-based Sudoku solver that uses a constraint satisfaction approach to solve the puzzle while ensuring all Sudoku rules are followed.


# Scope of the project

The scope of this project is limited to a console-based Sudoku solver.

1. Current Scope:
   - The application accepts Sudoku input row by row from the user.
   - It validates the input for correctness (duplicate values, invalid numbers).
   - It solves the puzzle using a constraint satisfaction technique.
   - It displays the final solved Sudoku grid.

2. Future Scope:
   - Adding a graphical user interface (GUI).
   - Allowing users to load puzzles from files.
   - Implementing difficulty levels and puzzle generation.
   - Visualizing the solving process step by step.


# Target users

1. Students: Individuals who want to understand how Sudoku solving works using programming and AI techniques.
2. Puzzle Enthusiasts: Users who want a quick way to solve Sudoku puzzles.
3. Beginners in Python: Learners interested in understanding constraint satisfaction and problem-solving techniques.


# High-level features

1. Input System: Allows users to enter Sudoku values in a structured format.
2. Solver Logic: Uses constraint satisfaction to find a valid solution.
3. Output Display: Presents the solved Sudoku in a clear grid format.
4. Error Handling: Prevents invalid puzzles from being processed.
