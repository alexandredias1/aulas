from exemplo01 import dobro

salario = float(input("Digite seu salário atual: "))

if salario >= 0:
    decimoterceiro = dobro(salario)

    print(f"Seu salário atual é de: {salario: .2f}\nSeu 13º vai ser no valor de: {decimoterceiro: .2f}")
else:
    print("Valor inválido")
