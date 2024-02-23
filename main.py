from tictactoe import *

matriz = setArray()

while(True):
    print_board(matriz)
    i = int(input("X Escolha posicao 1: "))
    j = int(input("X Escolha posicao 2: "))
    while(not set(matriz,"X",i,j)):
        i = int(input("X NOT Escolha posicao 1: "))
        j = int(input("X NOT Escolha posicao 2: "))
    if(victory(matriz,"X")):
        print("X")
        break
    if check_draw(matriz):
        break
    print_board(matriz)
    i = int(input("O Escolha posicao 1: "))
    j = int(input("O Escolha posicao 2: "))
    while(not set(matriz,"O",i,j)):
        i = int(input("X NOT Escolha posicao 1: "))
        j = int(input("X NOT Escolha posicao 2: "))
    if(victory(matriz,"O")):
        print("O")
        break
    if check_draw(matriz):
        break