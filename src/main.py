import requests
import subprocess

def signup():
    username = input("Digite o nome de usuário: ")
    email = input("Digite o e-mail: ")  # Adicione esta linha
    password = input("Digite a senha: ")

    data = {'username': username, 'email': email, 'password': password}  # Atualize esta linha
    response = requests.post('http://localhost:5000/signup', json=data)

    if response.status_code == 201:
        print("Cadastro realizado com sucesso!")
        return True
    else:
        print(f"Falha no cadastro: {response.json().get('error')}")
        return False

def login():
    username = input("Digite o nome de usuário: ")
    password = input("Digite a senha: ")

    data = {'username': username, 'password': password}
    response = requests.post('http://localhost:5000/login', json=data)

    if response.status_code == 200:
        print("Login bem-sucedido!")
        return True
    else:
        print(f"Falha no login: {response.json().get('error')}")
        return False
    
def recover_password(): #Recuperar senha
    username = input("Digite o nome de usuário: ")
    email = input("Digite o e-mail associado à conta: ") 

    data = {'username': username, 'email': email} 
    response = requests.post('http://localhost:5000/recover_password', json=data)

    if response.status_code == 200:
        print("Um e-mail de recuperação de senha foi enviado. Verifique sua caixa de entrada.")
        return True
    else:
        print(f"Falha ao recuperar senha: {response.json().get('error')}")
        return False

def main():
    while True:
        print("1. Cadastrar")
        print("2. Login")
        print("3. Recuperar Senha")
        print("4. Sair")
        choice = input("Escolha uma opção (1, 2, 3, 4): ")

        if choice == "1":
            if signup():
                continue
        elif choice == "2":
            if login():
                print("Escolha a opção de jogo:")
                print("1. Jogo Local (Dois Jogadores)")
                print("2. Jogo contra a IA")
                print("3. Voltar ao Menu Principal")
                subprocess.run(["python", "src/game/init.py"])
                SystemExit()
                break
        elif choice == "3":
            if recover_password():
                break
        elif choice == "4":
            print("Saindo...")
            break
        else:
            print("Escolha uma opção válida.")

if __name__ == "__main__":
    main()
