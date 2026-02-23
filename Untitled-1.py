import copy

def check_win(b, p):
    # Helper to check if player 'p' has won on board 'b'
    wins = [
        [b[0][0], b[0][1], b[0][2]], [b[1][0], b[1][1], b[1][2]], [b[2][0], b[2][1], b[2][2]],
        [b[0][0], b[1][0], b[2][0]], [b[0][1], b[1][1], b[2][1]], [b[0][2], b[1][2], b[2][2]],
        [b[0][0], b[1][1], b[2][2]], [b[0][2], b[1][1], b[2][0]]
    ]
    return [p, p, p] in wins

def minimax(current_board, is_maximizing):
    # Terminal states
    if check_win(current_board, "O"): return 10
    if check_win(current_board, "X"): return -10
    if not any("" in row for row in current_board): return 0

    if is_maximizing:
        best_score = -float('inf')
        for r in range(3):
            for c in range(3):
                if current_board[r][c] == "":
                    current_board[r][c] = "O"
                    score = minimax(current_board, False)
                    current_board[r][c] = ""
                    best_score = max(score, best_score)
        return best_score
    else:
        best_score = float('inf')
        for r in range(3):
            for c in range(3):
                if current_board[r][c] == "":
                    current_board[r][c] = "X"
                    score = minimax(current_board, True)
                    current_board[r][c] = ""
                    best_score = min(score, best_score)
        return best_score

# --- ORIGINAL BASE CODE START ---
s=True
board=[["","",""],["","",""],["","",""]]
Me=0
Ai=0

while Me==0 and Ai==0:
    # --- PLAYER TURN ---
    while s == True:
        row = input("row (0-2): ")
        column = input("column (0-2): ")
        if board[int(row)][int(column)] == "":
            board[int(row)][int(column)] = "X"
            s = False
        else:
            s = True
    
    # Check if Player Won
    if check_win(board, "X"):
        Me = 1
        print("you won")
        break
    if not any("" in row for row in board):
        print("draw")
        break

    # --- AI TURN (Now using Minimax instead of random) ---
    print("AI is thinking...")
    best_val = -float('inf')
    best_move = (-1, -1)
    
    for r in range(3):
        for c in range(3):
            if board[r][c] == "":
                board[r][c] = "O"
                move_val = minimax(board, False)
                board[r][c] = ""
                if move_val > best_val:
                    best_move = (r, c)
                    best_val = move_val
    
    if best_move != (-1, -1):
        board[best_move[0]][best_move[1]] = "O"
        print(f"AI plays at: {best_move[0]} {best_move[1]}")
    
    s = True # Back to player turn

    # Display current board
    for row_list in board:
        print(row_list)

    # Check if AI Won
    if check_win(board, "O"):
        Ai = 1
        print("you lost")

def thomaspucamere():
    print("(-_-)")