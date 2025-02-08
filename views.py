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
    
    @classmethod
    def Genero_Atualizar(cls, id, genero):
        g = Genero(id, genero)
        return Generos.Atualizar(g)
    
    @classmethod
    def Genero_Inserir(cls, genero):
        g = Genero(0, genero)
        return Generos.Inserir(g)
    
    @classmethod
    def Genero_Excluir(cls, id):
        for i  in Generos.Listar():
            if i.get_id() == id:
                return Generos.Excluir(i)
    
    #Emprestimo
    def Emprestimo_Listar(cls):
        return Emprestimos.Listar()
    
    def Emprestimo_Atualizar(cls, id, idUsuario, idQuantidade):
        e = Emprestimo(id, idUsuario, idQuantidade)
        return Emprestimos.Atualizar(e)
    
    def Emprestimo_Inserir(cls, idUsuario, idQuantidade):
        e = Emprestimo(0,idUsuario, idQuantidade)
        return Emprestimos.Inserir(e)
    
    def Emprestimo_Excluir(cls, id):
        for i in Emprestimos.Listar():
            if i.get_id() == id:
                return Emprestimos.Excluir(i)


