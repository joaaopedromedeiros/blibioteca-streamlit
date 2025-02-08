from crud import CRUD
import json

class Usuario:
    def __init__(self, id, nome, email, senha):
        self.__id = id
        self.__nome = nome
        self.__email = email
        self.__senha = senha
    
    #gets
    def get_id(self):
        return self.__id
    
    def get_nome(self):
        return self.__nome
    
    def get_email(self):
        return self.__email
    
    def get_senha(self):
        return self.__senha
    
    #sets

    def set_id(self, id):
        if id == '' or ' ':
            raise ValueError("Atributo ID vazio")
        else:
            self.__id = id

    def set_nome(self, nome):
        if nome == '' or ' ':
            raise ValueError("Atributo Nome vazio")
        else:
            self.__nome = nome

    def set_email(self, email):
        if email == '' or ' ':
            raise ValueError("Atributo Email vazio")
        else:
            self.__email = email

    def set_senha(self, senha):
        if senha == '' or ' ':
            raise ValueError("Atributo Senha vazio")
        else:
            self.__senha = senha
    
    def __str__(self):
        return f'Id: {self.__id} - Nome: {self.__nome} - Email: {self.__email} - Senha: {self.__senha}'

class Usuarios(CRUD):

    @classmethod
    def Atualizar(cls, usuario):
        u = CRUD.Listar_Id(usuario)
        u.set_id(usuario.get_id())
        u.set_nome(usuario.get_nome())
        u.set_email(usuario.get_email())
        u.set_senha(usuario.get_senha())
        Usuarios.Salvar()


    @classmethod
    def Salvar(cls):
        with open("usuarios.json", mode="w") as file:
            json.dump(cls.__objetos, file, default=vars, indent=1)
    
    @classmethod
    def Abrir(cls):
        try:
            cls.__objetos = [ ]
            with open("usuarios.json", mode="r") as file:
                texto = json.load(file)
                for objeto in texto:
                    u = Usuario(objeto["_Usuario__id"],objeto["_Usuario__id"],objeto["_Usuario__nome"],objeto["_Usuario__email"],objeto["_Usuario__senha"])
                    cls.__objetos.append(u)
        except FileNotFoundError:
         pass

