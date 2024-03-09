from flask import Flask, request, jsonify, redirect, url_for, render_template
from werkzeug.security import generate_password_hash, check_password_hash

app = Flask(__name__, template_folder='templates')

# Simples banco de dados de usuários (em memória para fins de exemplo)
users = {
    "user1": {"password": generate_password_hash("pass1")},
    "user2": {"password": generate_password_hash("pass2")}
}

@app.route('/', methods=['GET'])
def home():
    return render_template('home.html')


@app.route('/signup', methods=['GET'])
def signup():
    return render_template('signup.html')

@app.route('/signup', methods=['POST'])
def process_signup():
    data = request.get_json()
    username = data.get('username')
    password = data.get('password')

    if username in users:
        return jsonify({'error': 'Nome de usuário já existe'}), 400

    hashed_password = generate_password_hash(password)
    users[username] = {'password': hashed_password}
    return jsonify({'message': 'Cadastro realizado com sucesso'}), 201

@app.route('/recover_password', methods=['GET'])
def recover():
    return render_template('recover_password.html')

@app.route('/recover_password', methods=['POST'])
def process_recover():
    data = request.get_json()
    username = data.get('username')
    password = data.get('password')

    if username not in users or not check_password_hash(users[username]['password'], password):
        return jsonify({'error': 'Credenciais inválidas'}), 401

    # Redirecione para a página do jogo após o login bem-sucedido
    return redirect(url_for('game'))

@app.route('/login', methods=['POST'])
def login():
    data = request.get_json()
    username = data.get('username')
    password = data.get('password') 

    if username not in users or not check_password_hash(users[username]['password'], password):
        return jsonify({'error': 'Credenciais inválidas'}), 401

    return jsonify({'message': 'Login bem-sucedido'}), 200

@app.route('/game', methods=['GET'])
def game():
    return render_template('game.html')

if __name__ == '__main__':
    app.run(debug=True, port=5000)