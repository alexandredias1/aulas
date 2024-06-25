import numpy as np

def inicializar_tabuleiro():
    return np.zeros((5, 5), dtype=str)

def posicionar_navios(tabuleiro):
    navio1 = (np.random.randint(0, 5), np.random.randint(0, 5))
    navio2 = (np.random.randint(0, 5), np.random.randint(0, 5))
    
    while navio2 == navio1:
        navio2 = (np.random.randint(0, 5), np.random.randint(0, 5))
    
    tabuleiro[navio1] = 'N'  # Navio marcado com 'N'
    tabuleiro[navio2] = 'N'  # Navio marcado com 'N'
    
    return tabuleiro, (navio1, navio2)

def realizar_jogada(tabuleiro, navios):
    tentativas = 0
    max_tentativas = 10
    acertou1 = False
    acertou2 = False
    
    while not (acertou1 and acertou2) and tentativas < max_tentativas:
        print("\nTabuleiro do jogador:")
        for linha in tabuleiro:
            print(' '.join(linha))
        
        while True:
            try:
                linha = int(input("Jogador, adivinhe a linha (0-4): "))
                if linha < 0 or linha > 4:
                    raise ValueError
                break
            except ValueError:
                print("Entrada inválida. Digite um número entre 0 e 4.")
        
        while True:
            try:
                coluna = int(input("Jogador, adivinhe a coluna (0-4): "))
                if coluna < 0 or coluna > 4:
                    raise ValueError
                break
            except ValueError:
                print("Entrada inválida. Digite um número entre 0 e 4.")
        
        tentativas += 1
        if (linha, coluna) in navios:
            print(f"Jogador, você acertou um navio em {tentativas} tentativas!")
            if (linha, coluna) == navios[0]:
                acertou1 = True
            else:
                acertou2 = True
            tabuleiro[linha, coluna] = 'X'  # Marca o navio acertado com 'X' no tabuleiro
        else:
            if tabuleiro[linha, coluna] == '-':
                print("Você já tentou essa posição. Tente novamente.")
            else:
                tabuleiro[linha, coluna] = '-'  # Marca a posição tentada com '-' no tabuleiro
                print("Jogador, você errou! Tente novamente.")
    
    if not (acertou1 and acertou2):
        print(f"Jogador, você excedeu o número máximo de tentativas ({max_tentativas}).")
        print(f"Os navios estavam nas posições {navios[0]} e {navios[1]}.")
    else:
        print("\nTabuleiro final do jogador:")
        for linha in tabuleiro:
            print(' '.join(linha))

def jogo_batalha_naval():
    print("Bem-vindos ao jogo de Batalha Naval para 2 jogadores!")
    print("Cada jogador terá dois navios escondidos no tabuleiro. O objetivo é acertar os navios do oponente.")
    
    tabuleiro_jogador1 = inicializar_tabuleiro()
    tabuleiro_jogador2 = inicializar_tabuleiro()
    
    tabuleiro_jogador1, navios_jogador1 = posicionar_navios(tabuleiro_jogador1)
    tabuleiro_jogador2, navios_jogador2 = posicionar_navios(tabuleiro_jogador2)
    
    print("\nTabuleiro do Jogador 1:")
    for linha in tabuleiro_jogador1:
        print(' '.join(linha))
    
    print("\nTabuleiro do Jogador 2:")
    for linha in tabuleiro_jogador2:
        print(' '.join(linha))
    
    print("\nJogador 1, é sua vez!")
    realizar_jogada(tabuleiro_jogador2, navios_jogador2)
    
    print("\nJogador 2, é sua vez!")
    realizar_jogada(tabuleiro_jogador1, navios_jogador1)

# Exemplo de uso
jogo_batalha_naval()
