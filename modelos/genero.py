import json
from crud import CRUD


# MODELO

class Genero:
  def __init__(self, id, genero):
    self.__id = id
    self.__genero = genero

  # GETs E SETs

  def set_id(self, g):
     self.__id = g
    
  def get_id(self):
    return self.__id

  def set_genero(self, g):
    if g != "": 
       self.__genero = g
    else: 
      raise ValueError("O nome do gênero não pode ser vazio")
    
  def get_genero(self):
    return self.__genero

  def __str__(self):
    print (f"Gênero: {self.__genero}")


# PERSISTÊNCIA (herança CRUD)

class Generos(CRUD):
  def atualizar(self, obj):
    g = self.listar_id(obj.id)
    if g:
      g.genero = obj.genero
      self.salvar()
  
  def salvar(self):
    with open("generos.json", mode="w") as arquivo:
      json.dump(self.objetos, arquivo, default = vars)
  
  def abrir(self):
    self.objetos = []
    try:
      with open("generos.json", mode="r") as arquivo:   # r - read
        texto = json.load(arquivo)
        for obj in texto:   
          g = Genero(obj["__id"], obj["__genero"])
          self.objetos.append(g)
    except FileNotFoundError:
      pass
  
Generos.salvar()