import pyodbc

class Conexion:
    __str_conexion: str = ""
    
    def _cadena_de_conexion(self) -> None:
        self.__str_conexion = """
        Driver={MySQL ODBC 9.0 Unicode Driver};
        Server=localhost;
        Database=db_fincaturistica;
        PORT=3306;
        user=user_python;
        password=Clas3s1Nt2024_!"""
        
    def conectar_base_datos(self) -> pyodbc.Connection:
        self._cadena_de_conexion()
        return pyodbc.connect(self.__str_conexion)
        
