from Repository.ConexionRepository import ConexionRepository
from Services import MenuAlimentacionService, MetodoPagoService, OpinionService, ZonasEntretenimientoService
from Services.CargoService import CargoService
from Services.ConexionService import ConexionService
from Services.EmpleadosService import EmpleadosService
from Services.EventosService import EventosService
from Services.InsumosService import InsumosService  
from Services.HabitacionService import HabitacionService
from Services.TiendaLocalService import TiendaLocalService
from Services.ClienteService import ClienteService
from Services.ReservaService import ReservaService

def mostrar_menu():
    print("SISTEMA FINCA TURÍSTICA")
    print("1. Gestión de Clientes")
    print("2. Gestión de Habitaciones") 
    print("3. Gestión de Reservas")
    print("4. Gestión de Empleados")
    print("5. Gestión de Cargos")
    print("6. Gestión de Insumos")
    print("7. Gestión de Facturas")
    print("8. Gestión de Métodos de Pago")
    print("9. Gestión de Zonas de Entretenimiento")
    print("10. Gestión de Opiniones")
    print("11. Gestión de Menú alimentación")
    print("12. Gestión de Tienda Local")
    print("13. Gestión de Eventos")
    print("14. Probar Conexión a la Base de Datos")
    print("15. Salir")

def Inicio():
    while True:
        mostrar_menu()
                
        opcion = input("\nSeleccione una opción (1-15): ").strip()

        if opcion == "1":
            servicio = ClienteService()
            servicio.MenuClientes()
            pass
            
        elif opcion == "2":
            servicio = HabitacionService()
            servicio.MenuHabitaciones()
            pass
            
        elif opcion == "3":
            servicio = ReservaService()
            servicio.MenuReservas()
            pass
            
        elif opcion == "4":
            servicio = EmpleadosService()
            servicio.MenuEmpleados()
            pass
            
        elif opcion == "5":
            servicio = CargoService()
            servicio.MenuCargos()
            pass

        elif opcion == "6":
            servicio = InsumosService()
            servicio.MenuInsumos()
            pass
            
        elif opcion == "7":
            pass

        elif opcion == "8":
            servicio = MetodoPagoService()
            servicio.MenuMetodosPago()
            pass

        elif opcion == "9":
            servicio = ZonasEntretenimientoService()
            servicio.MenuZonasEntretenimiento()
            pass

        elif opcion == "10":
            servicio = OpinionService()
            servicio.MenuOpiniones()
            pass
        
        elif opcion == "11":
            servicio = MenuAlimentacionService()
            servicio.MenuMenuAlimentacion()
            pass

        elif opcion == "12":
            servicio = TiendaLocalService()
            servicio.MenuTiendaLocal()
            pass

        elif opcion == "13":
            servicio = EventosService()
            servicio.MenuEventos()
            pass

        elif opcion == "14":
            servicio = ConexionService()
            servicio.probarconexion()
            break
        else:
            print("Opción inválida. Por favor ingrese un número del 1 al 15.")

        input("Presione Enter para continuar...")

# ======================= Inicio de la aplicación =======================
Inicio()