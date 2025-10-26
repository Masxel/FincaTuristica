from Models.Cargo import Cargo
from Repository.CargoRepository import CargoRepository

class CargoService:
    
    def __init__(self):
        pass
    
    def InsertarCargo(self):
        print("\n--- INSERTAR NUEVO CARGO ---")
        descripcion = input("Ingrese la descripción del cargo: ")
        
        # Crear entidad Cargo
        entidad_cargo = Cargo()
        entidad_cargo.set_descripcion(descripcion)
        
        # Insertar usando el repository
        respuesta = CargoRepository().insertar(entidad_cargo)
        if respuesta:
            print("Cargo insertado correctamente.")
        else:
            print("Error al insertar cargo.")
    
    def ActualizarCargo(self):
        print("\n--- ACTUALIZAR CARGO ---")
        
        # Mostrar cargos disponibles
        self.MostrarCargos()
        
        try:
            id_cargo = int(input("Ingrese el ID del cargo a actualizar: "))
            nueva_descripcion = input("Ingrese la nueva descripción del cargo: ")
            
            # Crear entidad Cargo
            entidad_cargo = Cargo()
            entidad_cargo.set_id(id_cargo)
            entidad_cargo.set_descripcion(nueva_descripcion)
            
            # Actualizar usando el repository
            respuesta = CargoRepository().actualizar(entidad_cargo)
            if respuesta:
                print("Cargo actualizado correctamente.")
            else:
                print("Error al actualizar cargo.")
        except ValueError:
            print("Error: Debe ingresar un ID válido.")
    
    def EliminarCargo(self):
        print("\n--- ELIMINAR CARGO ---")
        
        # Mostrar cargos disponibles
        self.MostrarCargos()
        
        try:
            id_cargo = int(input("Ingrese el ID del cargo a eliminar: "))
            
            # Confirmar eliminación
            confirmacion = input(f"¿Está seguro de eliminar el cargo con ID {id_cargo}? (s/n): ")
            if confirmacion.lower() == 's':
                respuesta = CargoRepository().eliminar(id_cargo)
                if respuesta:
                    print("Cargo eliminado correctamente.")
                else:
                    print("Error al eliminar cargo.")
            else:
                print("Eliminación cancelada.")
        except ValueError:
            print("Error: Debe ingresar un ID válido.")
    
    def MostrarCargos(self):
        print("\n--- CARGOS DISPONIBLES ---")
        cargos = CargoRepository().consultar_todos_cargos()
        
        if cargos:
            print(f"{'ID':<5} {'Descripción':<30}")
            print("-" * 35)
            for cargo in cargos:
                print(f"{cargo[0]:<5} {cargo[1]:<30}")
        else:
            print("No hay cargos disponibles.")
    
    def ConsultarCargos(self):
        """Consulta y muestra todos los cargos"""
        self.MostrarCargos()
    
    def MenuCargos(self):
        """Menú principal para gestión de cargos"""
        while True:
            print("\n")
            print("         GESTIÓN DE CARGOS")
            print("="*40)
            print("1. Insertar cargo")
            print("2. Actualizar cargo") 
            print("3. Eliminar cargo")
            print("4. Consultar cargos")
            print("5. Volver al menú principal")
            print("="*40)
            
            try:
                opcion = int(input("Seleccione una opción: "))
                
                if opcion == 1:
                    self.InsertarCargo()
                elif opcion == 2:
                    self.ActualizarCargo()
                elif opcion == 3:
                    self.EliminarCargo()
                elif opcion == 4:
                    self.ConsultarCargos()
                elif opcion == 5:
                    break
                else:
                    print("Opción no válida. Intente nuevamente.")
            except ValueError:
                print("Error: Debe ingresar un número válido.")