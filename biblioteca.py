from livro import Livro

class Biblioteca:
    def __init__(self):
        self.livros = []

    def adicionar(self, titulo, autor, ano):
        livro = Livro(titulo, autor, ano)
        self.livros.append(livro)

    def listar(self):
        if not self.livros:
            print("Nenhum livro cadastrado.")
        else:
            for i, livro in enumerate(self.livros, start=1):
                print(f"{i}. {livro}")

    def buscar(self, termo):
        encontrados = [livro for livro in self.livros if termo.lower() in livro.titulo.lower() or termo.lower() in livro.autor.lower()]
        if encontrados:
            for livro in encontrados:
                print(livro)
        else:
            print("Nenhum livro encontrado com esse termo.")

    def remover(self, indice):
        if 0 <= indice < len(self.livros):
            removido = self.livros.pop(indice)
            print(f"Livro '{removido.titulo}' removido com sucesso.")
        else:
            print("Índice inválido.")