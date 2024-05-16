from flask import Flask, request, jsonify
from flask_cors import CORS
from connect4 import Connect4
from ai import Connect4AI

app = Flask(__name__)
CORS(app)

game = Connect4()
ai = Connect4AI(game)

@app.route('/move', methods=['POST'])
def make_move():
    data = request.get_json()
    column = data['column']
    piece = data['piece']
    if game.is_valid_location(game.board, column):
        row = game.get_next_open_row(game.board, column)
        game.drop_piece(game.board, row, column, piece)
        return jsonify({'status': 'success'})
    else:
        return jsonify({'status': 'invalid'})

@app.route('/ai-move', methods=['POST'])
def ai_move():
    data = request.get_json()
    piece = data['piece']
    column = ai.get_move(game.board)
    row = game.get_next_open_row(game.board, column)
    game.drop_piece(game.board, row, column, piece)
    return jsonify({'status': 'success', 'column': column})

@app.route('/reset', methods=['POST'])
def reset_game():
    game.reset_board()
    return jsonify({'status': 'success'})

@app.route('/check-win', methods=['POST'])
def check_win():
    data = request.get_json()
    piece = data['piece']
    if game.winning_move(game.board, piece):
        return jsonify({'status': 'win'})
    else:
        return jsonify({'status': 'no-win'})

if __name__ == '__main__':
    app.run(debug=True)