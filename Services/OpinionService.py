from Models.Opinion import Opinion
from Repository.OpinionRepository import OpinionRepository
from Repository.ClienteRepository import ClienteRepository

class OpinionService:
    
    def __init__(self):
        pass
    
    def mostrar_clientes_disponibles(self):
        print("\n--- CLIENTES REGISTRADOS ---")
        clientes = ClienteRepository().consultar()
        if clientes:
            for cliente in clientes:
                print(f"{cliente[0]}. {cliente[1]} {cliente[2]} - {cliente[4]}") 
        else:
            print("No hay clientes registrados.")
        return clientes
    
    def solicitar_cliente(self):
        while True:
            clientes = self.mostrar_clientes_disponibles()
            if not clientes:
                print("Error: No hay clientes registrados. Debe registrar clientes primero.")
                return None
            
            try:
                cliente_seleccionado = int(input("Seleccione el cliente (ID): "))
                cliente_valido = any(cliente[0] == cliente_seleccionado for cliente in clientes)
                if cliente_valido:
                    return cliente_seleccionado
                else:
                    print("Error: Cliente no válido. Intente nuevamente.")
            except ValueError:
                print("Error: Debe ingresar un número válido.")
    
    def solicitar_calificacion(self):
        while True:
            print("\n--- CALIFICACIÓN ---")
            print("1 ⭐ - Muy malo")
            print("2 ⭐⭐ - Malo") 
            print("3 ⭐⭐⭐ - Regular")
            print("4 ⭐⭐⭐⭐ - Bueno")
            print("5 ⭐⭐⭐⭐⭐ - Excelente")
            
            try:
                calificacion = int(input("Ingrese su calificación (1-5): "))
                if 1 <= calificacion <= 5:
                    return calificacion
                else:
                    print("Error: La calificación debe estar entre 1 y 5.")
            except ValueError:
                print("Error: Debe ingresar un número válido.")
    
    def InsertarOpinion(self):
        print("\n--- INSERTAR NUEVA OPINIÓN ---")
        
        cliente_id = self.solicitar_cliente()
        if cliente_id is None:
            return
        
        calificacion = self.solicitar_calificacion()
        
        comentario = input("Ingrese su comentario sobre la experiencia: ")
        
        entidad_opinion = Opinion()
        entidad_opinion.set_idcliente(cliente_id)
        entidad_opinion.set_calificacion(calificacion)
        entidad_opinion.set_comentario(comentario)
        
        respuesta = OpinionRepository().insertar(entidad_opinion)
        if respuesta:
            print("Opinión insertada correctamente.")
        else:
            print("Error al insertar opinión.")
    
    def ActualizarOpinion(self):
        print("\n--- ACTUALIZAR OPINIÓN ---")
        
        # Mostrar opiniones disponibles
        self.MostrarOpiniones()
        
        try:
            id_opinion = int(input("Ingrese el ID de la opinión a actualizar: "))
            
            # Solicitar nuevo cliente
            cliente_id = self.solicitar_cliente()
            if cliente_id is None:
                return
            
            # Solicitar nueva calificación
            calificacion = self.solicitar_calificacion()
            
            # Solicitar nuevo comentario
            comentario = input("Ingrese el nuevo comentario: ")
            
            # Crear entidad Opinion
            entidad_opinion = Opinion()
            entidad_opinion.set_id(id_opinion)
            entidad_opinion.set_idcliente(cliente_id)
            entidad_opinion.set_calificacion(calificacion)
            entidad_opinion.set_comentario(comentario)
            
            # Actualizar usando el repository
            respuesta = OpinionRepository().actualizar(entidad_opinion)
            if respuesta:
                print("Opinión actualizada correctamente.")
            else:
                print("Error al actualizar opinión.")
        except ValueError:
            print("Error: Debe ingresar un ID válido.")
    
    def EliminarOpinion(self):
        print("\n--- ELIMINAR OPINIÓN ---")
        
        self.MostrarOpiniones()
        
        try:
            id_opinion = int(input("Ingrese el ID de la opinión a eliminar: "))
            
            confirmacion = input(f"¿Está seguro de eliminar la opinión con ID {id_opinion}? (s/n): ")
            if confirmacion.lower() == 's':
                respuesta = OpinionRepository().eliminar(id_opinion)
                if respuesta:
                    print("Opinión eliminada correctamente.")
                else:
                    print("Error al eliminar opinión.")
            else:
                print("Eliminación cancelada.")
        except ValueError:
            print("Error: Debe ingresar un ID válido.")
    
    def obtener_estrellas(self, calificacion):
        """Convierte la calificación numérica en estrellas visuales"""
        estrellas = {
            1: "⭐",
            2: "⭐⭐", 
            3: "⭐⭐⭐",
            4: "⭐⭐⭐⭐",
            5: "⭐⭐⭐⭐⭐"
        }
        return estrellas.get(calificacion, "Sin calificación")
    
    def MostrarOpiniones(self):
        """Muestra todas las opiniones con formato enriquecido"""
        print("\n--- OPINIONES Y RESEÑAS ---")
        opiniones = OpinionRepository().consultar_todas_opiniones()
        
        if opiniones:
            print(f"{'ID':<5} {'Cliente':<25} {'Calificación':<15} {'Comentario':<50}")
            print("-" * 95)
            for opinion in opiniones:
                cliente_nombre = f"{opinion[2]} {opinion[3]}"
                estrellas = self.obtener_estrellas(opinion[4])
                comentario_corto = opinion[5][:47] + "..." if len(opinion[5]) > 50 else opinion[5]
                print(f"{opinion[0]:<5} {cliente_nombre:<25} {estrellas:<15} {comentario_corto:<50}")
        else:
            print("No hay opiniones registradas.")
    
    def ConsultarOpiniones(self):
        self.MostrarOpiniones()
    
    def MenuOpiniones(self):
        while True:
            print("\n" + "="*50)
            print("         GESTIÓN DE OPINIONES Y RESEÑAS")
            print("="*50)
            print("1. Insertar opinión")
            print("2. Actualizar opinión") 
            print("3. Eliminar opinión")
            print("4. Consultar opiniones")
            print("5. Volver al menú principal")
            print("="*50)
            
            try:
                opcion = int(input("Seleccione una opción: "))
                
                if opcion == 1:
                    self.InsertarOpinion()
                elif opcion == 2:
                    self.ActualizarOpinion()
                elif opcion == 3:
                    self.EliminarOpinion()
                elif opcion == 4:
                    self.ConsultarOpiniones()
                elif opcion == 5:
                    break
                else:
                    print("Opción no válida. Intente nuevamente.")
            except ValueError:
                print("Error: Debe ingresar un número válido.")