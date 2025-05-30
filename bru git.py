import json
from livro import Livro

def salvar_livros(biblioteca, arquivo='livros.json'):
    with open(arquivo, 'w') as f:
        livros_dict = [{'titulo': l.titulo, 'autor': l.autor, 'ano': l.ano} for l in biblioteca.livros]
        json.dump(livros_dict, f, indent=4)

def carregar_livros(biblioteca, arquivo='livros.json'):
    try:
        with open(arquivo, 'r') as f:
            livros_dict = json.load(f)
            for l in livros_dict:
                biblioteca.adicionar(l['titulo'], l['autor'], l['ano'])
    except FileNotFoundError:
        pass