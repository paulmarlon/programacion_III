import tkinter as tk  # Importamos la librería y le damos un alias corto (tk)
from tkinter import messagebox  # Importamos el módulo para mostrar alertas

# --- SECCIÓN DE LÓGICA (Funciones) ---
def saludar():
    # Muestra una ventana emergente: messagebox.showinfo("Título", "Mensaje")
    messagebox.showinfo("Saludo", "¡Hola Mundo py!")


# --- SECCIÓN DE INTERFAZ (Layout) ---
root = tk.Tk()                # Creamos la ventana principal (el contenedor base)
root.title("Mi Ventana") # Definimos el texto de la barra de título
root.geometry("400x300")      # Definimos el tamaño inicial (Ancho x Alto)


# Creamos una etiqueta (Label)
lbl = tk.Label(root, text="Bienvenido") 
# El método .pack() posiciona el elemento en la ventana
lbl.pack(pady=10) # <--- AQUÍ ESTÁ EL PADY (ESPACIADO VERTICAL)


# Creamos un botón (Button)
# 'command=saludar' vincula el clic del botón con la función definida arriba
btn = tk.Button(root, text="Saludar", command=saludar)
btn.pack(pady=10) # <--- Y AQUÍ TAMBIÉN

# El método mainloop() mantiene la ventana abierta y escuchando eventos (clics)
root.mainloop()