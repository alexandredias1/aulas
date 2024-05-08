#Olimpíadas

lista = []
lista2 = []
lista3 = []

for i in range(10):
    atletas = float(input(f"Lançamento do atleta {i + 1}: "))
    lista.append(atletas)

print(f"Ordem de lançamento dos atletas: {lista}")
lista.sort()
lista.reverse()
print(f"Os melhores lançamentos da primeira rodada: {lista}")

for i in range(6):
    atletas = float(input(f"Lançamento do atleta {i + 1}: "))
    lista2.append(atletas)

print(f"Ordem de lançamento dos atletas: {lista2}")
lista2.sort()
lista2.reverse()
print(f"Os melhores lançamentos da segunda rodada: {lista2}")

for i in range(4):
    atletas = float(input(f"Lançamento do atleta {i + 1}: "))
    lista3.append(atletas)

print(f"Ordem de lançamento dos atletas: {lista3}")
lista3.sort()
lista3.reverse()
print(f"Os melhores lançamentos da rodada final: {lista3}")