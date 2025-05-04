def is_safe(board, row, col, n):
    # Check if there is a queen in the same column
    for i in range(row):
        if board[i] == col or abs(board[i] - col) == row - i:
            return False
    return True

def print_board(board, n):
    # Print the board representation
    for i in range(n):
        row = ['Q' if j == board[i] else '.' for j in range(n)]
        print(" ".join(row))
    print()

def backtrack(board, row, n):
    if row == n:
        print_board(board, n)
        return True
    
    for col in range(n):
        if is_safe(board, row, col, n):
            board[row] = col
            if backtrack(board, row + 1, n):
                return True
            board[row] = -1  # Backtrack

    return False

def branch_and_bound(n):
    # Board initialization
    board = [-1] * n
    if not backtrack(board, 0, n):
        print("No solution exists.")
    
def main():
    n = int(input("Enter the number of queens (n): "))
    if n <= 1:
        print("No solution for n <= 1.")
    else:
        print(f"Solving {n}-Queens problem using Backtracking and Branch and Bound:")
        branch_and_bound(n)

if __name__ == "__main__":
    main()

