from Models.ZonasEntretenimiento import ZonasEntretenimiento
from Repository.ZonasEntretenimientoRepository import ZonasEntretenimientoRepository

class ZonasEntretenimientoService:
    
    def __init__(self):
        pass
    
    def InsertarZonaEntretenimiento(self):
        print("\n--- INSERTAR NUEVA ZONA DE ENTRETENIMIENTO ---")
        
        nombre = input("Ingrese el nombre de la zona: ")
        descripcion = input("Ingrese la descripción de la zona: ")
        
        print("\n--- ESTADOS DISPONIBLES ---")
        print("1. Disponible")
        print("2. En mantenimiento")
        print("3. Cerrada temporalmente")
        
        try:
            estado_opcion = int(input("Seleccione el estado (1-3): "))
            if estado_opcion in [1, 2, 3]:
                estado = estado_opcion
            else:
                print("Estado no válido. Se asignará estado 'Disponible' por defecto.")
                estado = 1
        except ValueError:
            print("Entrada no válida. Se asignará estado 'Disponible' por defecto.")
            estado = 1
        
        entidad_zona = ZonasEntretenimiento()
        entidad_zona.set_nombre(nombre)
        entidad_zona.set_descripcion(descripcion)
        entidad_zona.set_estado(estado)
        
        respuesta = ZonasEntretenimientoRepository().insertar(entidad_zona)
        if respuesta:
            print("Zona de entretenimiento insertada correctamente.")
        else:
            print("Error al insertar zona de entretenimiento.")
    
    def ActualizarZonaEntretenimiento(self):
        print("\n--- ACTUALIZAR ZONA DE ENTRETENIMIENTO ---")
        
        self.MostrarZonasEntretenimiento()
        
        try:
            id_zona = int(input("Ingrese el ID de la zona a actualizar: "))
            
            nombre = input("Ingrese el nuevo nombre de la zona: ")
            descripcion = input("Ingrese la nueva descripción de la zona: ")
            
            print("\n--- ESTADOS DISPONIBLES ---")
            print("1. Disponible")
            print("2. En mantenimiento")
            print("3. Cerrada temporalmente")
            
            try:
                estado_opcion = int(input("Seleccione el nuevo estado (1-3): "))
                if estado_opcion in [1, 2, 3]:
                    estado = estado_opcion
                else:
                    print("Estado no válido. Se mantendrá el estado anterior.")
                    return
            except ValueError:
                print("Entrada no válida.")
                return
            
            entidad_zona = ZonasEntretenimiento()
            entidad_zona.set_id(id_zona)
            entidad_zona.set_nombre(nombre)
            entidad_zona.set_descripcion(descripcion)
            entidad_zona.set_estado(estado)
            
            respuesta = ZonasEntretenimientoRepository().actualizar(entidad_zona)
            if respuesta:
                print("Zona de entretenimiento actualizada correctamente.")
            else:
                print("Error al actualizar zona de entretenimiento.")
        except ValueError:
            print("Error: Debe ingresar un ID válido.")
    
    def EliminarZonaEntretenimiento(self):
        print("\n--- ELIMINAR ZONA DE ENTRETENIMIENTO ---")
        
        self.MostrarZonasEntretenimiento()
        
        try:
            id_zona = int(input("Ingrese el ID de la zona a eliminar: "))
            
            confirmacion = input(f"¿Está seguro de eliminar la zona con ID {id_zona}? (s/n): ")
            if confirmacion.lower() == 's':
                respuesta = ZonasEntretenimientoRepository().eliminar(id_zona)
                if respuesta:
                    print("Zona de entretenimiento eliminada correctamente.")
                else:
                    print("Error al eliminar zona de entretenimiento.")
            else:
                print("Eliminación cancelada.")
        except ValueError:
            print("Error: Debe ingresar un ID válido.")
    
    def obtener_descripcion_estado(self, estado):
        estados = {
            1: "Disponible",
            2: "En mantenimiento", 
            3: "Cerrada temporalmente"
        }
        return estados.get(estado, "Estado desconocido")
    
    def MostrarZonasEntretenimiento(self):
        print("\n--- ZONAS DE ENTRETENIMIENTO ---")
        zonas = ZonasEntretenimientoRepository().consultar_todas_zonas_entretenimiento()
        
        if zonas:
            print(f"{'ID':<5} {'Nombre':<20} {'Descripción':<40} {'Estado':<20}")
            print("-" * 85)
            for zona in zonas:
                estado_desc = self.obtener_descripcion_estado(zona[3])
                print(f"{zona[0]:<5} {zona[1]:<20} {zona[2]:<40} {estado_desc:<20}")
        else:
            print("No hay zonas de entretenimiento registradas.")
    
    def ConsultarZonasEntretenimiento(self):
        """Consulta y muestra todas las zonas de entretenimiento"""
        self.MostrarZonasEntretenimiento()
    
    def MenuZonasEntretenimiento(self):
        """Menú principal para gestión de zonas de entretenimiento"""
        while True:
            print("\n")
            print("      GESTIÓN DE ZONAS DE ENTRETENIMIENTO")
            print("="*50)
            print("1. Insertar zona de entretenimiento")
            print("2. Actualizar zona de entretenimiento") 
            print("3. Eliminar zona de entretenimiento")
            print("4. Consultar zonas de entretenimiento")
            print("5. Volver al menú principal")
            print("="*50)
            
            try:
                opcion = int(input("Seleccione una opción: "))
                
                if opcion == 1:
                    self.InsertarZonaEntretenimiento()
                elif opcion == 2:
                    self.ActualizarZonaEntretenimiento()
                elif opcion == 3:
                    self.EliminarZonaEntretenimiento()
                elif opcion == 4:
                    self.ConsultarZonasEntretenimiento()
                elif opcion == 5:
                    break
                else:
                    print("Opción no válida. Intente nuevamente.")
            except ValueError:
                print("Error: Debe ingresar un número válido.")