# Sudoku Solver using Constraint Satisfaction

## Description

I created a Sudoku solver for my project. I used Python and some ideas from Artificial Intelligence like Sudoku Solver using Constraint Satisfaction Problems. The Sudoku Solver takes a Sudoku puzzle that's not complete and finds a solution that follows all the rules of Sudoku Solver.

The Sudoku solver solve it by a system based on rules. Each cell in the Sudoku Solver grid is like a variable and the numbers 1 to 9 are the values for these variables. The rules make sure that each row, column and small grid has each number once. This shows how smart systems can solve problems that have a lot of rules by using these rules of guessing.

## Objective

The main goal of this project was to see how Artificial Intelligence can help solve problems like Sudoku Solver.

## Approach

To solve the Sudoku Solver puzzle I used a library called python-constraint. This library helps define variables and rules. First I made variables for each cell in the Sudoku Solver grid. Then I said what numbers could go in each cell.

After that I added rules to make sure the Sudoku Solver puzzle follows the rules of Sudoku Solver. I used a rule, that says all the numbers in each row column and small grid must be different. For the cells that already had numbers I added a rule to keep those numbers the same while solving the Sudoku Solver puzzle.

Once all the rules were set the Sudoku Solver solver tried to find a solution that follows all the rules. If it finds a solution it shows the Sudoku Solver puzzle. If not it says the puzzle is invalid or cannot be solved.

## Implementation Details

The Sudoku Solver program has three parts. The first part asks the user to enter the Sudoku Solver puzzle row by row. It checks to make sure each row has nine numbers and the numbers are between 0 and 9.

The second part shows the Sudoku Solver board in a way that makes it easy to see the puzzle and the solution.

The third part is the Sudoku Solver function. It defines the problem. Uses the constraint satisfaction method to find a solution for Sudoku Solver.

## Execution

To run the Sudoku Solver program I installed the python-constraint library using pip install python-constraint. Then I ran the Python file. The Sudoku Solver program asked me to enter the Sudoku Solver puzzle row by row. As I entered each row it showed the state of the Sudoku Solver grid.

After entering all the rows the Sudoku Solver program solved the puzzle. Showed the solution if it found one.

## Result

The Sudoku Solver program can solve Sudoku Solver puzzles using constraint satisfaction. It makes sure to follow all the Sudoku Solver rules. If the puzzle is invalid it tells the user that no solution exists for Sudoku Solver.

## Learning Outcome

I learned a lot from this Sudoku Solver project. I understood how Artificial Intelligence techniques, like constraint satisfaction can be used to solve problems with a lot of rules. I also saw how using rules can make solving problems faster than trying all solutions. This Sudoku Solver project helped me connect the ideas from my AI and ML class to a project.

## Limitations

The Sudoku Solver program which I had made only works for Sudoku Solver puzzles. It assumes the user enters numbers. It does check to make sure the numbers are correct. It can't go for column wise input. And it too can't seperate the numbers on its own, you have to give space between the numbers 

