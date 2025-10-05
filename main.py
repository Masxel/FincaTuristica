from Repository.ConexionRepository import Conexion

class ValidarConexion:
    
    def probar(self):
        try:
            conexion = Conexion()
            conexion.conectar_base_datos()
            print("Conectado")
        except:
            print("No conectado")

# Ejecutar la prueba
validar = ValidarConexion()
validar.probar()
