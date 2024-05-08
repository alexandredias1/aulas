somatorio = 0

x = int(input("Digite 1 se deseja somar um número, Digite 2 se quiser saber o somatório ou Digite 3 para encerrar o programa: "))

while x == 1:
        num = int(input("Digite o número que gostaria de somar: "))
        somatorio += num
        x = int(input("Digite 1 se deseja somar um número, Digite 2 se quiser saber o somatório ou Digite 3 para encerrar o programa: "))
 
if x == 2:
    print(f"O resultado é: {somatorio}")
elif x == 3:
    print("Programa encerrado.")
else:
    print("Número inválido!")

