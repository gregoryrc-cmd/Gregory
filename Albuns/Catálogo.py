#Catálogo com filme, album, personagem, figurinhas.

filmes = []

def cadastrar_filmes(titulo, preco_albuns, preco_pacote):
    filme = {
        "Titulo": titulo,
        "Preco_Album": preco_albuns,
        "Preco_Pacote": preco_pacote,
        "Personagens": [],
        "Figurinhas": []
    }

    filmes.append(filme)
    return filme

def cadastrar_personagem(filme, nome):
    filme["Personagens"].append(nome)

def cadastrar_figurinha(filme, numero, personagem):
    figurinha = {
        "numero": numero,
        "personagens": personagem
    }
    filme["figurinhas"].append(figurinha)