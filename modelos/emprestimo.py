import json
from crud import CRUD

# MODELO

class Emprestimo:
    def __init__(self, id, idLivro, idUsuario, reserva):
        self.__id = id
        self.__idLivro = idLivro
        self.__idUsuario = idUsuario
        self.__reserva = reserva

    # GETs E SETs

    def set_id(self, g):
        self.__id = g
    
    def get_id(self):
        return self.__id

    def set_idLivro(self, g):
        self.__idLivro = g
    
    def get_idLivro(self):
        return self.__idLivro

    def set_idUsuario(self, g):
        self.__idUsuario = g
    
    def get_idUsuario(self):
        return self.__idUsuario
    
    def set_reserva(self, g):
        if isinstance(g, bool):  # Verifica se o valor é booleano
            self.__reserva = g
        else:
            raise ValueError("O valor de reserva deve ser True ou False")
    
    def get_reserva(self):
        return self.__reserva


    # str
    def __str__(self):
        print (f"Livro: {self.__idLivro} - {self.__idUsuario} - {self.__reserva}")


# PERSISTÊNCIA (herança CRUD)

class Emprestimos(CRUD):
    def atualizar(cls, obj):
        g = cls.listar_id(obj.id)
        if g:
            g.idLivro = obj.idLivro
            g.idUsuario = obj.idUsuario
            g.reserva = obj.reserva
            cls.salvar()
    
    def salvar(cls):
        with open("emprestimo.json", mode="w") as arquivo:
            json.dump(cls.objetos, arquivo, default = vars)
    
    def abrir(cls):
        cls.objetos = []
        try:
                with open("emprestimo.json", mode="r") as arquivo:   # r - read
                    texto = json.load(arquivo)
                    for obj in texto:   
                        g = Emprestimo(obj["__id"], obj["__idLivro"], obj["__idUsuario"], obj["__reserva"])
                        #Pelo reserva ser booleano irá mudar algo no arquivo json?
                        cls.objetos.append(g)
        except FileNotFoundError:
            pass

Emprestimos.salvar()