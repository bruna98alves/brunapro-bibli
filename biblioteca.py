from livro import Livro

class Biblioteca:
    def __init__(self):
        self.livros = []

    def adicionar(self, titulo, autor, ano, genero):  # 🆕 Adiciona o novo campo "gênero"
        self.livros.append({
            "titulo": titulo,
            "autor": autor,
            "ano": ano,
            "genero": genero  # 🆕 Armazena o gênero
        })

    def listar(self):
        if not self.livros:
            print("Nenhum livro cadastrado.")
            return

        # 🆕 Ordena os livros por título (alfabeticamente)
        livros_ordenados = sorted(self.livros, key=lambda l: l["titulo"].lower())

        for i, livro in enumerate(livros_ordenados, 1):
            print(f"{i}. {livro['titulo']} - {livro['autor']} ({livro['ano']}) | Gênero: {livro['genero']}")

    def buscar(self, termo):
        encontrados = [
            livro for livro in self.livros
            if termo.lower() in livro['titulo'].lower() or termo.lower() in livro['autor'].lower()
        ]
        if not encontrados:
            print("Nenhum livro encontrado.")
            return

        for livro in encontrados:
            print(f"{livro['titulo']} - {livro['autor']} ({livro['ano']}) | Gênero: {livro['genero']}")

    def remover(self, indice):
        if 0 <= indice < len(self.livros):
            removido = self.livros.pop(indice)
            print(f"Livro '{removido['titulo']}' removido com sucesso.")
        else:
            print("Índice inválido.")
