class CRUD: 
    __objetos = [ ]

    @classmethod
    def Inserir(cls, obj):
        id = 0
        for i in cls.__objetos:
            if i.get_id() > obj.get_id():
                id = i.get_id()
        obj.set_id(id + 1)
        cls.__objetos.append(obj)
    
    @classmethod
    def Listar(cls):
        for i in cls.__objetos:
            print(i)
        return cls.__objetos
    
    @classmethod
    def Listar_Id(cls, id):
        for i in cls.__objetos:
            if i.get_id() == id:
                return i
    
    @classmethod
    def Atualizar(cls, objeto):
        obj = CRUD.Listar_Id(objeto)
    
    @classmethod
    def Excluir(cls, objeto):
        obj = CRUD.Listar_Id(objeto)
        cls.__objetos.remove(objeto)