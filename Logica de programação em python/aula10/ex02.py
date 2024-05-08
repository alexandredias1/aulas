alunos = int(input("Quantos alunos tem na turma: "))

lista = []

for i in range(alunos):
    nomes = input(f"Diga o nome de cada aluno {i + 1}: ").lower()
    lista.append(nomes)

quantAlunos1 = lista.count("enzo")
quantAlunos2 = lista.count("valentina")

print(f"Nessa turma de {alunos} alunos(a), tem o total de {quantAlunos1} Enzos e {quantAlunos2} Valentinas.")