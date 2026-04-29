from database import DatabaseConnection

class Producto:
    """Modelo de un producto del inventario."""
    def __init__(self, id=None, nombre=None, marca=None, precio=None, unidades=None):
        self.id = id
        self.nombre = nombre
        self.marca = marca
        self.precio = precio
        self.unidades = unidades

    def to_dict(self):
        """Convierte la instancia en un diccionario para JSON."""
        return {
            'id': self.id,
            'nombre': self.nombre,
            'marca': self.marca,
            'precio': self.precio,
            'unidades': self.unidades
        }

class ProductoRepository:
    """Repositorio que encapsula las consultas a la base de datos usando POO."""

    def __init__(self, db_connection):
        self.db = db_connection

    def guardar(self, datos):
        """Inserta un nuevo producto y devuelve su ID."""
        query = '''
            INSERT INTO productos (nombre, marca, precio, unidades)
            VALUES (?, ?, ?, ?)
        '''
        # Aseguramos la conversión de tipos antes de la inserción
        params = (
            datos.get('nombre'),
            datos.get('marca'),
            float(datos.get('precio', 0)),
            int(datos.get('unidades', 0))
        )
        
        # Ejecutamos usando la conexión activa del objeto DatabaseConnection
        cursor = self.db.connection.cursor()
        cursor.execute(query, params)
        self.db.connection.commit()
        return cursor.lastrowid

    def buscar(self, nombre=None, marca=None, precio_min=None, precio_max=None, unidades_min=None, sort_by='nombre', order='asc'):
        """
        Realiza búsquedas dinámicas y permite ordenar los resultados de forma segura.
        """
        query = "SELECT * FROM productos WHERE 1=1"
        params = []

        # Filtros dinámicos con limpieza de nulos/vacíos
        if nombre and nombre.strip():
            query += " AND nombre LIKE ?"
            params.append(f"%{nombre}%")
        
        if marca and marca.strip():
            query += " AND marca LIKE ?"
            params.append(f"%{marca}%")
        
        if precio_min is not None and precio_min != '':
            query += " AND precio >= ?"
            params.append(float(precio_min))
        
        if precio_max is not None and precio_max != '':
            query += " AND precio <= ?"
            params.append(float(precio_max))
        
        if unidades_min is not None and unidades_min != '':
            query += " AND unidades >= ?"
            params.append(int(unidades_min))

        # --- LÓGICA DE ORDENAMIENTO SEGURA ---
        columnas_permitidas = ['id', 'nombre', 'marca', 'precio', 'unidades']
        
        # Validación de columna (Whitelist)
        columna = sort_by if sort_by in columnas_permitidas else 'nombre'
        
        # Validación de dirección
        sentido = 'ASC' if str(order).lower() == 'asc' else 'DESC'
        
        query += f" ORDER BY {columna} {sentido}"

        # Ejecución (rows devuelve una lista de diccionarios gracias a row_factory)
        rows = self.db.execute_query(query, params)
        
        # Retorno de lista de objetos Producto
        return [Producto(**row) for row in rows]