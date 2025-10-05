from Repository.ConexionRepository import ConexionRepository

class ConexionService:
    
    # Metodo basico para validar la conexion a la base de datos.
    def ValidarConexion(self):
        try:
            conexion = ConexionRepository()
            conexion.conectar_base_datos()
            print("Conectado")
            conexion.cerrar_conexion(conexion)
        except:
            print("No se pudo conectar")