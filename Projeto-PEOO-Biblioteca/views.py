from exemplar import Exemplar, Exemplares
from genero import Genero, Generos
from livro import Livro, Livros

def livro_inserir(nome, autor, idGenero):
    c = Livro(0, nome, autor, idGenero)
    Livros.inserir(c)


def livro_listar():
    r = []
    for livro in Livros.listar():
        g = Generos.listar_id(livro.idGenero) 
        r.append(str(livro.id) + " - " + livro.livro + " - "  + livro.autor + " - " + g.genero)
    return r


def livro_atualizar(id, nome, autor, idGenero):
    c = Livro(id, nome, autor, idGenero)
    Livros.atualizar(c)


def livro_excluir(id):
    c = Livro(id, "", "", "")
    Livros.excluir(c)


def genero_inserir(genero):
    c = Genero(0, genero)
    Generos.inserir(c)
    
def genero_listar():
    return Generos.listar()

def genero_atualizar(id, genero):
    c = Genero(id, genero)
    Generos.atualizar(c)


def genero_excluir(id):
    c = Genero(id, "")
    Generos.excluir(c)

def exemplar_inserir(idLivro, ano, editora):
    c = Exemplar(0, idLivro, ano, editora)
    Exemplares.inserir(c)

def exemplar_listar():
    r = []
    for exemplar in Exemplares.listar():
        g = Livros.listar_id(exemplar.idLivro) 
        r.append(str(exemplar.id) + " - " + g.livro + " - "  + exemplar.ano + " - " + exemplar.editora)
    return r

def exemplar_atualizar(id, idLivro, ano, editora):
    c = Exemplar(id, idLivro, ano, editora)
    Exemplares.atualizar(c)

def exemplar_excluir(id):
    c = Exemplar(id, "","","")
    Exemplares.excluir(c)
