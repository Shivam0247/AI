# Evaluate the board
def evaluate(board):
    # Check rows, columns, diagonals for a win
    for row in range(3):
        if board[row][0] == board[row][1] == board[row][2]:
            if board[row][0] == 'X': return 1
            if board[row][0] == 'O': return -1
    for col in range(3):
        if board[0][col] == board[1][col] == board[2][col]:
            if board[0][col] == 'X': return 1
            if board[0][col] == 'O': return -1
    if board[0][0] == board[1][1] == board[2][2]:
        if board[0][0] == 'X': return 1
        if board[0][0] == 'O': return -1
    if board[0][2] == board[1][1] == board[2][0]:
        if board[0][2] == 'X': return 1
        if board[0][2] == 'O': return -1
    return 0  # Draw

# MinMax function
def minmax(board, depth, isMaximizingPlayer):
    score = evaluate(board)
    
    # If the game is over (win or draw)
    if score == 1 or score == -1 or isFull(board):
        return score
    
    if isMaximizingPlayer:
        best = -float('inf')  # Maximize for X
        for move in getPossibleMoves(board):
            makeMove(board, move, 'X')
            best = max(best, minmax(board, depth+1, False))
            undoMove(board, move)
        return best
    
    else:
        best = float('inf')  # Minimize for O
        for move in getPossibleMoves(board):
            makeMove(board, move, 'O')
            best = min(best, minmax(board, depth+1, True))
            undoMove(board, move)
        return best

# Find the best move for X (Maximizing Player)
def findBestMove(board):
    bestVal = -float('inf')
    bestMove = None
    for move in getPossibleMoves(board):
        makeMove(board, move, 'X')
        moveVal = minmax(board, 0, False)
        undoMove(board, move)
        if moveVal > bestVal:
            bestMove = move
            bestVal = moveVal
    return bestMove

# Check if board is full
def isFull(board):
    for row in board:
        for cell in row:
            if cell == ' ':
                return False
    return True

# Get possible moves
def getPossibleMoves(board):
    moves = []
    for i in range(3):
        for j in range(3):
            if board[i][j] == ' ':
                moves.append((i, j))
    return moves

# Make a move on the board
def makeMove(board, move, player):
    i, j = move
    board[i][j] = player

# Undo a move
def undoMove(board, move):
    i, j = move
    board[i][j] = ' '

# Main function to run the game
def playTicTacToe(board):
    while not isFull(board):
        printBoard(board)
        move = findBestMove(board)
        makeMove(board, move, 'X')
        if evaluate(board) == 1:
            printBoard(board)
            print("X Wins!")
            break
        if isFull(board):
            printBoard(board)
            print("It's a Draw!")
            break
        # Add O's move randomly or you can simulate player O as well.
        # Example: simulateRandomMove(board)

# Printing the board
def printBoard(board):
    for row in board:
        print("|".join(row))
        print("-" * 5)
