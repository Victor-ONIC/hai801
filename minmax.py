import math

def evaluate(board):
    for row in board:
        if row.count('X') == 3:
            return 1
        if row.count('O') == 3:
            return -1
    
    for col in range(3):
        if board[0][col] == board[1][col] == board[2][col] != ' ':
            return 1 if board[0][col] == 'X' else -1
    
    if board[0][0] == board[1][1] == board[2][2] != ' ':
        return 1 if board[0][0] == 'X' else -1
    
    if board[0][2] == board[1][1] == board[2][0] != ' ':
        return 1 if board[0][2] == 'X' else -1
    
    return 0

def is_moves_left(board):
    for row in board:
        if ' ' in row:
            return True
    return False

def minimax(board, depth, is_max):
    score = evaluate(board)
    
    if score == 1 or score == -1:
        return score
    
    if not is_moves_left(board):
        return 0
    
    if is_max:
        best = -math.inf
        for i in range(3):
            for j in range(3):
                if board[i][j] == ' ':
                    board[i][j] = 'X'
                    best = max(best, minimax(board, depth + 1, not is_max))
                    board[i][j] = ' '
        return best
    else:
        best = math.inf
        for i in range(3):
            for j in range(3):
                if board[i][j] == ' ':
                    board[i][j] = 'O'
                    best = min(best, minimax(board, depth + 1, not is_max))
                    board[i][j] = ' '
        return best

def find_best_move(board, player):
    best_val = -math.inf if player == 'X' else math.inf
    best_move = (-1, -1)
    
    for i in range(3):
        for j in range(3):
            if board[i][j] == ' ':
                board[i][j] = player
                move_val = minimax(board, 0, player == 'O')
                board[i][j] = ' '
                if (player == 'X' and move_val > best_val) or (player == 'O' and move_val < best_val):
                    best_move = (i, j)
                    best_val = move_val
    
    return best_move

def print_board(board):
    for row in board:
        print(" | ".join(row))
    print("\n")

def play_ai_vs_human():
    board = [[' ' for _ in range(3)] for _ in range(3)]
    human_player = input("Choisissez votre symbole (X ou O) : ").upper()
    ai_player = 'O' if human_player == 'X' else 'X'
    current_player = 'X'
    
    while is_moves_left(board) and evaluate(board) == 0:
        print_board(board)
        if current_player == human_player:
            move = None
            while move not in range(1, 10):
                try:
                    move = int(input("Entrez votre coup (1-9) : ")) - 1
                    row, col = divmod(move, 3)
                    if board[row][col] == ' ':
                        board[row][col] = human_player
                    else:
                        print("Case déjà prise, essayez encore.")
                        move = None
                except (ValueError, IndexError):
                    print("Entrée invalide, veuillez choisir un nombre entre 1 et 9.")
        else:
            print("Tour de l'IA...")
            move = find_best_move(board, ai_player)
            board[move[0]][move[1]] = ai_player
        
        current_player = 'O' if current_player == 'X' else 'X'
    
    print_board(board)
    result = evaluate(board)
    if result == 1:
        print("X gagne !")
    elif result == -1:
        print("O gagne !")
    else:
        print("Match nul !")

# Lancer une partie IA vs Humain
play_ai_vs_human()





# algo search
# puis adapté au min max
# puis augmenter la taille de la grille
# mène vers l'ajout de alpha/beta
