import sqlite3

def create_database():
    # Establecer conexión
    conn = sqlite3.connect('inventario.db')
    cursor = conn.cursor()
    
    # 1. Crear la tabla
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS productos (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nombre TEXT NOT NULL,
            marca TEXT NOT NULL,
            precio REAL NOT NULL,
            unidades INTEGER NOT NULL
        )
    ''')
    
    # 2. LIMPIEZA (Opcional pero recomendada): 
    # Esto evita que los datos se dupliquen cada vez que corres el script
    cursor.execute('DELETE FROM productos')
    
    # Datos de ejemplo
    productos_ejemplo = [
        ('Monitor 24" FHD', 'Samsung', 1150.00, 12), ('Teclado Mecánico RGB', 'Redragon', 350.50, 20),
        ('Mouse Ergonómico', 'Logitech', 180.00, 45), ('Laptop i5 12va Gen', 'Lenovo', 5800.00, 5),
        ('Impresora EcoTank', 'Epson', 1950.00, 8), ('Resma Papel Bond A4', 'Chamex', 38.00, 100),
        ('Engrapadora de Metal', 'Artesco', 45.00, 30), ('Perforadora 2 Huecos', 'Rapid', 55.00, 15),
        ('Tinta Negra 664', 'Epson', 70.00, 50), ('Flash Drive 64GB', 'Kingston', 45.00, 60),
        ('Disco SSD 1TB', 'Western Digital', 520.00, 15), ('Cargador de Laptop', 'Dell', 250.00, 10),
        ('Mochila Antirrobo', 'Targus', 320.00, 12), ('Silla de Escritorio', 'Muebles Inti', 950.00, 6),
        ('Escritorio Moderno', 'Taboada', 1200.00, 4), ('Lámpara de Mesa LED', 'Xiaomi', 210.00, 10),
        ('Cable HDMI 4K', 'Ugreen', 65.00, 30), ('Router Doble Banda', 'TP-Link', 420.00, 14),
        ('Cámara Web 1080p', 'Logitech', 480.00, 10), ('Audífonos con Mic', 'Sony', 280.00, 22),
        ('Pilas Alcalinas AA', 'Duracell', 35.00, 80), ('Supresor de Picos', 'Forza', 85.00, 25),
        ('Folder con Clip', 'Artesco', 8.50, 150), ('Bolígrafo Azul (Caja)', 'Bic', 45.00, 40),
        ('Marcadores de Pizarra', 'Faber-Castell', 32.00, 50), ('Cuaderno de 100 Hojas', 'Top', 15.00, 120),
        ('Calculadora Científica', 'Casio', 165.00, 20), ('Pizarra Acrílica', 'Quartz', 280.00, 5),
        ('Tijeras de Oficina', 'Stanley', 18.00, 40), ('Pegamento en Barra', 'Pritt', 12.00, 90),
        ('Clips para Papel', 'Torre', 6.50, 200), ('Notas Adhesivas', '3M', 14.00, 110),
        ('Organizador de Archivos', 'Acrimet', 55.00, 20), ('Pasta Térmica MX-4', 'Arctic', 75.00, 15),
        ('Ventilador para PC', 'Cooler Master', 95.00, 18), ('Tableta Gráfica', 'Huion', 680.00, 7),
        ('Smartphone Redmi 12', 'Xiaomi', 1450.00, 9), ('Funda para Celular', 'Spigen', 110.00, 30),
        ('Adaptador USB-C a RJ45', 'Ugreen', 145.00, 15), ('Cable de Red Cat6 5m', 'Nexxt', 25.00, 40),
        ('Folder Plástico A4', 'Loro', 4.50, 300), ('Borrador de Goma', 'Pelikan', 3.50, 180),
        ('Sacapuntas de Metal', 'Faber-Castell', 5.00, 150), ('Grapas 26/6 (Caja)', 'Rapid', 12.00, 70),
        ('Corrector en Cinta', 'Liquid Paper', 18.00, 60), ('Chinchetas de Colores', 'Maped', 8.00, 100),
        ('Cinta de Embalaje', 'Tesa', 16.00, 55), ('Portaminas 0.5mm', 'Pentel', 25.00, 45),
        ('Minas de Grafito HB', 'Rotring', 10.00, 80), ('Mouse Pad Gamer', 'Havit', 45.00, 40)
    ]
    
    # 3. Insertar los datos
    cursor.execute('DELETE FROM productos')
    cursor.executemany('''
        INSERT INTO productos (nombre, marca, precio, unidades)
        VALUES (?, ?, ?, ?)
    ''', productos_ejemplo)
    
    # 4. GUARDAR (Importante: El commit es lo que escribe físicamente en el disco)
    conn.commit()
    
    # 5. Verificación inmediata en consola
    cursor.execute('SELECT COUNT(*) FROM productos')
    total = cursor.fetchone()[0]
    
    conn.close()
    print(f"¡Éxito! Base de datos 'inventario.db' lista con {total} productos.")

if __name__ == '__main__':
    create_database()