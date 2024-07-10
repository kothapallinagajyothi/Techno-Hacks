import random

def print_board(board):
    for row in board:
        print(" | ".join(row))
        print("-" * 5)

def check_winner(board, player):
    # Check rows, columns, and diagonals for a win
    for row in board:
        if all(cell == player for cell in row):
            return True

    for col in range(3):
        if all(board[row][col] == player for row in range(3)):
            return True

    if all(board[i][i] == player for i in range(3)) or all(board[i][2 - i] == player for i in range(3)):
        return True

    return False

def is_board_full(board):
    return all(cell != ' ' for row in board for cell in row)

def get_player_move():
    row = int(input("Enter the row (0, 1, or 2): "))
    col = int(input("Enter the column (0, 1, or 2): "))
    return row, col

def get_computer_move(board):
    # Simple random move for the computer
    available_moves = [(row, col) for row in range(3) for col in range(3) if board[row][col] == ' ']
    return random.choice(available_moves)

def play_tic_tac_toe():
    board = [[' ' for _ in range(3)] for _ in range(3)]
    players = ['X', 'O']

    print_board(board)

    for turn in range(9):
        player = players[turn % 2]

        if player == 'X':
            row, col = get_player_move()
        else:
            row, col = get_computer_move(board)

        if board[row][col] == ' ':
            board[row][col] = player
        else:
            print("Cell already occupied. Try again.")
            turn -= 1  # Repeat the same turn

        print_board(board)

        if check_winner(board, player):
            print(f"{player} wins!")
            break

        if is_board_full(board):
            print("It's a tie!")
            break

if __name__ == "__main__":
    print("Welcome to Tic Tac Toe!")
    play_tic_tac_toe()
