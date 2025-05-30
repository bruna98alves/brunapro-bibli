from biblioteca import Biblioteca
from arquivo import salvar_livros, carregar_livros

def menu():
    print("\n=== Sistema de Cadastro de Livros ===")
    print("1. Cadastrar livro")
    print("2. Listar livros")
    print("3. Buscar livro")
    print("4. Remover livro")
    print("5. Sair")

biblioteca = Biblioteca()
carregar_livros(biblioteca)

while True:
    menu()
    opcao = input("Escolha: ")

    if opcao == "1":
        titulo = input("Título: ")
        autor = input("Autor: ")
        ano = input("Ano: ")
        genero= input("Genero:")
        biblioteca.adicionar(titulo, autor, ano, genero)
        salvar_livros(biblioteca)
        print("Livro cadastrado com sucesso!")

    elif opcao == "2":
        biblioteca.listar()

    elif opcao == "3":
        termo = input("Digite título ou autor para buscar: ")
        biblioteca.buscar(termo)

    elif opcao == "4":
        biblioteca.listar()
        try:
            indice = int(input("Digite o número do livro para remover: ")) - 1
            biblioteca.remover(indice)
            salvar_livros(biblioteca)
        except ValueError:
            print("Por favor, insira um número válido.")

    elif opcao == "5":
        print("Saindo... Até logo!")
        break

    else:
        print("Opção inválida. Tente novamente.")