from flask import Flask, jsonify, request
import werkzeug
import random

app = Flask(__name__)

@app.route('/ai/move', methods=['GET'])
def ai_move():
    data = request.get_json()
    board = data.get('board')

    # Use a função get_ai_move
    move = get_random_move(board)

    return jsonify({'move': move})

def get_random_move(board):
    # Lógica da IA: Escolhe uma posição aleatória
    available_moves = [(i, j) for i in range(3) for j in range(3) if board[i][j] == "n"]
    if available_moves:
        return random.choice(available_moves)
    else:
        return None

if __name__ == '__main__':
    app.run(debug=True, port=5001)
