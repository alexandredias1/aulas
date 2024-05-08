lista = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

print(f"O tesouro está em um lugar da lista!\n {lista}")

x = int(input("Digite um numero para encontrar o tesouro (Você tem 3 tentativas!): "))

while x != 3:
    print("Sem tesouro!")
    x = int(input("Digite um numero para encontrar o tesouro (Você tem 2 tentativas!): "))
    if x != 3:
        x = int(input("Digite um numero para encontrar o tesouro (Você tem uma 1 tentativa!): "))
        print("Número de tentativas esgotadas.")
    break

while x == 3:
    print("Testouro encontrado!")
    break