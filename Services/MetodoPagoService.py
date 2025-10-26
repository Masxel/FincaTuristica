from Models.MetodoPago import MetodoPago
from Repository.MetodoPagoRepository import MetodoPagoRepository

class MetodoPagoService:
    
    def __init__(self):
        pass
    
    def InsertarMetodoPago(self):
        print("\n--- INSERTAR NUEVO MÉTODO DE PAGO ---")
        descripcion = input("Ingrese la descripción del método de pago: ")
        
        # Crear entidad MetodoPago
        entidad_metodo_pago = MetodoPago()
        entidad_metodo_pago.set_descripcion(descripcion)
        
        # Insertar usando el repository
        respuesta = MetodoPagoRepository().insertar(entidad_metodo_pago)
        if respuesta:
            print("Método de pago insertado correctamente.")
        else:
            print("Error al insertar método de pago.")
    
    def ActualizarMetodoPago(self):
        print("\n--- ACTUALIZAR MÉTODO DE PAGO ---")
        
        # Mostrar métodos de pago disponibles
        self.MostrarMetodosPago()
        
        try:
            id_metodo_pago = int(input("Ingrese el ID del método de pago a actualizar: "))
            nueva_descripcion = input("Ingrese la nueva descripción del método de pago: ")
            
            # Crear entidad MetodoPago
            entidad_metodo_pago = MetodoPago()
            entidad_metodo_pago.set_id(id_metodo_pago)
            entidad_metodo_pago.set_descripcion(nueva_descripcion)
            
            # Actualizar usando el repository
            respuesta = MetodoPagoRepository().actualizar(entidad_metodo_pago)
            if respuesta:
                print("Método de pago actualizado correctamente.")
            else:
                print("Error al actualizar método de pago.")
        except ValueError:
            print("Error: Debe ingresar un ID válido.")
    
    def EliminarMetodoPago(self):
        print("\n--- ELIMINAR MÉTODO DE PAGO ---")
        
        # Mostrar métodos de pago disponibles
        self.MostrarMetodosPago()
        
        try:
            id_metodo_pago = int(input("Ingrese el ID del método de pago a eliminar: "))
            
            # Confirmar eliminación
            confirmacion = input(f"¿Está seguro de eliminar el método de pago con ID {id_metodo_pago}? (s/n): ")
            if confirmacion.lower() == 's':
                respuesta = MetodoPagoRepository().eliminar(id_metodo_pago)
                if respuesta:
                    print("Método de pago eliminado correctamente.")
                else:
                    print("Error al eliminar método de pago.")
            else:
                print("Eliminación cancelada.")
        except ValueError:
            print("Error: Debe ingresar un ID válido.")
    
    def MostrarMetodosPago(self):
        print("\n--- MÉTODOS DE PAGO DISPONIBLES ---")
        metodos_pago = MetodoPagoRepository().consultar_todos_metodos_pago()
        
        if metodos_pago:
            print(f"{'ID':<5} {'Descripción':<30}")
            print("-" * 35)
            for metodo in metodos_pago:
                print(f"{metodo[0]:<5} {metodo[1]:<30}")
        else:
            print("No hay métodos de pago disponibles.")
    
    def ConsultarMetodosPago(self):
        """Consulta y muestra todos los métodos de pago"""
        self.MostrarMetodosPago()
    
    def MenuMetodosPago(self):
        while True:
            print("      GESTIÓN DE MÉTODOS DE PAGO")
            print("="*40)
            print("1. Insertar método de pago")
            print("2. Actualizar método de pago") 
            print("3. Eliminar método de pago")
            print("4. Consultar métodos de pago")
            print("5. Volver al menú principal")
            print("="*40)
            
            try:
                opcion = int(input("Seleccione una opción: "))
                
                if opcion == 1:
                    self.InsertarMetodoPago()
                elif opcion == 2:
                    self.ActualizarMetodoPago()
                elif opcion == 3:
                    self.EliminarMetodoPago()
                elif opcion == 4:
                    self.ConsultarMetodosPago()
                elif opcion == 5:
                    break
                else:
                    print("Opción no válida. Intente nuevamente.")
            except ValueError:
                print("Error: Debe ingresar un número válido.")