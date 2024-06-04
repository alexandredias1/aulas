#Tupla

#Entrada de nomes
nomes = input("Digite cinco nomes, separados por vírgulas: ")

#Conversão de lista para tupla
var2 = nomes.split(",")
minha_tupla = tuple(var2)

if len(minha_tupla) != 5:
    print("Você não inseriu exatamente cinco nomes.")

else:

    nome_inserido = input("Digite um nome para verificar se está na tupla: ")

    if nome_inserido in nomes:
        print("O nome está na tupla")

    else:
        print("O nome não está na tupla")
