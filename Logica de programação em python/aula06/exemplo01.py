idade = int(input("Digite sua idade: "))
assinante = input("Você é assinante do game pass? (sim/não): ").lower()

#A função "lower" serve para colocar a resposta em minusculo.

if idade >= 18 and assinante == "sim":
    print("Você tem acesso ao game pass!")
else:
    print("Você não tem acesso ao game pass.")