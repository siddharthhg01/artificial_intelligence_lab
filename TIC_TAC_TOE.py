def print_board(board):
    for row in board:
        print(" | ".join(row))
        print("-" * 9)

def check_winner(board):
    for i in range(3):
        if board[i][0] == board[i][1] == board[i][2] != ' ':
            return board[i][0]
        if board[0][i] == board[1][i] == board[2][i] != ' ':
            return board[0][i]
    if board[0][0] == board[1][1] == board[2][2] != ' ':
        return board[0][0]
    if board[0][2] == board[1][1] == board[2][0] != ' ':
        return board[0][2]
    return None

def get_available_moves(board):
    return [(r, c) for r in range(3) for c in range(3) if board[r][c] == ' ']

def play_game():
    board = [[' ' for _ in range(3)] for _ in range(3)]
    player = 'X'

    while True:
        print_board(board)
        winner = check_winner(board)
        if winner:
            print(f"{winner} wins!")
            break
        if not get_available_moves(board):
            print("It's a draw!")
            break

        row, col = map(int, input(f"Player {player}, enter row and column (0-2): ").split())
        if board[row][col] == ' ':
            board[row][col] = player
            player = 'O' if player == 'X' else 'X'
        else:
            print("Invalid move! Try again.")

play_game()