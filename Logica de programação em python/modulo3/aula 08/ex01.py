nome_turma = 'turma.txt'

for i in range(5):
    adicao = input("O que deseja adicionar?(Nome / Matricula / CPF / CEP / Email): ")
    if adicao == "nome":
        nome = input("Insira o nome do aluno(a): ")
    elif adicao == "cpf":
        cpf = int(input("Insira o CPF do aluno(a): "))
    elif adicao == "matricula":
        matricula = int(input("Insira o número de matricula: "))
    elif adicao == "email":
        email = input("Insira o email do aluno(a): ")
    elif adicao == "cep":
        cep = int(input("Insira o CEP do aluno(a): "))

with open(nome_turma, 'w') as arquivo:
    arquivo.writelines(f"Matricula: {matricula}\nNome: {nome}\nEmail: {email}\nCPF: {cpf}\nCEP: {cep}")
    arquivo.writelines(nome_turma)