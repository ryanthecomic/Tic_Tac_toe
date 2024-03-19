import pygame
import sys
from tictactoe import *

# Inicialização do Pygame
pygame.init()

# Definições de cores
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
AZUL = (0, 0, 255)
GREEN = (0, 255, 0)

largura, altura = 300, 300
tamanho_celula = largura // 3  # Divide a largura em 3 para o tabuleiro de jogo da velha
tela = pygame.display.set_mode((largura, altura))
# Defina a fonte para exibir "X" e "O"
fonte = pygame.font.Font(None, 100)

matriz = setArray()
# Variável para alternar entre "X" e "O"

tabuleiro = [["" for _ in range(3)] for _ in range(3)]

# Configurações da janela
WIDTH, HEIGHT = 800, 600
window = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Menu")

def reset_screen():
    global window, WIDTH, HEIGHT
    # Redefine a largura e altura da tela
    WIDTH, HEIGHT = 300, 300
    window = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("Jogo da velha")
def reset_screen_menu():
    global window, WIDTH, HEIGHT
    # Redefine a largura e altura da tela
    WIDTH, HEIGHT = 800, 600
    window = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("Jogo da velha")
def jogar_com_ia():
    reset_screen()
    global matriz
    matriz = setArray()
    control = True
    jogador = "X"
    while control:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                x, y = pygame.mouse.get_pos()
                linha_clicada = y // tamanho_celula
                coluna_clicada = x // tamanho_celula
                if matriz[linha_clicada][coluna_clicada] == "":
                    matriz[linha_clicada][coluna_clicada] = jogador
                    if victory(matriz, "O"):
                        tela_vitoriaO()
                        control = False
                        break
                    elif victory(matriz, "X"):
                        tela_vitoriaX()
                        control = False
                        break
                    elif check_draw(matriz):
                        tela_empate()
                        control = False
                        break
                    ai_move = get_ai_move(matriz)
                    set(matriz, "O", ai_move[0], ai_move[1])
                    desenhar_tabuleiro()
                    if victory(matriz, "O"):
                        tela_vitoriaO()
                        control = False
                        break
                    elif victory(matriz, "X"):
                        tela_vitoriaX()
                        control = False
                        break
                    elif check_draw(matriz):
                        tela_empate()
                        control = False
                        break
            desenhar_tabuleiro()
def tela_vitoriaX():
    update_score('Jogador X')
    while True:
        window.fill(WHITE)

        draw_text("Vitória do X", font, BLACK, window, WIDTH // 2, HEIGHT // 2)


        # Desenha o botão
        button_width, button_height = 200, 50
        button_x, button_y = (WIDTH - button_width) // 2, (HEIGHT + button_height) // 2  # Ajuste da posição do botão
        draw_button("Menu", font, BLACK, GREEN, window, button_x, button_y, button_width, button_height)

        pygame.display.update()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                mouse_x, mouse_y = pygame.mouse.get_pos()
                # Verifica se o clique ocorreu dentro da área do botão
                if button_x <= mouse_x <= button_x + button_width and button_y <= mouse_y <= button_y + button_height:
                    main_menu()
def tela_vitoriaO():
    update_score('Jogador O')
    while True:
        window.fill(WHITE)

        draw_text("Vitória do O", font, BLACK, window, WIDTH // 2, HEIGHT // 2)

        # Desenha o botão
        button_width, button_height = 200, 50
        button_x, button_y = (WIDTH - button_width) // 2, (HEIGHT + button_height) // 2  # Ajuste da posição do botão
        draw_button("Menu", font, BLACK, GREEN, window, button_x, button_y, button_width, button_height)

        pygame.display.update()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                mouse_x, mouse_y = pygame.mouse.get_pos()
                # Verifica se o clique ocorreu dentro da área do botão
                if button_x <= mouse_x <= button_x + button_width and button_y <= mouse_y <= button_y + button_height:
                    main_menu()
def tela_empate():
    while True:
        window.fill(WHITE)

        draw_text("Empate!", font, BLACK, window, WIDTH // 2, HEIGHT // 2)

        # Desenha o botão
        button_width, button_height = 200, 50
        button_x, button_y = (WIDTH - button_width) // 2, (HEIGHT + button_height) // 2  # Ajuste da posição do botão
        draw_button("Menu", font, BLACK, GREEN, window, button_x, button_y, button_width, button_height)

        pygame.display.update()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                mouse_x, mouse_y = pygame.mouse.get_pos()
                # Verifica se o clique ocorreu dentro da área do botão
                if button_x <= mouse_x <= button_x + button_width and button_y <= mouse_y <= button_y + button_height:
                    main_menu()
def jogar():
    reset_screen()
    global matriz
    matriz = setArray()
    control = True
    jogador = "X"
    while control:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                x, y = pygame.mouse.get_pos()
                linha_clicada = y // tamanho_celula
                coluna_clicada = x // tamanho_celula
                if matriz[linha_clicada][coluna_clicada] == "":
                    matriz[linha_clicada][coluna_clicada] = jogador
                    if jogador == "X":
                        jogador = "O"
                    else:
                        jogador = "X"
                if victory(matriz, "O"):
                    tela_vitoriaO()
                    control = False
                    break
                elif victory(matriz, "X"):
                    tela_vitoriaX()
                    control = False
                    break
                elif check_draw(matriz):
                    tela_empate()
                    control = False
                    break
                desenhar_tabuleiro()
        desenhar_tabuleiro()

def ranking():
    response = requests.get('http://localhost:5002/score')
    if response.status_code == 200:
        scores = response.json()
        print(f"Pontuação dos jogadores: {scores}")
    else:
        print("Falha ao obter a pontuação.")
        
def update_score(player):
    url = 'http://localhost:5002/score/update'
    data = {'winner': player}
    response = requests.post(url, json=data)

    if response.status_code == 200:
        print("Pontuação atualizada com sucesso!")
    else:
        print("Falha ao atualizar a pontuação.")
        
# Fonte e tamanho do texto
font = pygame.font.Font(None, 50)
def desenhar_tabuleiro():
    tela.fill(WHITE)
    desenhar_linhas()
    desenhar_jogadas()
    pygame.display.update()

def desenhar_linhas():
    for i in range(1, 3):
        pygame.draw.line(tela, BLACK, (0, tamanho_celula * i), (largura, tamanho_celula * i), 4)
        pygame.draw.line(tela, BLACK, (tamanho_celula * i, 0), (tamanho_celula * i, altura), 4)

def desenhar_jogadas():
    for linha in range(3):
        for coluna in range(3):
            texto = fonte.render(matriz[linha][coluna], True, AZUL)
            centro_x = coluna * tamanho_celula + tamanho_celula // 2
            centro_y = linha * tamanho_celula + tamanho_celula // 2
            tela.blit(texto, (centro_x - texto.get_width() // 2, centro_y - texto.get_height() // 2))
def draw_text(text, font, color, surface, x, y):
    text_obj = font.render(text, True, color)
    text_rect = text_obj.get_rect()
    text_rect.center = (x, y)
    surface.blit(text_obj, text_rect)
def draw_button(text, font, color, bg_color, surface, x, y, width, height):
    pygame.draw.rect(surface, bg_color, (x, y, width, height))
    draw_text(text, font, color, surface, x + width // 2, y + height // 2)
def main_menu():
    reset_screen_menu()
    while True:
        window.fill(WHITE)
        draw_text("Jogo da velha", font, BLACK, window, WIDTH // 2, HEIGHT // 4)

        # Botões do menu
        button_width, button_height = 200, 50
        button_start = pygame.Rect(WIDTH // 2 - button_width // 2, HEIGHT // 2 - button_height // 2 - 25, button_width, button_height)
        button_instrucoes = pygame.Rect(WIDTH // 2 - button_width // 2, HEIGHT // 2 - button_height // 2 + 50, button_width, button_height)
        button_ranks = pygame.Rect(WIDTH // 2 - button_width // 2, HEIGHT // 2 - button_height // 2 + 125, button_width, button_height)
        button_sair = pygame.Rect(WIDTH // 2 - button_width // 2, HEIGHT // 2 - button_height // 2 + 200, button_width, button_height)

        pygame.draw.rect(window, BLACK, button_start)
        pygame.draw.rect(window, BLACK, button_instrucoes)
        pygame.draw.rect(window, BLACK, button_ranks)
        pygame.draw.rect(window, BLACK, button_sair)

        draw_text("Local", font, WHITE, window, WIDTH // 2, HEIGHT // 2 - 25)
        draw_text("vs IA", font, WHITE, window, WIDTH // 2, HEIGHT // 2 + 50)
        draw_text("Ranking", font, WHITE, window, WIDTH // 2, HEIGHT // 2 + 125)
        draw_text("Sair", font, WHITE, window, WIDTH // 2, HEIGHT // 2 + 200)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if button_start.collidepoint(pygame.mouse.get_pos()):
                    jogar()
                elif button_instrucoes.collidepoint(pygame.mouse.get_pos()):
                    jogar_com_ia()
                elif button_ranks.collidepoint(pygame.mouse.get_pos()):
                    ranking()    
                elif button_sair.collidepoint(pygame.mouse.get_pos()):
                    pygame.quit()
                    sys.exit()

        pygame.display.update()

if __name__ == "__main__":
    main_menu()
