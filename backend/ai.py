import numpy as np
from connect4 import Connect4, ROWS, COLUMNS

AI_PIECE = 2
PLAYER_PIECE = 1

class Connect4AI:
    def __init__(self, game):
        self.game = game

    def negamax(self, board, depth, alpha, beta, maximizing_player):
        if depth == 0 or self.game.is_terminal_node(board):
            if self.game.winning_move(board, AI_PIECE):
                return (None, 100000000000000)
            elif self.game.winning_move(board, PLAYER_PIECE):
                return (None, -10000000000000)
            else:
                return (None, 0)

        valid_locations = self.game.get_valid_locations(board)
        best_score = -np.inf if maximizing_player else np.inf
        best_col = np.random.choice(valid_locations)

        for col in valid_locations:
            row = self.game.get_next_open_row(board, col)
            b_copy = board.copy()
            self.game.drop_piece(b_copy, row, col, AI_PIECE if maximizing_player else PLAYER_PIECE)
            score = self.negamax(b_copy, depth - 1, alpha, beta, not maximizing_player)[1]

            if maximizing_player:
                if score > best_score:
                    best_score = score
                    best_col = col
                alpha = max(alpha, best_score)
            else:
                if score < best_score:
                    best_score = score
                    best_col = col
                beta = min(beta, best_score)

            if alpha >= beta:
                break

        return best_col, best_score

    def get_move(self, board):
        valid_locations = self.game.get_valid_locations(board)
        best_score = -np.inf
        best_col = np.random.choice(valid_locations)
        depth = 5

        for col in valid_locations:
            row = self.game.get_next_open_row(board, col)
            b_copy = board.copy()
            self.game.drop_piece(b_copy, row, col, AI_PIECE)
            score = self.negamax(b_copy, depth - 1, -np.inf, np.inf, False)[1]
            if score > best_score:
                best_score = score
                best_col = col

        return best_col