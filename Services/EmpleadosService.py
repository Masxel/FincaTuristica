from Models.Empleados import Empleados
from Repository.EmpleadosRepository import EmpleadosRepository
from Repository.CargoRepository import CargoRepository

class EmpleadosService:
    
    UltimoId: int
    
    def __init__(self):
        pass
    
    def mostrar_cargos_disponibles(self):
        print("\n--- CARGOS DISPONIBLES ---")
        cargos = CargoRepository().consultar_todos_cargos()
        if cargos:
            for cargo in cargos:
                print(f"{cargo[0]}. {cargo[1]}")
        else:
            print("No hay cargos disponibles.")
        return cargos
    
    def solicitar_cargo(self):
        while True:
            cargos = self.mostrar_cargos_disponibles()
            if not cargos:
                print("Error: No hay cargos disponibles. Debe crear cargos primero.")
                return None
            
            try:
                cargo_seleccionado = int(input("Seleccione el cargo (ID): "))
                # Validar que el cargo existe
                cargo_valido = any(cargo[0] == cargo_seleccionado for cargo in cargos)
                if cargo_valido:
                    return cargo_seleccionado
                else:
                    print("Error: Cargo no válido. Intente nuevamente.")
            except ValueError:
                print("Error: Debe ingresar un número válido.")
    
    def InsertarEmpleado(self):
        print("\n--- INSERTAR NUEVO EMPLEADO ---")
        
        nombre = input("Ingrese el nombre del empleado: ")
        apellido = input("Ingrese el apellido del empleado: ")
        telefono = input("Ingrese el teléfono del empleado: ")
        email = input("Ingrese el email del empleado: ")
        
        # Solicitar cargo
        cargo = self.solicitar_cargo()
        if cargo is None:
            return
        
        # Crear entidad Empleado
        entidad_empleado = Empleados()
        entidad_empleado.set_nombre(nombre)
        entidad_empleado.set_apellido(apellido)
        entidad_empleado.set_telefono(telefono)
        entidad_empleado.set_email(email)
        entidad_empleado.set_cargo(cargo)
        
        # Insertar usando el repository
        respuesta = EmpleadosRepository().insertar(entidad_empleado)
        if respuesta:
            print("Empleado insertado correctamente.")
        else:
            print("Error al insertar empleado.")
    
    def ActualizarEmpleado(self):
        print("\n--- ACTUALIZAR EMPLEADO ---")
        
        # Mostrar empleados disponibles
        self.MostrarEmpleados()
        
        try:
            id_empleado = int(input("Ingrese el ID del empleado a actualizar: "))
            
            nombre = input("Ingrese el nuevo nombre del empleado: ")
            apellido = input("Ingrese el nuevo apellido del empleado: ")
            telefono = input("Ingrese el nuevo teléfono del empleado: ")
            email = input("Ingrese el nuevo email del empleado: ")
            
            # Solicitar nuevo cargo
            cargo = self.solicitar_cargo()
            if cargo is None:
                return
            
            # Crear entidad Empleado
            entidad_empleado = Empleados()
            entidad_empleado.set_id(id_empleado)
            entidad_empleado.set_nombre(nombre)
            entidad_empleado.set_apellido(apellido)
            entidad_empleado.set_telefono(telefono)
            entidad_empleado.set_email(email)
            entidad_empleado.set_cargo(cargo)
            
            # Actualizar usando el repository
            respuesta = EmpleadosRepository().actualizar(entidad_empleado)
            if respuesta:
                print("Empleado actualizado correctamente.")
            else:
                print("Error al actualizar empleado.")
        except ValueError:
            print("Error: Debe ingresar un ID válido.")
    
    def EliminarEmpleado(self):
        print("\n--- ELIMINAR EMPLEADO ---")
        
        # Mostrar empleados disponibles
        self.MostrarEmpleados()
        
        try:
            id_empleado = int(input("Ingrese el ID del empleado a eliminar: "))
            
            # Confirmar eliminación
            confirmacion = input(f"¿Está seguro de eliminar el empleado con ID {id_empleado}? (s/n): ")
            if confirmacion.lower() == 's':
                respuesta = EmpleadosRepository().eliminar(id_empleado)
                if respuesta:
                    print("Empleado eliminado correctamente.")
                else:
                    print("Error al eliminar empleado.")
            else:
                print("Eliminación cancelada.")
        except ValueError:
            print("Error: Debe ingresar un ID válido.")
    
    def MostrarEmpleados(self):
        print("\n--- EMPLEADOS REGISTRADOS ---")
        empleados = EmpleadosRepository().consultar_todos_empleados()
        
        if empleados:
            print(f"{'ID':<5} {'Nombre':<15} {'Apellido':<15} {'Teléfono':<12} {'Email':<25} {'Cargo':<20}")
            print("\n")
            for empleado in empleados:
                # empleado = (id, nombre, apellido, telefono, email, cargo_id, cargo_descripcion)
                print(f"{empleado[0]:<5} {empleado[1]:<15} {empleado[2]:<15} {empleado[3]:<12} {empleado[4]:<25} {empleado[6]:<20}")
        else:
            print("No hay empleados registrados.")
    
    def ConsultarEmpleados(self):
        self.MostrarEmpleados()
    
    def MenuEmpleados(self):
        while True:
            print("\n" + "="*50)
            print("         GESTIÓN DE EMPLEADOS")
            print("="*50)
            print("1. Insertar empleado")
            print("2. Actualizar empleado") 
            print("3. Eliminar empleado")
            print("4. Consultar empleados")
            print("5. Volver al menú principal")
            print("="*50)
            
            try:
                opcion = int(input("Seleccione una opción: "))
                
                if opcion == 1:
                    self.InsertarEmpleado()
                elif opcion == 2:
                    self.ActualizarEmpleado()
                elif opcion == 3:
                    self.EliminarEmpleado()
                elif opcion == 4:
                    self.ConsultarEmpleados()
                elif opcion == 5:
                    break
                else:
                    print("Opción no válida. Intente nuevamente.")
            except ValueError:
                print("Error: Debe ingresar un número válido.")