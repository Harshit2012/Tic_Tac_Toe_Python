def print_board(board):
    for row in board:
        print(" | ".join(row))
        print("-" * 9)

def check_winner(board):
    for row in board:
        if all(cell == 'X' for cell in row) or all(cell == 'O' for cell in row):
            return True

    for col in range(3):
        if all(board[row][col] == 'X' for row in range(3)) or all(board[row][col] == 'O' for row in range(3)):
            return True

    if all(board[i][i] == 'X' for i in range(3)) or all(board[i][2 - i] == 'O' for i in range(3)):
        return True

    return False

def is_board_full(board):
    return all(all(cell != ' ' for cell in row) for row in board)

def get_valid_move():
    while True:
        try:
            move = int(input("Enter your move (1-9): "))
            if 1 <= move <= 9:
                return move
            else:
                print("Invalid move. Please enter a number between 1 and 9.")
        except ValueError:
            print("Invalid input. Please enter a number.")

def main():
    board = [[' ' for _ in range(3)] for _ in range(3)]
    players = ['X', 'O']
    current_player = 0

    while True:
        print_board(board)

        move = get_valid_move()

        row, col = divmod(move - 1, 3)

        if board[row][col] == ' ':
            board[row][col] = players[current_player]

            if check_winner(board):
                print_board(board)
                print(f"Player {players[current_player]} wins!")
                break

            if is_board_full(board):
                print_board(board)
                print("It's a tie!")
                break

            current_player = 1 - current_player  # Switch players
        else:
            print("Invalid move. The cell is already taken.")

if __name__ == "__main__":
    main()