import requests
import subprocess

def signup():
    username = input("Digite o nome de usuário: ")
    password = input("Digite a senha: ")

    data = {'username': username, 'password': password}
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

def main():
    while True:
        print("1. Cadastrar")
        print("2. Login")
        print("3. Sair")
        choice = input("Escolha uma opção (1, 2, 3): ")

        if choice == "1":
            if signup():
                break
        elif choice == "2":
            if login():
                start()
                break
        elif choice == "3":
            print("Saindo...")
            break
        else:
            print("Escolha uma opção válida.")
            
def start():
    print("Running the game...")
    subprocess.run(["python", "src/game/init.py"])
    
main()         

if __name__ == "__main__":
    main()
