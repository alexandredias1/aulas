#Aprovado ou reprovado

nomeAluno = input("Insira o nome do aluno: ")
disciplina = input("Diga o nome da disciplina: ")
nota1 = float(input("Nota do primeiro bimestre: "))
nota2 = float(input("Nota do segundo bimestre: "))
nota3 = float(input("Nota do terceiro bimestre: "))
nota4 = float(input("Nota do quarto bimestre: "))

soma = nota1 + nota2 + nota3 + nota4
media = soma / 4


if media >= 6:
    print(f"Média de: {media} Aluno(a) aprovado(a)")
else:
    print(f"Média de: {media} Aluno(a) reprovado(a)")