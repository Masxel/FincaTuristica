from Entidades.Insumos import Insumos
from Repository.InsumosRepository import InsumosRepository

class InsumosService:
    
    def InsertarInsumo(self):
        nombre = input("Ingrese el nombre del insumo: ")
        cantidad = int(input("Ingrese la cantidad del insumo: "))
        descripcion = input("Ingrese la descripcion del insumo: ")
        precio = float(input("Ingrese el precio del insumo: "))
        
        EntidadInsumo = Insumos()
        EntidadInsumo.SetNombre(nombre)
        EntidadInsumo.SetCantidad(cantidad)
        EntidadInsumo.SetDescripcion(descripcion)
        EntidadInsumo.SetPrecio(precio)

        respuesta = InsumosRepository().insertar(EntidadInsumo)
        if respuesta:
            print("Insumo insertado correctamente.")
        else:
            print("Error al insertar insumo.")
            
    def MenuInsumos(self):
        while True:
            print("\n--- Menú de Insumos ---")
            print("1. Insertar Insumo")
            print("2. Actualizar Insumo")
            print("3. Eliminar Insumo")
            print("4. Consultar Insumo")
            print("5. Salir")
            
            opcion = input("Seleccione una opción: ")
            
            if opcion == '1':
                self.InsertarInsumo()
            elif opcion == '2':
                pass
            elif opcion == '3':
                pass
            elif opcion == '4':
                pass
            elif opcion == '5':
                print("Saliendo del menú de insumos.")
                break
            else:
                print("Opción no válida. Por favor, intente de nuevo.")