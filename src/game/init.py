from tictactoe import setArray, print_board, set, victory, check_draw
import requests
import subprocess

def play_local():
    matriz = setArray()

    while True:
        print_board(matriz)
        print("local")
        i = int(input("Jogador X, escolha a posição 1: "))
        j = int(input("Jogador X, escolha a posição 2: "))
        
        while not set(matriz, "X", i, j):
            i = int(input("Posição já ocupada. Jogador X, escolha a posição 1: "))
            j = int(input("Jogador X, escolha a posição 2: "))
        
        if victory(matriz, "X"):
            print("Jogador X venceu!")
            break
        elif check_draw(matriz):
            print("Empate!")
            break

        print_board(matriz)
        i = int(input("Jogador O, escolha a posição 1: "))
        j = int(input("Jogador O, escolha a posição 2: "))
        
        while not set(matriz, "O", i, j):
            i = int(input("Posição já ocupada. Jogador O, escolha a posição 1: "))
            j = int(input("Jogador O, escolha a posição 2: "))
        
        if victory(matriz, "O"):
            print("Jogador O venceu!")
            break
        elif check_draw(matriz):
            print("Empate!")
            break

def play_vs_ai():
    matriz = setArray()

    while True:
        print_board(matriz)
        i = int(input("Jogador X, escolha a posição 1: "))
        j = int(input("Jogador X, escolha a posição 2: "))
        
        while not set(matriz, "X", i, j):
            i = int(input("Posição já ocupada. Jogador X, escolha a posição 1: "))
            j = int(input("Jogador X, escolha a posição 2: "))
        
        if victory(matriz, "X"):
            print("Jogador X venceu!")
            break
        elif check_draw(matriz):
            print("Empate!")
            break

        # Comunicação com o serviço da IA
        ai_move = get_ai_move(matriz)
        print(f"IA escolheu a posição {ai_move}")
        set(matriz, "O", ai_move[0], ai_move[1])

        if victory(matriz, "O"):
            print("IA venceu!")
            break
        elif check_draw(matriz):
            print("Empate!")
            break

def get_ai_move(board):
    # Comunicação com o serviço da IA
    url = 'http://localhost:5001/ai/move'
    data = {'board': board}
    response = requests.get(url, json=data)

    if response.status_code == 200:
        move = response.json().get('move')
        return move
    else:
        raise Exception(f"Falha ao obter movimento da IA: {response.json().get('error')}")

if __name__ == "__main__":
    play_option = input("Escolha o modo de jogo: ")
    
    if play_option == "1":
        play_option = "local"
        play_local()
    elif play_option == "2":
        play_option == "vs_ai"
        play_vs_ai()
    elif play_option == "3":
        subprocess.run(["python", "src/main.py"])
        SystemExit()
    else:
        print("Modo de jogo inválido.")
