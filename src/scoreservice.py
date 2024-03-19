from flask import Flask, jsonify, request

app = Flask(__name__)

# Dicionário para armazenar a pontuação dos jogadores
scores = {'Jogador X': 0, 'Jogador O': 0}

@app.route('/score', methods=['GET'])
def get_scores():
    return jsonify(scores)

@app.route('/score/update', methods=['POST'])
def update_score():
    data = request.get_json()
    winner = data.get('winner')

    if winner in scores:
        scores[winner] += 1
        return jsonify({'message': 'Pontuação atualizada com sucesso!'})
    else:
        return jsonify({'error': 'Jogador não encontrado!'})

if __name__ == '__main__':
    app.run(debug=True, port=5002)