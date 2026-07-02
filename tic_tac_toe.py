# tic_tac_toe.py

def print_board(board):
    print()
    for row in board:
        print(" | ".join(row))
        print("-" * 9)
    print()

def check_winner(board, player):
    for row in board:
        if all(c == player for c in row):
            return True
    for col in range(3):
        if all(board[r][col] == player for r in range(3)):
            return True
    if all(board[i][i] == player for i in range(3)):
        return True
    if all(board[i][2-i] == player for i in range(3)):
        return True
    return False

def board_full(board):
    return all(c != " " for row in board for c in row)

def main():
    board = [[" "]*3 for _ in range(3)]
    player = "X"
    print("=== TIC TAC TOE ===")
    while True:
        print_board(board)
        try:
            r = int(input(f"Player {player} Row (1-3): ")) - 1
            c = int(input(f"Player {player} Col (1-3): ")) - 1
            if r not in range(3) or c not in range(3):
                print("Invalid position.")
                continue
            if board[r][c] != " ":
                print("Cell occupied.")
                continue
            board[r][c] = player
            if check_winner(board, player):
                print_board(board)
                print(f"Player {player} wins!")
                break
            if board_full(board):
                print_board(board)
                print("It's a draw!")
                break
            player = "O" if player == "X" else "X"
        except ValueError:
            print("Enter valid numbers.")

if __name__ == "__main__":
    main()
