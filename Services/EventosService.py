from Models.Eventos import Eventos
from Repository.EventosRepository import EventosRepository

class EventosService:
    
    def __init__(self):
        pass
    
    def InsertarEvento(self):
        print("\n--- INSERTAR NUEVO EVENTO ---")
        descripcion = input("Ingrese la descripción del evento: ")
        
        # Crear entidad Evento
        entidad_evento = Eventos()
        entidad_evento.set_descripcion(descripcion)
        
        # Insertar usando el repository
        respuesta = EventosRepository().insertar(entidad_evento)
        if respuesta:
            print("Evento insertado correctamente.")
        else:
            print("Error al insertar evento.")
    
    def ActualizarEvento(self):
        print("\n--- ACTUALIZAR EVENTO ---")
        
        # Mostrar eventos disponibles
        self.MostrarEventos()
        
        try:
            id_evento = int(input("Ingrese el ID del evento a actualizar: "))
            nueva_descripcion = input("Ingrese la nueva descripción del evento: ")
            
            # Crear entidad Evento
            entidad_evento = Eventos()
            entidad_evento.set_id(id_evento)
            entidad_evento.set_descripcion(nueva_descripcion)
            
            # Actualizar usando el repository
            respuesta = EventosRepository().actualizar(entidad_evento)
            if respuesta:
                print("Evento actualizado correctamente.")
            else:
                print("Error al actualizar evento.")
        except ValueError:
            print("Error: Debe ingresar un ID válido.")
    
    def EliminarEvento(self):
        print("\n--- ELIMINAR EVENTO ---")
        
        # Mostrar eventos disponibles
        self.MostrarEventos()
        
        try:
            id_evento = int(input("Ingrese el ID del evento a eliminar: "))
            
            # Confirmar eliminación
            confirmacion = input(f"¿Está seguro de eliminar el evento con ID {id_evento}? (s/n): ")
            if confirmacion.lower() == 's':
                respuesta = EventosRepository().eliminar(id_evento)
                if respuesta:
                    print("Evento eliminado correctamente.")
                else:
                    print("Error al eliminar evento.")
            else:
                print("Eliminación cancelada.")
        except ValueError:
            print("Error: Debe ingresar un ID válido.")
    
    def MostrarEventos(self):
        print("\n--- EVENTOS DISPONIBLES ---")
        eventos = EventosRepository().consultar_todos_eventos()
        
        if eventos:
            print(f"{'ID':<5} {'Descripción':<30}")
            print("-" * 35)
            for evento in eventos:
                print(f"{evento[0]:<5} {evento[1]:<30}")
        else:
            print("No hay eventos disponibles.")
    
    def ConsultarEventos(self):
        """Consulta y muestra todos los eventos"""
        self.MostrarEventos()
    
    def MenuEventos(self):
        """Menú principal para gestión de eventos"""
        while True:
            print("\n")
            print("         GESTIÓN DE EVENTOS")
            print("="*40)
            print("1. Insertar evento")
            print("2. Actualizar evento") 
            print("3. Eliminar evento")
            print("4. Consultar eventos")
            print("5. Volver al menú principal")
            print("="*40)
            
            try:
                opcion = int(input("Seleccione una opción: "))
                
                if opcion == 1:
                    self.InsertarEvento()
                elif opcion == 2:
                    self.ActualizarEvento()
                elif opcion == 3:
                    self.EliminarEvento()
                elif opcion == 4:
                    self.ConsultarEventos()
                elif opcion == 5:
                    break
                else:
                    print("Opción no válida. Intente nuevamente.")
            except ValueError:
                print("Error: Debe ingresar un número válido.")