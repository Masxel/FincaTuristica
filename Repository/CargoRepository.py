from Repository.ConexionRepository import ConexionRepository

class CargoRepository:
    
    def __init__(self):
        self.conexion = ConexionRepository()
    
    def insertar(self, cargo):
        try:
            cursor = self.conexion.obtener_cursor()
            cursor.execute("CALL proc_insertar_cargo(?)", (cargo.get_descripcion(),))
            cursor.commit()
            return True
        except Exception as e:
            print(f"Error al insertar cargo: {str(e)}")
            return False
        finally:
            cursor.close()
    
    def actualizar(self, cargo):
        try:
            cursor = self.conexion.obtener_cursor()
            cursor.execute("CALL proc_actualizar_cargo(?, ?)", 
                         (cargo.get_id(), cargo.get_descripcion()))
            cursor.commit()
            return True
        except Exception as e:
            print(f"Error al actualizar cargo: {str(e)}")
            return False
        finally:
            cursor.close()
    
    def eliminar(self, id):
        try:
            cursor = self.conexion.obtener_cursor()
            cursor.execute("CALL proc_eliminar_cargo(?)", (id,))
            cursor.commit()
            return True
        except Exception as e:
            print(f"Error al eliminar cargo: {str(e)}")
            return False
        finally:
            cursor.close()
    
    def consultar_todos_cargos(self):
        try:
            cursor = self.conexion.obtener_cursor()
            cursor.execute("CALL proc_consultar_cargos()")
            resultados = cursor.fetchall()
            return resultados
        except Exception as e:
            print(f"Error al consultar cargos: {str(e)}")
            return []
        finally:
            cursor.close()
    
    def consultar(self):
        return self.consultar_todos_cargos()