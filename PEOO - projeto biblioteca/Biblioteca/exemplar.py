# C - Create - Insere um objeto na lista
# R - Read   - Listar os objetos da lista
# U - Update - Atualizar um objeto na lista
# D - Delete - Exclui um objeto da lista

import json
from livro import Livro, Livros

# Modelo
class Exemplar:
  def __init__(self, id, idLivro, ano, editora):
    self.id = id
    self.editora = editora
    self.ano = ano
    self.idLivro = idLivro
  def __str__(self):
    return f"{self.id} - {self.idLivro} - {self.ano} - {self.editora}"

# Persistência
class Exemplares:
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
      c.editora = obj.editora
      c.ano = obj.ano
      c.idLivro = obj.idLivro
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
      with open("exemplares.json", mode="r") as arquivo:   # r - read 
        texto = json.load(arquivo)
        for obj in texto:   
          c = Exemplar(obj["id"], obj["idLivro"], obj["editora"], obj["ano"])
          cls.objetos.append(c)
    except FileNotFoundError:
      pass

  @classmethod
  def salvar(cls):
    with open("exemplares.json", mode="w") as arquivo:   # w - write
      json.dump(cls.objetos, arquivo, default = vars)
