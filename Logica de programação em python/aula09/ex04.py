from multi import multiplicação, divisao, soma, subtracao

while True:
    opcao = int(input("Digite 1 para somar 2 números\nDigite 2 para multiplicar\nDigite 3 para dividir\nDigite 4 para subtrair\nDigite 5 para encerrar o programa: "))

    if opcao == 1:
        num1 = int(input("Digite o 1° número: "))
        num2 = int(input("Digite o 2° número: "))
        soma1 = soma(num1, num2)
        print(f"O resultado da soma é: {soma1}")
    elif opcao == 2:
        num1 = int(input("Digite o 1° número: "))
        num2 = int(input("Digite o 2° número: "))
        multiplicação1 = multiplicação(num1, num2)
        print(f"O resultado da multiplicação: {multiplicação1}")
    elif opcao == 3:
        num1 = int(input("Digite o 1° número: "))
        num2 = int(input("Digite o 2° número: "))
        divisao1 = divisao(num1, num2)
        print(f"O resultado da divisão: {divisao1}")
    elif opcao == 4:
        num1 = int(input("Digite o 1° número: "))
        num2 = int(input("Digite o 2° número: "))
        subtracao1 = subtracao(num1, num2)
        print(f"O resultado da subtração: {subtracao1}")
    elif opcao == 5:
        break