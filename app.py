import flask
from Routes.ClientesRoutes import clientes_bp
from Routes.CargoRoutes import cargo_bp
from Routes.EmpleadosRoutes import empleados_bp
from Routes.EstadoHabitacionRoutes import estadohabitacion_bp

# Crear la aplicación Flask
app = flask.Flask(__name__)

# Registrar blueprints (rutas)
app.register_blueprint(clientes_bp)
app.register_blueprint(cargo_bp)
app.register_blueprint(empleados_bp)
app.register_blueprint(estadohabitacion_bp)

# Solo ejecutar si es el archivo principal
if __name__ == '__main__':
    print(f"Iniciando servidor Flask en http://localhost:4560")
    app.run('localhost', port=4560, debug=True)