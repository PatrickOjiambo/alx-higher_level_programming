import sys

def is_safe(board, row, col, N):
    # Check if the current position is safe for a queen

    # Check the row on the left side
    for i in range(col):
        if board[row][i] == 1:
            return False

    # Check the upper diagonal on the left side
    i, j = row, col
    while i >= 0 and j >= 0:
        if board[i][j] == 1:
            return False
        i -= 1
        j -= 1

    # Check the lower diagonal on the left side
    i, j = row, col
    while i < N and j >= 0:
        if board[i][j] == 1:
            return False
        i += 1
        j -= 1

    return True


def solve_nqueens(N):
    board = [[0] * N for _ in range(N)]
    solutions = []
    solve_util(board, 0, N, solutions)
    return solutions


def solve_util(board, col, N, solutions):
    if col == N:
        # Found a solution, convert the board to a string representation
        solution = []
        for row in range(N):
            for col in range(N):
                if board[row][col] == 1:
                    solution.append(str(col + 1))
        solutions.append(",".join(solution))
        return

    for row in range(N):
        if is_safe(board, row, col, N):
            # Place the queen and recursively solve for the next column
            board[row][col] = 1
            solve_util(board, col + 1, N, solutions)
            # Backtrack and remove the queen
            board[row][col] = 0


def main():
    # Check the number of arguments
    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        sys.exit(1)

    # Get the value of N from the command line argument
    try:
        N = int(sys.argv[1])
    except ValueError:
        print("N must be a number")
        sys.exit(1)

    # Check if N is at least 4
    if N < 4:
        print("N must be at least 4")
        sys.exit(1)

    # Solve the N queens problem
    solutions = solve_nqueens(N)

    # Print the solutions
    for solution in solutions:
        print(solution)

if __name__ == '__main__':
    main()

