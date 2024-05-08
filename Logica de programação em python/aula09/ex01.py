from exemplo01 import dobro

saldo = float(input("Digite seu saldo atual: "))

if saldo >= 0 or saldo <= 0:
    limite = dobro(saldo)

    print(f"Seu limite atual é de: {limite: .2f}")
else:
    print("Valor inválido")
