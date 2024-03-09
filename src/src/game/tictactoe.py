import requests

def get_ai_move(array):
    # Substitua pela chamada real ao microserviço de IA
    print('got')
    response = requests.get('http://localhost:5001/ai/move', json={'board': array})
    if response.status_code == 200:
        return response.json().get('move')
    else:
        return None  # Em caso de falha na comunicação ou movimento inválido

def victory(array,c):
    if array[0][0] == c and array[0][1] == c and array[0][2] == c:
        return True
    elif array[1][0] == c and array[1][1] == c and array[1][2] == c:
        return True
    elif array[2][0] == c and array[2][1] == c and array[2][2] == c:
        return True
    elif array[0][0] == c and array[1][0] == c and array[2][0] == c:
        return True
    elif array[0][1] == c and array[1][1] == c and array[2][1] == c:
        return True
    elif array[0][2] == c and array[1][2] == c and array[2][2] == c:
        return True
    elif array[0][0] == c and array[1][1] == c and array[2][2] == c:
        return True
    elif array[0][2] == c and array[1][1] == c and array[2][0] == c:
        return True
    else:
        return False
def set(array,caractere,i,j):
    if array[i][j] == "n":
        array[i][j] = caractere
        return True
    return False
def setArray():
    array = [["n" for j in range(3)] for i in range(3)]
    return array
def check_draw(array):
    for row in array:
        for cell in row:
            if cell not in ['X', 'O']:
                return False  
    return True
def print_board(array):
    for row in array:
        print(" ".join(row))