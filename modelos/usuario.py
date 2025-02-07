import json
from crud import CRUD

# MODELO

class Usuario:
    def __init__(self, id, nome, email, senha):
        self.__id = id
        self.__nome = nome
        self.__email = email
        self.__senha = senha

    # GETs E SETs

    def set_id(self, g):
        self.__id = g
    
    def get_id(self):
        return self.__id

    def set_nome(self, g):
        if g != "": 
            self.__nome = g
        else: 
            raise ValueError("O nome do usuário não pode ser vazio")
    
    def get_nome(self):
        return self.__nome

    def set_email(self, g):
        if g != "": 
            self.__email = g
        else: 
            raise ValueError("Digite um email")
    
    def get_email(self):
        return self.__email

    def set_senha(self, g):
        if g != "": 
            self.__senha = g
        else: 
            raise ValueError("Digite uma senha")
    
    def get_senha(self):
        return self.__senha

    # str

    def __str__(self):
        print (f"Gênero: {self.__nome}")


# PERSISTÊNCIA (herança CRUD)

class Usuarios(CRUD):
    def atualizar(self, obj):
        g = self.listar_id(obj.id)
        if g:
            g.nome = obj.nome
            g.email = obj.email
            g.senha = obj.senha
            self.salvar()
    
    def salvar(self):
        with open("usuarios.json", mode="w") as arquivo:
            json.dump(self.objetos, arquivo, default = vars)
    
    def abrir(self):
        self.objetos = []
        try:
                with open("usuarios.json", mode="r") as arquivo:   # r - read
                    texto = json.load(arquivo)
                    for obj in texto:   
                        g = Usuario(obj["__id"], obj["__nome"], obj["__email"], obj["__senha"])
                        self.objetos.append(g)
        except FileNotFoundError:
            pass