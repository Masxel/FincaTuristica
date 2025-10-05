from Repository.ConexionRepository import ConexionRepository

class InsumosRepository:
    
    def __init__(self):
        self.conexion = ConexionRepository()
    
    def insertar(self, insumo):
        try:
            # Establecer conexión usando la instancia del constructor
            conn = self.conexion.conectar_base_datos()
            cursor = conn.cursor()
            
            # Preparar parámetros
            nombre = insumo.nombre
            cantidad = insumo.cantidad
            descripcion = insumo.descripcion
            precio = insumo.precio
            
            # Llamar al procedimiento almacenado
            cursor.execute(
                "CALL proc_insertar_insumos(?, ?, ?, ?, @respuesta)",
                (nombre, cantidad, descripcion, precio)
            )
            
            # Obtener el resultado de la variable @respuesta
            cursor.execute("SELECT @respuesta")
            resultado = cursor.fetchone()
            respuesta = resultado[0] if resultado else 0
            
            # Confirmar cambios y cerrar conexión
            conn.commit()
            cursor.close()
            conn.close()
            
            return respuesta
            
        except Exception as e:
            print(f"Error al insertar insumo: {e}")
            return 0
    
    def actualizar(self, insumo):
        pass
    
    def eliminar(self, id):
        pass
    
    def consultar(self, id=None):
        pass