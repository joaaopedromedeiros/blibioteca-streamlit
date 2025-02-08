from models.emprestimo import Emprestimo, Emprestimos
from models.genero import Genero, Generos
from models.livro import Livro, Livros
from models.usuario import Usuario, Usuarios


class View:
    #Usuarios

    @classmethod
    def Usuario_Listar(cls):
        return Usuarios.Listar()
    
    @classmethod
    def Usuario_Atualizar(cls, id, nome, email, senha):
        u = Usuario(id, nome, email, senha)
        return Usuarios.Atualizar(u)
    
    @classmethod
    def Usuario_Inserir(cls, nome, email, senha):
        u = Usuarios(0, nome, email, senha)
        return Usuarios.Inserir(u)
    
    @classmethod
    def Usuario_Excluir(cls, id):
        for i in Usuarios.Listar():
            if i.get_id() == id:
                return Usuarios.Excluir(i)
    
    #Livro

    @classmethod
    def Livro_Listar(cls):
        return Livros.Listar()
    
    @classmethod
    def Livro_Atualizar(cls, id, livro, autor, idGenero, editora, ano, quantidade):
        l = Livro(id, livro, autor, idGenero, editora, ano, quantidade)
        return Livros.Atualizar(l)
    
    @classmethod
    def Livro_Inserir(cls, livro, autor, idGenero, editora, ano, quantidade):
        l = Livro(0, livro, autor, idGenero, editora, ano, quantidade)
        return Livros.Inserir(l)
    
    @classmethod
    def Livro_Excluir(cls, id):
        for i in Livros.Listar():
            if i.get__id() == id:
                return Livros.Excluir(i)


    
    #Generos

    @classmethod
    def Genero_Listar(cls):
        return Generos.Listar()
    
    #Emprestimo
    def Emprestimo_Listar(cls):
        return Emprestimos.Listar()

