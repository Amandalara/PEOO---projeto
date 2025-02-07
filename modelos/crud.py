from abc import ABC, abstractmethod

class CRUD(ABC):
    def __init__(self):
        self.objetos = []
    
    def inserir(self, obj):
        self.abrir()
        m = 0
        for c in self.objetos:
            if c.id > m: 
                m = c.id
        obj.id = m + 1
        self.objetos.append(obj)
        self.salvar()

    def listar_id(self, id):
        self.abrir()
        for c in self.objetos:
            if c.id == id: 
                return c    
        return None  
    
    def listar(self):
        self.abrir()
        return self.objetos

    def excluir(self, obj):
        c = self.listar_id(obj.id)
        if c != None:
            self.objetos.remove(c)
            self.salvar()

    # Classes abstratas
    
    @abstractmethod
    def atualizar(self):
        pass

    @abstractmethod
    def salvar(self):
        pass

    @abstractmethod
    def abrir(self):
        pass