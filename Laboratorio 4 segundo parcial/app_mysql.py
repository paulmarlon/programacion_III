import mysql.connector 
from mysql.connector import Error
import tkinter as tk
from tkinter import ttk, messagebox

# =========================================================
# 1. CAPA DE CONEXIÓN (MySQL)
# =========================================================
class ConexionMySQL:
    def __init__(self):
        self.config = {
            'host': 'localhost',
            'user': 'root',          
            'password': '',          # Cambia esto si tienes contraseña en MySQL
            'database': 'usuarios_db'    # Asegúrate de que exista en phpMyAdmin
        }
        self.conn = None

    def conectar(self):
        try:
            self.conn = mysql.connector.connect(**self.config)
            return self.conn
        except Error as e:
            messagebox.showerror("Error de Conexión", f"No se pudo conectar a MySQL: {e}")
            return None

    def desconectar(self):
        if self.conn and self.conn.is_connected():
            self.conn.close()

    def ejecutar_consulta(self, sql, params=()):
        conn = self.conectar()
        if conn:
            try:
                cursor = conn.cursor()
                cursor.execute(sql, params)
                conn.commit()
                return cursor.lastrowid
            except Error as e:
                print(f"Error en consulta: {e}")
                return None
            finally:
                self.desconectar()

    def obtener_resultados(self, sql, params=()):
        conn = self.conectar()
        if conn:
            try:
                cursor = conn.cursor()
                cursor.execute(sql, params)
                return cursor.fetchall()
            except Error as e:
                print(f"Error en consulta: {e}")
                return []
            finally:
                self.desconectar()

# =========================================================
# 2. CAPA DAO (Lógica de Datos)
# =========================================================
class TareaDAO:
    def __init__(self, conexion):
        self.conexion = conexion

    def crear(self, nombre, descripcion, estado="pendiente"):
        sql = "INSERT INTO tareas (nombre, descripcion, estado) VALUES (%s, %s, %s)"
        return self.conexion.ejecutar_consulta(sql, (nombre, descripcion, estado))

    def listar(self):
        sql = "SELECT id, nombre, descripcion, estado FROM tareas"
        return self.conexion.obtener_resultados(sql)

    def actualizar(self, id_tarea, nombre, descripcion, estado):
        sql = "UPDATE tareas SET nombre=%s, descripcion=%s, estado=%s WHERE id=%s"
        return self.conexion.ejecutar_consulta(sql, (nombre, descripcion, estado, id_tarea))

    def eliminar(self, id_tarea):
        sql = "DELETE FROM tareas WHERE id=%s"
        return self.conexion.ejecutar_consulta(sql, (id_tarea,))


# =========================================================
# 3. INTERFAZ GRÁFICA (Tkinter)
# =========================================================
class AppTareas:
    def __init__(self, root):
        self.root = root
        self.root.title("Gestor de Tareas - MySQL")
        
        # CORRECCIÓN: Usar ConexionMySQL en lugar de ConexionSQLite
        self.dao = TareaDAO(ConexionMySQL())

        self.id_var = tk.StringVar()
        self.nombre_var = tk.StringVar()
        self.desc_var = tk.StringVar()
        self.estado_var = tk.StringVar(value="pendiente")

        self._crear_widgets()
        self.listar_tareas()

    def _crear_widgets(self):
        frame_form = tk.LabelFrame(self.root, text="Datos de Tarea", padx=10, pady=10)
        frame_form.pack(fill="x", padx=10, pady=5)

        tk.Label(frame_form, text="Nombre:").grid(row=0, column=0, sticky="e", pady=2)
        tk.Entry(frame_form, textvariable=self.nombre_var, width=35).grid(row=0, column=1, pady=2)

        tk.Label(frame_form, text="Descripción:").grid(row=1, column=0, sticky="e", pady=2)
        tk.Entry(frame_form, textvariable=self.desc_var, width=35).grid(row=1, column=1, pady=2)

        tk.Label(frame_form, text="Estado:").grid(row=2, column=0, sticky="e", pady=2)
        combo = ttk.Combobox(frame_form, textvariable=self.estado_var, values=["pendiente", "completada"], state="readonly", width=32)
        combo.grid(row=2, column=1, pady=2)

        frame_botones = tk.Frame(frame_form)
        frame_botones.grid(row=3, column=0, columnspan=2, pady=10)
        
        tk.Button(frame_botones, text="Agregar", command=self.agregar_tarea, bg="#d4edda").pack(side="left", padx=5)
        tk.Button(frame_botones, text="Actualizar", command=self.actualizar_tarea, bg="#fff3cd").pack(side="left", padx=5)
        tk.Button(frame_botones, text="Eliminar", command=self.eliminar_tarea, bg="#f8d7da").pack(side="left", padx=5)
        tk.Button(frame_botones, text="Limpiar", command=self.limpiar_form).pack(side="left", padx=5)

        self.tree = ttk.Treeview(self.root, columns=("ID", "Nombre", "Descripción", "Estado"), show="headings")
        self.tree.heading("ID", text="ID")
        self.tree.heading("Nombre", text="Nombre")
        self.tree.heading("Descripción", text="Descripción")
        self.tree.heading("Estado", text="Estado")
        
        self.tree.column("ID", width=40, anchor="center")
        self.tree.column("Nombre", width=150)
        self.tree.column("Descripción", width=200)
        self.tree.column("Estado", width=100, anchor="center")
        
        self.tree.pack(fill="both", expand=True, padx=10, pady=5)
        self.tree.bind("<<TreeviewSelect>>", self.on_select)

    def listar_tareas(self):
        for item in self.tree.get_children():
            self.tree.delete(item)
        res = self.dao.listar()
        if res:
            for tarea in res:
                self.tree.insert("", "end", values=tarea)

    def agregar_tarea(self):
        nombre = self.nombre_var.get().strip()
        if not nombre:
            messagebox.showwarning("Validación", "El nombre es obligatorio")
            return
        self.dao.crear(nombre, self.desc_var.get(), self.estado_var.get())
        self.listar_tareas()
        self.limpiar_form()

    def actualizar_tarea(self):
        if not self.id_var.get():
            messagebox.showwarning("Selección", "Seleccione una tarea de la lista")
            return
        self.dao.actualizar(int(self.id_var.get()), self.nombre_var.get(), 
                            self.desc_var.get(), self.estado_var.get())
        self.listar_tareas()
        self.limpiar_form()

    def eliminar_tarea(self):
        if not self.id_var.get():
            messagebox.showwarning("Selección", "Seleccione una tarea para eliminar")
            return
        if messagebox.askyesno("Confirmar", "¿Seguro que desea eliminar esta tarea?"):
            self.dao.eliminar(int(self.id_var.get()))
            self.listar_tareas()
            self.limpiar_form()

    def limpiar_form(self):
        self.id_var.set("")
        self.nombre_var.set("")
        self.desc_var.set("")
        self.estado_var.set("pendiente")

    def on_select(self, event):
        seleccion = self.tree.selection()
        if seleccion:
            valores = self.tree.item(seleccion[0], "values")
            self.id_var.set(valores[0])
            self.nombre_var.set(valores[1])
            self.desc_var.set(valores[2])
            self.estado_var.set(valores[3])

# =========================================================
# 4. PUNTO DE ENTRADA
# =========================================================
if __name__ == "__main__":
    root = tk.Tk()
    app = AppTareas(root)
    root.mainloop()