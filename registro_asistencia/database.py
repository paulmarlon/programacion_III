import sqlite3
from datetime import datetime
DB_NAME = "asistencia.db"
def init_db():
    
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS asistentes (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nombre TEXT NOT NULL,
            email TEXT NOT NULL,
            fecha_registro TEXT NOT NULL
        )
    """)
    conn.commit()
    conn.close()

def insertar_asistente(nombre, email):
    """Guarda un nuevo asistente si el email no existe."""
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()
    
    # --- NUEVA VERIFICACIÓN ---
    cursor.execute("SELECT id FROM asistentes WHERE email = ?", (email,))
    if cursor.fetchone():
        conn.close()
        # Lanzamos una excepción personalizada
        raise ValueError("Email ya registrado")
    
    fecha = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    cursor.execute(
        "INSERT INTO asistentes (nombre, email, fecha_registro) VALUES (?, ?, ?)",
        (nombre, email, fecha)
    )
    conn.commit()
    nuevo_id = cursor.lastrowid
    conn.close()
    return nuevo_id

def obtener_todos():
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()
    cursor.execute("SELECT id, nombre, email, fecha_registro FROM asistentes")
    datos = cursor.fetchall()
    conn.close()
    return datos

if __name__ == "__main__":
    init_db()
    print("Base de datos lista.")

    id_test = insertar_asistente("Paul Quispe", "paul@example.com")
    print(f"Asistente insertado con ID: {id_test}")
    
    print("Lista de asistentes:")
    for persona in obtener_todos():
        print(persona)