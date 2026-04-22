import tkinter as tk
from tkinter import messagebox, ttk  # Añadimos ttk
import json
import urllib.request
import urllib.error

API_URL = "http://127.0.0.1:5000/asistencia"

# --- Función para cargar datos en el visor ---
def cargar_datos():
    """Consulta la API y llena la tabla con los registros previos."""
    # Limpiar la tabla antes de cargar
    for i in tabla.get_children():
        tabla.delete(i)
    
    try:
        # Hacemos una petición GET a la nueva ruta
        url_listar = "http://127.0.0.1:5000/asistentes"
        with urllib.request.urlopen(url_listar) as respuesta:
            if respuesta.status == 200:
                datos = json.loads(respuesta.read().decode())
                for registro in datos:
                    tabla.insert("", "end", values=(registro['id'], registro['nombre'], registro['email']))
    except Exception as e:
        print(f"No se pudieron cargar los datos iniciales: {e}")



def enviar_datos():
    nombre = entry_nombre.get().strip()
    email = entry_email.get().strip()
    
    if not nombre or not email:
        messagebox.showwarning("Campos incompletos", "Por favor completa todo.")
        return
    
    datos = {"nombre": nombre, "email": email}
    data_json = json.dumps(datos).encode('utf-8')
    
    try:
        req = urllib.request.Request(
            API_URL, 
            data=data_json, 
            headers={'Content-Type': 'application/json'}, 
            method='POST'
        )
        with urllib.request.urlopen(req) as respuesta:
            if respuesta.status == 201:
                resultado = json.loads(respuesta.read().decode())
                # Insertar directamente en el visor (DataGrid)
                tabla.insert("", "end", values=(resultado['id'], nombre, email))
                
                messagebox.showinfo("Éxito", "Asistente registrado con éxito.")
                entry_nombre.delete(0, tk.END)
                entry_email.delete(0, tk.END)

    # --- AQUÍ VAN LOS EXCEPT ESPECÍFICOS ---
    except urllib.error.HTTPError as e:
        # Capturamos errores enviados por Flask (como el 400 del email duplicado)
        try:
            error_data = json.loads(e.read().decode())
            mensaje_servidor = error_data.get('error', 'Error desconocido')
            
            if e.code == 400:
                # Caso específico: Email ya registrado
                messagebox.showwarning("Atención", f"No se pudo registrar: {mensaje_servidor}")
            else:
                messagebox.showerror("Error del Servidor", f"Código {e.code}: {mensaje_servidor}")
        except:
            messagebox.showerror("Error", f"Error HTTP: {e.code}")

    except urllib.error.URLError:
        # Error cuando el servidor Flask no está encendido
        messagebox.showerror("Error de Conexión", "No se pudo conectar con la API.\n¿Iniciaste el servidor app.py?")

    except Exception as e:
        # Cualquier otro error inesperado
        messagebox.showerror("Error Inesperado", f"Ocurrió algo extraño: {str(e)}")
# --- Interfaz gráfica ---
ventana = tk.Tk()
ventana.title("Registro y Visor de Asistencia")
ventana.geometry("500x500") # Más grande para que entre la tabla

# (Tus etiquetas y campos de texto igual que antes...)
tk.Label(ventana, text="Nombre completo:").pack(pady=5)
entry_nombre = tk.Entry(ventana, width=40)
entry_nombre.pack()

tk.Label(ventana, text="Correo electrónico:").pack(pady=5)
entry_email = tk.Entry(ventana, width=40)
entry_email.pack()

btn_enviar = tk.Button(ventana, text="Registrar asistencia", command=enviar_datos, bg="#4CAF50", fg="white")
btn_enviar.pack(pady=20)

# --- EL DATAGRID (Treeview) ---
tk.Label(ventana, text="Registros en el sistema:", font=("Arial", 10, "bold")).pack()

columnas = ("ID", "Nombre", "Email")
tabla = ttk.Treeview(ventana, columns=columnas, show="headings", height=8)

# Definir encabezados
tabla.heading("ID", text="ID")
tabla.heading("Nombre", text="Nombre")
tabla.heading("Email", text="Email")

# Ajustar ancho de columnas
tabla.column("ID", width=50, anchor="center")
tabla.column("Nombre", width=200)
tabla.column("Email", width=200)

tabla.pack(pady=10, padx=10)

cargar_datos()  # <--- Esta línea hace que aparezcan los registros viejos al abrir
ventana.mainloop()
