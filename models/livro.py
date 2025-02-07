from crud import CRUD

class Livro(CRUD):
    def __init__(self, id, livro, autor, idGenero, editora, ano, quantidade):
        self.__id = id
        self.__livro = livro
        self.__autor = autor
        self.__idGenero = idGenero
        self.__editora = editora
        self.__ano = ano
        self.__quantidade = quantidade
    
    #gets

    def get_id(self):
        return self.__id
    
    def get_livro(self):
        return self.__livro
    
    def get_autor(self):
        return self.__autor
    
    def get_idGenero(self):
        return self.__idGenero
    
    def get_editora(self):
        return self.__editora
    
    def get_ano(self):
        return self.__ano
    
    def get_quantidade(self):
        return self.__quantidade
    
    #sets

    def set_id(self, id):
        self.__id = id

    def set_livro(self, livro):
        self.__livro = livro

    def set_autor(self, autor):
        self.__autor = autor

    def set_idGenero(self, idGenero):
        self.__idGenero = idGenero

    def set_editora(self, editora):
        self.__editora = editora

    def set_ano(self, ano):
        self.__ano = ano

    def set_quantidade(self, quantidade):
        self.__quantidade = quantidade
    
    def __str__(self):
        return (f'Id: {self.__id}, Livro: {self.__livro}, Autor: {self.__autor}, Gênero: {self.__idGenero}, Editora: {self.__editora}, Ano: {self.__ano}, Quantidade: {self.__quantidade}')
    

harry = Livro(1,2,3,4,5,6,7)
Livro.Inserir(harry)
Livro.Listar()