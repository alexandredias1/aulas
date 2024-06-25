import numpy as np

def jogo_batalha_naval():
    tabuleiro = np.zeros((5, 5), dtype=int)
    posicao_navio = (np.random.randint(0, 5), np.random.randint(0, 5))
    tentativas = 0
    acertou = False
    
    while not acertou:
        print("\nTabuleiro:")
        print(tabuleiro)
        linha = int(input("Adivinhe a linha (0-4): "))
        coluna = int(input("Adivinhe a coluna (0-4): "))
        tentativas += 1
        if (linha, coluna) == posicao_navio:
            print(f"Você acertou o navio em {tentativas} tentativas!")
            acertou = True
        else:
            tabuleiro[linha, coluna] = -1
            print("Errou! Tente novamente.")

jogo_batalha_naval()