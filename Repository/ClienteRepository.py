from Repository.ConexionRepository import ConexionRepository

class ClienteRepository:
    
    def __init__(self):
        self.conexion = ConexionRepository()
    
    def insertar(self, cliente):
        pass
    
    def actualizar(self, cliente):
        pass
    
    def eliminar(self, id):
        pass
    
    def consultar(self, id=None):
        pass