import numpy as np

ROWS = 6
COLUMNS = 7

class Connect4:
    def __init__(self):
        self.board = self.create_board()

    def create_board(self):
        return np.zeros((ROWS, COLUMNS))

    def drop_piece(self, board, row, col, piece):
        board[row][col] = piece

    def is_valid_location(self, board, col):
        return board[ROWS - 1][col] == 0

    def get_next_open_row(self, board, col):
        for r in range(ROWS):
            if board[r][col] == 0:
                return r

    def winning_move(self, board, piece):
        # Check horizontal locations for win
        for c in range(COLUMNS - 3):
            for r in range(ROWS):
                if board[r][c] == piece and board[r][c + 1] == piece and board[r][c + 2] == piece and board[r][c + 3] == piece:
                    return True

        # Check vertical locations for win
        for c in range(COLUMNS):
            for r in range(ROWS - 3):
                if board[r][c] == piece and board[r + 1][c] == piece and board[r + 2][c] == piece and board[r + 3][c] == piece:
                    return True

        # Check positively sloped diagonals
        for c in range(COLUMNS - 3):
            for r in range(ROWS - 3):
                if board[r][c] == piece and board[r + 1][c + 1] == piece and board[r + 2][c + 2] == piece and board[r + 3][c + 3] == piece:
                    return True

        # Check negatively sloped diagonals
        for c in range(COLUMNS - 3):
            for r in range(3, ROWS):
                if board[r][c] == piece and board[r - 1][c + 1] == piece and board[r - 2][c + 2] == piece and board[r - 3][c + 3] == piece:
                    return True

        return False

    def is_terminal_node(self, board):
        return self.winning_move(board, 1) or self.winning_move(board, 2) or len(self.get_valid_locations(board)) == 0

    def get_valid_locations(self, board):
        valid_locations = []
        for col in range(COLUMNS):
            if self.is_valid_location(board, col):
                valid_locations.append(col)
        return valid_locations

    def reset_board(self):
        self.board = self.create_board()