somatorio = 0
x = int(input("Digite 1 caso queira somar um número e 0 caso queria ver o somatório final: "))
while x == 1:
    numero = int(input("Digite o numero que gostaria de somar: "))
    somatorio = somatorio + numero
    x = int(input("Digite 1 caso queira somar um número e 0 caso queria ver o somatório final: "))

    
print(somatorio)