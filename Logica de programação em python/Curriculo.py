# Especificar o nome do arquivo e o conteúdo

curriculo = input("Insira seu nome: ")
informacoes = f'{curriculo}.html'

nome = input("Insira seu nome completo: ")
email = (input("Digite seu email de contato: "))
educaçao = input("Digite sua formação: ")
Certificados = input("Informe seus cursos e certificados: ")

with open(informacoes, 'w') as arquivo:
    arquivo.writelines(f"Nome: {nome}\nEmail: {email}\nEducação: {educaçao}\nCursos e certificados: {Certificados}")

    print("Informações adicionadas com sucesso.")