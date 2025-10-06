from Repository.ConexionRepository import ConexionRepository
from Services.ConexionService import ConexionService
from Services.InsumosService import InsumosService  
from Services.HabitacionService import HabitacionService
from Services.TiendaLocalService import TiendaLocalService

def mostrar_menu():
    print("SISTEMA FINCA TURÍSTICA")
    print("1. Gestión de Clientes")
    print("2. Gestión de Habitaciones") 
    print("3. Gestión de Reservas")
    print("4. Gestión de Eventos")
    print("5. Gestión de Empleados")
    print("6. Gestión de Cargos")
    print("7. Gestión de Insumos")
    print("8. Gestión de Facturas")
    print("9. Gestión de Métodos de Pago")
    print("10. Gestión de Zonas de Entretenimiento")
    print("11. Gestión de Opiniones")
    print("12. Gestión de Menús")
    print("13. Gestión de Tienda Local")
    print("14. Configuraciones")
    print("15. Salir")

def Inicio():
    while True:
        mostrar_menu()
        
        # Capturar la opción del usuario
        opcion = input("\nSeleccione una opción (1-15): ").strip()
        
        if opcion == "1":
            pass
            
        elif opcion == "2":
            pass
            
        elif opcion == "3":
            pass
            
        elif opcion == "4":
            pass
            
        elif opcion == "5":
            pass
            
        elif opcion == "6":
            pass
            
        elif opcion == "7":
            servicio = InsumosService()
            servicio.MenuInsumos()
            pass
            
        elif opcion == "8":
            pass
            
        elif opcion == "9":
            pass
            
        elif opcion == "10":
            pass
        
        elif opcion == "11":
            pass
        
        elif opcion == "12":
            pass
        
        elif opcion == "13":
            servicio = TiendaLocalService()
            servicio.MenuTiendaLocal()
            
        elif opcion == "14":
            pass
        
        elif opcion == "15":
            break
            
        else:
            print("Opción inválida. Por favor ingrese un número del 1 al 15.")
        
        input("Presione Enter para continuar...")
        
Inicio()