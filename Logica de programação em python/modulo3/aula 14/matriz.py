import numpy
# Cria uma matriz 3x3 com valores aleatórios entre 0 e 20
matrix = numpy.random.randint(0, 21, size =(3,3))

print("Matriz completa")
print(matrix)

valores_maiores_que_10 = matrix[matrix > 10]
print("\nValores maiores que 10:")
print(valores_maiores_que_10)