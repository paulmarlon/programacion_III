import tkinter as tk  # Biblioteca principal para la interfaz gráfica (GUI)
from tkinter import messagebox  # Para mostrar ventanas emergentes de error
import math  # Para funciones matemáticas avanzadas como la raíz cuadrada

class CalculadoraAvanzada:
    def __init__(self):
        """Constructor: Configura la ventana principal y las variables iniciales"""
        self.ventana = tk.Tk()  # Crea la base de la ventana
        self.ventana.title("Calculadora Python")  # Título de la parte superior
        self.ventana.geometry("350x500")  # Tamaño inicial (Ancho x Alto)
        self.ventana.resizable(False, False)  # Evita que el usuario cambie el tamaño
        self.ventana.configure(bg='#1C1C1C')  # Color de fondo oscuro (estilo moderno)

        # VARIABLES DE CONTROL
        self.numero1 = 0  # Guarda el primer número de una operación (ej: el 5 en 5+2)
        self.operador = None  # Guarda el símbolo de la operación (+, -, *, /)
        
        # LLAMADA A MÉTODOS DE CONSTRUCCIÓN
        self.crear_display()  # Dibuja la pantalla de resultados
        self.crear_botones()  # Dibuja el teclado numérico y de funciones

    def crear_display(self):
        """Configura la pantalla donde se ven los números"""
        # El 'frame' actúa como un contenedor para el display
        frame_display = tk.Frame(self.ventana, bg='#1C1C1C')
        frame_display.pack(pady=20, padx=10, fill='both')

        # 'Entry' es el campo de texto. Usamos 'readonly' para que solo se escriba vía botones
        self.display = tk.Entry(
            frame_display,
            font=("Arial", 28),
            justify="right",  # Alinea el texto a la derecha
            bg='#2C2C2C',
            fg='black',
            relief=tk.FLAT,  # Sin bordes resaltados para un look plano
            state='readonly'
        )
        self.display.pack(fill='both', ipady=15)  # ipady añade relleno interno vertical
        self.actualizar_display("0")  # Valor por defecto al iniciar

    def actualizar_display(self, valor):
        """Método auxiliar para escribir en el display bloqueado"""
        self.display.config(state='normal')  # Desbloquea para escribir
        self.display.delete(0, tk.END)       # Borra lo que haya
        self.display.insert(0, valor)        # Inserta el nuevo valor
        self.display.config(state='readonly') # Bloquea de nuevo

    def agregar_numero(self, numero):
        """Concatena los números presionados en la pantalla"""
        actual = self.display.get()
        # Si hay un "0" inicial o un "Error", lo reemplazamos por el nuevo número
        if actual == "0" or actual == "Error":
            self.actualizar_display(str(numero))
        else:
            self.actualizar_display(actual + str(numero))

    def agregar_punto(self):
        """Añade un punto decimal asegurando que no existan duplicados"""
        actual = self.display.get()
        if '.' not in actual:
            self.actualizar_display(actual + ".")

    # --- LÓGICA DEL RETO (Funciones Especiales) ---
    
    def borrar_ultimo(self):
        """Elimina el último carácter (Botón ←)"""
        actual = self.display.get()
        if actual != "0" and actual != "Error":
            nuevo = actual[:-1]  # Técnica de 'slicing' para quitar el último carácter
            # Si al borrar queda vacío o solo el signo menos, ponemos "0"
            if nuevo == "" or nuevo == "-":
                self.actualizar_display("0")
            else:
                self.actualizar_display(nuevo)

    def operacion_instantanea(self, tipo):
        """Calcula raíz, cuadrado o inverso inmediatamente sin usar el '='"""
        try:
            valor = float(self.display.get())
            if tipo == 'sqrt':
                if valor < 0: raise ValueError("Raíz negativa") # Error personalizado
                resultado = math.sqrt(valor)
            elif tipo == 'sqr':
                resultado = valor ** 2  # Eleva al cuadrado
            elif tipo == 'inv':
                if valor == 0: raise ZeroDivisionError # No existe 1/0
                resultado = 1 / valor
            
            self.mostrar_resultado_formateado(resultado)
        except ValueError:
            messagebox.showerror("Error", "❌ No se puede calcular raíz de negativo")
        except ZeroDivisionError:
            messagebox.showerror("Error", "❌ No se puede dividir entre cero")
        except Exception:
            messagebox.showerror("Error", "❌ Operación inválida")

    # --- LÓGICA DE OPERACIONES BÁSICAS ---

    def seleccionar_operador(self, op):
        """Guarda el primer número y el operador, luego limpia pantalla para el segundo"""
        try:
            self.numero1 = float(self.display.get())
            self.operador = op
            self.actualizar_display("0")
        except:
            self.limpiar()

    def calcular(self):
        """Ejecuta la operación aritmética final (Botón =)"""
        try:
            if self.operador is None: return # Si no hay operación pendiente, no hace nada
            
            numero2 = float(self.display.get())
            if self.operador == '+': resultado = self.numero1 + numero2
            elif self.operador == '-': resultado = self.numero1 - numero2
            elif self.operador == '*': resultado = self.numero1 * numero2
            elif self.operador == '/':
                if numero2 == 0: raise ZeroDivisionError
                resultado = self.numero1 / numero2
            
            self.mostrar_resultado_formateado(resultado)
            self.operador = None # Resetea el operador tras terminar
        except ZeroDivisionError:
            messagebox.showerror("Error", "❌ No se puede dividir entre cero")
            self.limpiar()
        except:
            messagebox.showerror("Error", "❌ Error en el cálculo")
            self.limpiar()

    def mostrar_resultado_formateado(self, resultado):
        """Muestra el resultado quitando el .0 si es un número entero"""
        if resultado == int(resultado):
            self.actualizar_display(str(int(resultado)))
        else:
            # Redondeamos a 8 decimales para evitar errores de precisión de punto flotante
            self.actualizar_display(str(round(resultado, 8)))

    def limpiar(self):
        """Reset total (Botón AC)"""
        self.numero1 = 0
        self.operador = None
        self.actualizar_display("0")

    def porcentaje(self):
        """Convierte el número actual a su valor centesimal"""
        try:
            valor = float(self.display.get())
            self.mostrar_resultado_formateado(valor / 100)
        except: pass

    def cambiar_signo(self):
        """Multiplica por -1 (Botón +/-)"""
        try:
            valor = float(self.display.get())
            self.mostrar_resultado_formateado(valor * -1)
        except: pass

    def crear_botones(self):
        """Crea la cuadrícula de botones de forma eficiente"""
        # Diccionario de colores para el diseño
        colores = {
            'bg': '#1C1C1C', # Fondo
            'num': '#505050', # Botones numéricos (Gris oscuro)
            'op': '#FF9500',  # Botones de operación (Naranja)
            'esp': '#D4D4D2'  # Botones especiales (Gris claro)
        }

        frame_botones = tk.Frame(self.ventana, bg=colores['bg'])
        frame_botones.pack(pady=10, padx=10, fill='both', expand=True)

        # Configura las 6 filas y 4 columnas para que se expandan uniformemente
        for i in range(6): frame_botones.grid_rowconfigure(i, weight=1)
        for i in range(4): frame_botones.grid_columnconfigure(i, weight=1)

        # ESTRUCTURA DE LA CALCULADORA
        # Formato: [Texto, Fila, Columna, Color, Comando]
        botones = [
            ['AC', 0, 0, colores['esp'], self.limpiar],
            ['←', 0, 1, colores['esp'], self.borrar_ultimo],
            ['%', 0, 2, colores['esp'], self.porcentaje],
            ['/', 0, 3, colores['op'], lambda: self.seleccionar_operador('/')],
            
            ['√', 1, 0, colores['num'], lambda: self.operacion_instantanea('sqrt')],
            ['x²', 1, 1, colores['num'], lambda: self.operacion_instantanea('sqr')],
            ['1/x', 1, 2, colores['num'], lambda: self.operacion_instantanea('inv')],
            ['*', 1, 3, colores['op'], lambda: self.seleccionar_operador('*')],

            ['7', 2, 0, colores['num'], lambda: self.agregar_numero('7')],
            ['8', 2, 1, colores['num'], lambda: self.agregar_numero('8')],
            ['9', 2, 2, colores['num'], lambda: self.agregar_numero('9')],
            ['-', 2, 3, colores['op'], lambda: self.seleccionar_operador('-')],

            ['4', 3, 0, colores['num'], lambda: self.agregar_numero('4')],
            ['5', 3, 1, colores['num'], lambda: self.agregar_numero('5')],
            ['6', 3, 2, colores['num'], lambda: self.agregar_numero('6')],
            ['+', 3, 3, colores['op'], lambda: self.seleccionar_operador('+')],

            ['1', 4, 0, colores['num'], lambda: self.agregar_numero('1')],
            ['2', 4, 1, colores['num'], lambda: self.agregar_numero('2')],
            ['3', 4, 2, colores['num'], lambda: self.agregar_numero('3')],
            ['=', 4, 3, colores['op'], self.calcular],

            ['+/-', 5, 0, colores['num'], self.cambiar_signo],
            ['0', 5, 1, colores['num'], lambda: self.agregar_numero('0')],
            ['.', 5, 2, colores['num'], self.agregar_punto],
            ['C', 5, 3, colores['esp'], lambda: self.actualizar_display("0")]
        ]

        # Bucle para dibujar cada botón en la cuadrícula (grid)
        for texto, fila, columna, color, comando in botones:
            btn = tk.Button(
                frame_botones, text=texto, font=("Arial", 14, "bold"),
                bg=color, 
                # Si el color es gris claro, el texto es negro; si no, es blanco
                fg='white' if color != colores['esp'] else 'black',
                relief=tk.FLAT, 
                command=comando
            )
            # 'sticky=nsew' hace que el botón llene todo el espacio de su celda
            btn.grid(row=fila, column=columna, sticky='nsew', padx=2, pady=2)

    def ejecutar(self):
        """Arranca el bucle principal de la aplicación"""
        self.ventana.mainloop()

# PUNTO DE ENTRADA DEL PROGRAMA
if __name__ == "__main__":
    CalculadoraAvanzada().ejecutar()