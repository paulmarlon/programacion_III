import sqlite3
import os

class DatabaseConnection:
    """Maneja la conexión a SQLite de forma orientada a objetos."""

    def __init__(self, db_name='inventario.db'):
        self.db_name = db_name
        self.connection = None

    def connect(self):
        """Establece la conexión a la base de datos."""
        try:
            self.connection = sqlite3.connect(self.db_name)
            # Permite acceder a los datos por nombre de columna (como un diccionario)
            self.connection.row_factory = sqlite3.Row  
            return self.connection
        except sqlite3.Error as e:
            print(f"Error al conectar a la base de datos: {e}")
            return None

    def close(self):
        """Cierra la conexión si existe."""
        if self.connection:
            self.connection.close()
            self.connection = None

    def execute_query(self, query, params=()):
        """Ejecuta una consulta SELECT y retorna los resultados."""
        if not self.connection:
            print("Error: No hay conexión activa.")
            return []
            
        try:
            cursor = self.connection.cursor()
            cursor.execute(query, params)
            rows = cursor.fetchall()
            return [dict(row) for row in rows]
        except sqlite3.Error as e:
            print(f"Error en la consulta: {e}")
            return []

# Ejemplo de uso:
if __name__ == '__main__':
    db = DatabaseConnection()
    if db.connect():
        # Ejemplo: Listar productos (asumiendo que la tabla existe)
        productos = db.execute_query("SELECT * FROM productos LIMIT 5")
        for p in productos:
            print(f"{p['nombre']} - {p['marca']}: ${p['precio']}")
        
        db.close()