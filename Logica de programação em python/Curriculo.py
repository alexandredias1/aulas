# Especificar o nome do arquivo e o conteúdo

curriculo = input("Insira seu nome: ")
informacoes = f'{curriculo}.html'

nome = input("Insira seu nome completo: ")
email = (input("Digite seu email de contato: "))
educaçao = input("Digite sua formação: ")
Certificados = input("Informe seus cursos e certificados: ")

arquivohtml = """<!DOCTYPE html>
    <html lang="pt-br">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Curriculo</title>
    </head>
    <body>
        
    </body>
    </html>"""

with open(informacoes, 'w') as arquivo:
    arquivo.write(f"Nome: {nome}\nEmail: {email}\nEducação: {educaçao}\nCursos e certificados: {Certificados}")
    print("Informações adicionadas com sucesso.")
    arquivo.write(arquivohtml)