from crud import CRUD
import  json

class Genero:
    def __init__(self, id, genero):
        self.__id = id
        self.__genero = genero

    #gets

    def get_id(self):
        return self.__id
    
    def get_genero(self):
        return self.__genero
    
    #sets

    def set_id(self, id):
        self.__id = id
    
    def set_genero(self, genero):
        self.__genero = genero
    
    def __str__(self):
        return f'Id: {self.__id} - Genero: {self.__genero}'

class Generos(CRUD):


    @classmethod
    def Atualizar(cls, genero):
        g = CRUD.Listar_Id(genero)
        g.set_id(genero.get_id())
        g.set_genero(genero.get_genero())
        Generos.Salvar()

    @classmethod
    def Salvar(cls):
        with open("generos.json", mode="w") as file:
            json.dump(cls.__objetos, file, default=vars, indent=1)
    
    @classmethod
    def Abrir(cls):
        try:
            cls.__objetos = [ ]
            with open("generos,json", mode="r") as file:
                texto = json.load(file)
                for objeto in texto:
                    g = Genero(objeto["_Genero__id"], objeto["_Genero__genero"])
                    cls.__objetos.append(g)
        except FileNotFoundError:
            pass


acao = Genero(0,"ação")
Generos.Inserir(acao)
Generos.Listar()


