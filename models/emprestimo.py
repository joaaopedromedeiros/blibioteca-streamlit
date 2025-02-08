from crud import CRUD
import json

class Emprestimo:
    def __init__(self, id, idUsuario, idQuantidade):
        self.__id = id
        self.__idUsuario = idUsuario
        self.__idQuantidade = idQuantidade

    def __str__(self):
        return f'Id: {self.__id} - idUsuario: {self.__idUsuario} - idQuantidade: {self.__idQuantidade}'

class Emprestimos(CRUD):

    @classmethod
    def Atualizar(cls, emprestimo):
        e = CRUD.Listar_Id(emprestimo)
        e.set_id(emprestimo.get_id())
        e.set_idUsuario(emprestimo.get_idUsuario())
        e.set_idQuantidade(emprestimo.get_idQuantidade())
        Emprestimos.Salvar()

    @classmethod
    def Salvar(cls):
        with open("emprestimos.json", mode="w") as file:
            json.dump(cls.__objetos, file, default=vars, indent=1)
    
    @classmethod
    def Abrir(cls):
        try:
         cls.__objetos = [ ]
         with open("emprestimos.json", mode="w") as file:
             texto = json.load(file)
             for objeto in file:
                 e = Emprestimo(objeto["_Emprestimo__id"], objeto["_Emprestimo__idUsuario"], objeto["_Emprestimo__idQuantidade"])
                 cls.__objetos.append(e)
        except FileNotFoundError:
            pass
