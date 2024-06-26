import random

def imprimir_tabuleiro(tabuleiro):
    for linha in tabuleiro:
        print(" ".join(linha))

def criar_tabuleiro():
    return [["~"] * 5 for _ in range(5)]

def posicionar_navios(tabuleiro):
    navios = 3
    while navios > 0:
        linha = random.randint(0, 4)
        coluna = random.randint(0, 4)
        if tabuleiro[linha][coluna] == "~":
            tabuleiro[linha][coluna] = "N"
            navios -= 1

def obter_palpite():
    while True:
        try:
            linha = int(input("Digite a linha (0-4): "))
            coluna = int(input("Digite a coluna (0-4): "))
            if 0 <= linha <= 4 and 0 <= coluna <= 4:
                return linha, coluna
            else:
                print("Entrada inválida, por favor, digite números entre 0 e 4.")
        except ValueError:
            print("Entrada inválida, por favor, digite números entre 0 e 4.")

def principal():
    tabuleiro_j1 = criar_tabuleiro()
    tabuleiro_j2 = criar_tabuleiro()
    visao_j1 = criar_tabuleiro()
    visao_j2 = criar_tabuleiro()

    print("Jogador 1, posicione seus navios:")
    posicionar_navios(tabuleiro_j1)
    print("Jogador 2, posicione seus navios:")
    posicionar_navios(tabuleiro_j2)

    turno = 0
    while True:
        if turno % 2 == 0:
            print("Turno do Jogador 1")
            imprimir_tabuleiro(visao_j2)
            linha, coluna = obter_palpite()
            if tabuleiro_j2[linha][coluna] == "N":
                print("Acertou!")
                visao_j2[linha][coluna] = "X"
                tabuleiro_j2[linha][coluna] = "X"
            else:
                print("Errou.")
                visao_j2[linha][coluna] = "O"
        else:
            print("Turno do Jogador 2")
            imprimir_tabuleiro(visao_j1)
            linha, coluna = obter_palpite()
            if tabuleiro_j1[linha][coluna] == "N":
                print("Acertou!")
                visao_j1[linha][coluna] = "X"
                tabuleiro_j1[linha][coluna] = "X"
            else:
                print("Errou.")
                visao_j1[linha][coluna] = "O"

        if all(celula != "N" for linha in tabuleiro_j1 for celula in linha):
            print("Jogador 2 vence!")
            break
        if all(celula != "N" for linha in tabuleiro_j2 for celula in linha):
            print("Jogador 1 vence!")
            break

        turno += 1

if __name__ == "__main__":
    principal()
