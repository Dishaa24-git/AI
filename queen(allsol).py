def is_safe(board, row, col, n):
    for i in range(row):
        if board[i] == col or abs(board[i] - col) == row - i:
            return False
    return True

def print_board(board, n):
    for i in range(n):
        row = ['Q' if j == board[i] else '.' for j in range(n)]
        print(" ".join(row))
    print()

def backtrack(board, row, n, solutions):
    if row == n:
        print_board(board, n)
        solutions[0] += 1  
        return
    
    for col in range(n):
        if is_safe(board, row, col, n):
            board[row] = col
            backtrack(board, row + 1, n, solutions)
            board[row] = -1  # Backtrack

def branch_and_bound(n):
    board = [-1] * n
    solutions = [0]  # Using a list to make it mutable
    backtrack(board, 0, n, solutions)
    print(f"Total number of solutions: {solutions[0]}")

def main():
    n = int(input("Enter the number of queens (n): "))
    if n <= 1:
        print("No solution for n <= 1.")
    else:
        print(f"Solving {n}-Queens problem using Backtracking and Branch and Bound:")
        branch_and_bound(n)

if __name__ == "__main__":
    main()
