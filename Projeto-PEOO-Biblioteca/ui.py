import views

class UI:
  @staticmethod
  def menu():
    print("\n------------- Biblioteca virtual -------------\n")
    print("----------- Cadastro de livros -----------")
    print("  1 - Inserir livros, 2 - Listar livros, 3 - Atualizar livros, 4 - Excluir livros\n")
    print("----------- Cadastro de gêneros -----------")
    print("  5 - Inserir gênero, 6 - Listar gênero, 7 - Atualizar gênero, 8 - Excluir gênero\n")
    print("----------- Cadastro de exemplar -----------")
    print("  9 - Inserir exemplar, 10 - Listar exemplar, 11 - Atualizar exemplar, 12 - Excluir exemplar ")
    print("  13- sair\n")

    return int(input("Informe uma opção: "))

  @staticmethod
  def main():
    op = 0
    while op != 13:
      op = UI.menu()
      if op == 1: UI.livro_inserir()
      if op == 2: UI.livro_listar()
      if op == 3: UI.livro_atualizar()
      if op == 4: UI.livro_excluir()
      if op == 5: UI.genero_inserir()
      if op == 6: UI.genero_listar()
      if op == 7: UI.genero_atualizar()
      if op == 8: UI.genero_excluir()
      if op == 9: UI.exemplar_inserir()
      if op == 10: UI.exemplar_listar()
      if op == 11: UI.exemplar_atualizar()
      if op == 12: UI.exemplar_excluir()

  @staticmethod
  def livro_inserir():
    nome = input("Informe o nome do livro: ")
    autor = input("Informe o autor do livro: ")
    UI.genero_listar()
    idGenero = int(input("Digite o id do gênero do livro escolhido:"))  
    views.livro_inserir(nome, autor, idGenero)

  @staticmethod
  def livro_listar():  
    for c in views.livro_listar():
      print(c)

  @staticmethod
  def livro_atualizar():
    UI.livro_listar()
    id = int(input("Informe o id do livro a ser atualizado: "))
    nome = input("Informe o novo nome: ")
    autor = input("Informe o novo autor: ")
    UI.genero_listar()
    idGenero = input("Informe o novo gênero: ")
    views.livro_atualizar(id, nome, autor, idGenero)

  @staticmethod
  def livro_excluir():
    UI.livro_listar()
    id = int(input("Informe o id do livro a ser excluído: "))
    views.livro_excluir(id)

  @staticmethod
  def genero_inserir():
    genero = input("Informe o gênero: ")
    views.genero_inserir(genero)

  @staticmethod
  def genero_listar():  
    for c in views.genero_listar():
        print(c)

  @staticmethod
  def genero_atualizar():
    UI.genero_listar()
    id = int(input("Informe o id do livro a ser atualizado: "))
    genero = input("Informe o novo gênero: ")
    views.genero_atualizar(id, genero)

  @staticmethod
  def genero_excluir():
    UI.genero_listar()
    id = int(input("Informe o id do gênero a ser excluído: "))
    views.genero_excluir(id)

  def exemplar_inserir():
    UI.livro_listar()
    idLivro = int(input("Digite o id do livro escolhido:"))  
    ano = input("Informe o ano do exemplar: ")
    editora = input("Informe a editora do exemplar: ")
    views.exemplar_inserir(idLivro, ano, editora)

  @staticmethod
  def exemplar_listar():  
    for c in views.exemplar_listar():
      print(c)

  @staticmethod
  def exemplar_atualizar():
    UI.exemplar_listar()
    id = int(input("Informe o id do exemplar a ser atualizado: "))
    ano = input("Informe o novo ano: ")
    editora = input("Informe a nova editora: ")
    UI.exemplar_listar()
    idLivro = input("Informe o livro a ser atualizado: ")
    views.exemplar_atualizar(id, ano, editora, idLivro)

  @staticmethod
  def exemplar_excluir():
    UI.exemplar_listar()
    id = int(input("Informe o id do exemplar a ser excluído: "))
    views.exemplar_excluir(id)

UI.main()
