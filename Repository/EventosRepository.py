from Repository.ConexionRepository import ConexionRepository

class EventosRepository:
    
    def __init__(self):
        self.conexion = ConexionRepository()
    
    def insertar(self, evento):
        try:
            cursor = self.conexion.obtener_cursor()
            cursor.execute("CALL proc_insertar_evento(?)", (evento.get_descripcion(),))
            cursor.commit()
            return True
        except Exception as e:
            print(f"Error al insertar evento: {str(e)}")
            return False
        finally:
            cursor.close()
    
    def actualizar(self, evento):
        try:
            cursor = self.conexion.obtener_cursor()
            cursor.execute("CALL proc_actualizar_evento(?, ?)", 
                         (evento.get_id(), evento.get_descripcion()))
            cursor.commit()
            return True
        except Exception as e:
            print(f"Error al actualizar evento: {str(e)}")
            return False
        finally:
            cursor.close()
    
    def eliminar(self, id):
        try:
            cursor = self.conexion.obtener_cursor()
            cursor.execute("CALL proc_eliminar_evento(?)", (id,))
            cursor.commit()
            return True
        except Exception as e:
            print(f"Error al eliminar evento: {str(e)}")
            return False
        finally:
            cursor.close()
    
    def consultar_todos_eventos(self):
        """Consulta todos los eventos disponibles"""
        try:
            cursor = self.conexion.obtener_cursor()
            cursor.execute("CALL proc_consultar_eventos()")
            resultados = cursor.fetchall()
            return resultados
        except Exception as e:
            print(f"Error al consultar todos los eventos: {str(e)}")
            return []
        finally:
            cursor.close()
    
    def consultar_evento_por_id(self, id):
        """Consulta un evento específico por ID"""
        try:
            cursor = self.conexion.obtener_cursor()
            cursor.execute("CALL proc_consultar_evento_por_id(?)", (id,))
            resultado = cursor.fetchone()
            return resultado
        except Exception as e:
            print(f"Error al consultar evento por ID: {str(e)}")
            return None
        finally:
            cursor.close()
    
    def consultar(self, id=None):
        """Método genérico que llama a los métodos específicos según el parámetro"""
        if id is None:
            return self.consultar_todos_eventos()
        else:
            return self.consultar_evento_por_id(id)