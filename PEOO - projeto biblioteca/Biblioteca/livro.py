# C - Create - Insere um objeto na lista
# R - Read   - Listar os objetos da lista
# U - Update - Atualizar um objeto na lista
# D - Delete - Exclui um objeto da lista

import json
# Modelo
class Livro:
  def __init__(self, id, livro, autor,idGenero): #Construtor que inicializa os atributos do livro
    self.id = id #Atributos
    self.livro = livro #Atributos
    self.autor = autor #Atributos
    self.idGenero = idGenero #Atributos
  def __str__(self):
    return f"{self.id} - {self.livro} - {self.autor} - {self.idGenero}" #Método que retorna uma representação em string do objeto Livro

# Persistência
class Livros:
  objetos = []    # atributo estático

  @classmethod
  def inserir(cls, obj):
    cls.abrir()
    # calcular o ID
    n = 0
    for c in cls.objetos:
      if c.id > n:
        n = c.id
    obj.id = n + 1
    cls.objetos.append(obj)
    cls.salvar()

  @classmethod
  def listar(cls):
    cls.abrir()
    return cls.objetos

  @classmethod
  def listar_id(cls, id):
    cls.abrir()
    for c in cls.objetos:
      if c.id == id: 
        return c
    return None  

  @classmethod
  def atualizar(cls, obj):
    c = cls.listar_id(obj.id)
    if c != None:
      c.livro = obj.livro
      c.autor = obj.autor
      c.idGenero = obj.idGenero
      cls.salvar()

  @classmethod
  def excluir(cls, obj):
    c = cls.listar_id(obj.id)
    if c != None:
      cls.objetos.remove(c)
      cls.salvar()

  @classmethod
  def abrir(cls):
    cls.objetos = []
    try:
      with open("livros.json", mode="r") as arquivo:   # r - read 
        texto = json.load(arquivo)
        for obj in texto:   
          c = Livro(obj["id"], obj["livro"], obj["autor"], obj["idGenero"])
          cls.objetos.append(c)
    except FileNotFoundError:
      pass

  @classmethod
  def salvar(cls):
    with open("livros.json", mode="w") as arquivo:   # w - write
      json.dump(cls.objetos, arquivo, default = vars)
