# Especificar o nome do arquivo e o conteúdo
nome_arquivo = 'livros.txt'
livros = int(input("Quantos livros deseja guardar: "))

for i in range(livros):
    autor = input("Diga o nome do autor do livro: ")
    conteudo = input("Digite o nome do livro que deseja guardar: ")

    # Abrir o arquivo no modo de escrita e escrever o conteúdo
    with open(nome_arquivo, 'a') as arquivo:
        arquivo.writelines(f"Autor: {autor} - Livro: {conteudo}\n")

    print("Livro adicionado com sucesso.")
