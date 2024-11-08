0x05. N Queens
Project Overview
The N Queens problem is a classic algorithm challenge in computer science and mathematics. The task is to place N queens on an N×N chessboard so that no two queens can attack each other. This project uses a backtracking algorithm to explore potential solutions and efficiently find all possible arrangements where the queens are non-attacking.

This README provides a detailed guide to understand, set up, and run the solution to the N Queens problem in Python.

Concepts and Techniques
To complete this project, you should understand several core concepts:

Backtracking Algorithm: Used to explore all potential solutions and backtrack when a solution path cannot be completed.
Recursion: Essential for implementing backtracking algorithms in Python.
List Manipulation: To manage positions of queens on the board.
Command-line Arguments: Utilized to input N, the size of the board, from the command line.
Requirements
Editor: Allowed editors include vi, vim, and emacs.
Operating System: Files will be run on Ubuntu 20.04 LTS using Python 3.4.3.
PEP 8 Compliance: Code should adhere to the PEP 8 style guide (version 1.7.*).
Execution: Ensure all files are executable.
Files: Each file should end with a newline, and the first line of all files should be #!/usr/bin/python3.
Project File
0-nqueens.py: The main Python script that implements the N Queens solution using backtracking.
Usage
Run the program from the command line as follows:

bash
Copy code
./0-nqueens.py N
where N is the size of the board and the number of queens.

Conditions:
N must be an integer greater than or equal to 4.
If the wrong number of arguments is provided, the program will print:
makefile
Copy code
Usage: nqueens N
and exit with status 1.
If N is not an integer, it will print:
css
Copy code
N must be a number
and exit with status 1.
If N is less than 4, it will print:
mathematica
Copy code
N must be at least 4
and exit with status 1.
Example
bash
Copy code
$ ./0-nqueens.py 4
[[0, 1], [1, 3], [2, 0], [3, 2]]
[[0, 2], [1, 0], [2, 3], [3, 1]]
Each solution is displayed as a list of [row, column] positions for each queen on the board.

Solution Approach
The program employs a backtracking algorithm:

Recursive Placement: The algorithm attempts to place queens row by row, ensuring that each placed queen does not conflict with previously placed queens.
Checking Conflicts: Each position is checked for conflicts with previously placed queens by verifying row, column, and diagonal constraints.
Backtracking: If a queen cannot be placed in any column of a row, the algorithm backtracks to the previous row and tries the next column.
This approach ensures all possible solutions are explored, and each valid configuration is printed.

Additional Resources
Backtracking Introduction: A comprehensive overview of backtracking algorithms.
Recursion in Python: Understanding recursion to implement the solution.
Python Lists: Guide to manipulate lists in Python.
Command Line Arguments in Python: Handling command-line inputs with the sys module.
Repository Structure
plaintext
Copy code
.
├── 0-nqueens.py        # Main file containing the solution
└── README.md           # Project description and usage guide
Author: Gatjuat Wicteat Riek
email: gatjuatriek@gmail.com
GitHub Repository: alx-interview
