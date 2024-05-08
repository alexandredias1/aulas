#Sistema de cadastro de turmas

nomeCurso = input("Insira o nome do curso: ")
quantAlunos = int(input("Insira a quantidade de alunos: "))

if quantAlunos >= 5:
    print(f"Turma para o curso de {nomeCurso}, cadastrada com sucesso!")
    
else:
    print("Numero de alunos insuficiente.")