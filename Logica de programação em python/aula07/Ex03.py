dataNasc = int(input("Digite seu ano de nascimento: "))
anoAtual = int(input("Insira o ano atual: "))
idade = anoAtual - dataNasc

for nascimento in range(dataNasc, anoAtual + 1):
    idade = nascimento - dataNasc
    print(f"Em {nascimento} você tinha {idade} anos")