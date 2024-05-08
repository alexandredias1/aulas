Categoria = int(input("Insira o numero da categoria: "))
distancia = float(input("Qual a distancia que você irá percorrer: "))

catBlack = distancia * 2
catConfort = distancia * 1.5
catConvencional = distancia
catTaxi = distancia * 3

if Categoria == 1:
    print(f"Você selecionou a categoria Black\nTotal a pagar: {catBlack}")
elif Categoria == 2:
    print(f"Você selecionou a categoria Confort\nTotal a pagar: {catConfort}") 
elif Categoria == 3:
    print(f"Você selecionou a categoria Convencional\nTotal a pagar: {catConvencional}")
elif Categoria == 4:
    print(f"Você selecionou a categoria Taxi\nTotal a pagar: {catTaxi}")
else:
    print("Número da categoria inválida.")   