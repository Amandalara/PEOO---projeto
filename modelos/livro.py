import json
from crud import CRUD

# MODELO

class Usuario:
    def __init__(self, id, livro, autor, idGenero, editora, ano, quantidade):
        self.__id = id
        self.__livro = livro
        self.__autor = autor
        self.__idGenero = idGenero
        self.__editora = editora
        self.__ano = ano
        self.__quantidade = quantidade

    # GETs E SETs
    #Lembrar de ver como colocar o id genero

    def set_id(self, g):
        self.__id = g
    
    def get_id(self):
        return self.__id

    def set_livro(self, g):
        if g != "": 
            self.__livro = g
        else: 
            raise ValueError("O nome do livro não pode ser vazio")
    
    def get_nome(self):
        return self.__livro

    def set_autor(self, g):
        if g != "": 
            self.__autor = g
        else: 
            raise ValueError("O nome do autor não pode ser vazio")
    
    def get_autor(self):
        return self.__autor

    def set_editora(self, g):
        if g != "": 
            self.__editora = g
        else: 
            raise ValueError("O nome do editora não pode ser vazio")
    
    def get_editora(self):
        return self.__editora

    def set_ano(self, g):
        if g != "": 
            self.__ano = g
        else: 
            raise ValueError("O ano não pode ser vazio")
    
    def get_ano(self):
        return self.__ano
    
    def set_quantidade(self, g):
        self.__quantidade = g
    
    def get_quantidade(self):
        return self.__quantidade

    # str

    def __str__(self):
        print (f"Livro: {self.__livro} - {self.__autor} - {self.__idGenero} - {self.__editora} - {self.__ano} - {self.__quantidade}")


# PERSISTÊNCIA (herança CRUD)

class Livros(CRUD):
    def atualizar(self, obj):
        g = self.listar_id(obj.id)
        if g:
            g.livro = obj.livro
            g.autor = obj.autor
            g.idGenero = obj.idGenero
            g.editora = obj.editora
            g.ano = obj.ano
            g.quantidade = obj.quantidade
            self.salvar()
    
    def salvar(self):
        with open("livros.json", mode="w") as arquivo:
            json.dump(self.objetos, arquivo, default = vars)
    
    def abrir(self):
        self.objetos = []
        try:
                with open("livros.json", mode="r") as arquivo:   # r - read
                    texto = json.load(arquivo)
                    for obj in texto:   
                        g = Usuario(obj["__id"], obj["__livro"], obj["__autor"], obj["__idGenero"], obj["__editora"], obj["__ano"], obj["__quantidade"])
                        self.objetos.append(g)
        except FileNotFoundError:
            pass