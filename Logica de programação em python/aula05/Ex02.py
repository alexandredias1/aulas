#Loja de tapete

tapete = int(input("Digite o tipo de tapete que deseja: "))
metros = float(input("Quantos metros de tapete: "))

tapeteConvencional = metros * 10
tapetePremium = metros * 20
tapeteMax = metros * 30


if tapete == 1:
    print(f"O tipo de tapete escolhido foi o Tapete Convencional\nO orçamento ficou no valor de: {tapeteConvencional} ")
elif tapete == 2:
    print(f"O tipo de tapete escolhido foi o Tapete Premium\nO orçamento ficou no total de: {tapetePremium}")  
elif tapete == 3:
    print(f"O tipo de tapete escolhido foi o Tapete Max Premium\n O orçamento ficou no total de: {tapeteMax}")
else:
    print(f"Tipo de tapete inválido.")  