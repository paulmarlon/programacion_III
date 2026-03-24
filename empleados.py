class Empleado:
    def __init__(self,nombre,edad,salario_base):
        #publico
        self.nombre=nombre
        self.edad=edad
        #protegido
        self._salario_base=salario_base
    def calcular_salario(self):
        "metodo base sera sobreescrito"
        return self._salario_base
    def mostrar_info(self):
        "muestra informacion basica"
        return f"Empleado:{self.nombre}, Edad:{self.edad},Salario:${self.calcular_salario():.2f}"
"""
if __name__=="__main__":
    emp=Empleado("Juan",30,3000)
    print(emp.mostrar_info())
    print(f"Salario calculado: ${emp.calcular_salario()}")
"""
class Gerente(Empleado):
    """Gerente - Hereda de Empleado"""
    def __init__(self, nombre, edad, salario_base, bono, departamento):
        # Llamar al constructor de la clase padre
        super().__init__(nombre, edad, salario_base)
        # Atributos específicos de Gerente
        self.bono = bono
        self.departamento = departamento
    def calcular_salario(self):
        """SOBRESCRITURA: El salario del gerente incluye el bono"""
        return self._salario_base + self.bono
    def mostrar_info(self):
        """SOBRESCRITURA: Mostrar información específica del gerente"""
        return (f"Gerente: {self.nombre}, Edad: {self.edad}, "
                f"Departamento: {self.departamento}, "
                f"Salario: ${self.calcular_salario():.2f} "
                f"(Base: ${self._salario_base} + Bono: ${self.bono})")
# Probamos las clases
"""
if __name__ == "__main__":
    print("\n--- Probando Gerente ---")
    gerente = Gerente("Monica", 45, 5000, 2000, "Tecnología")
    print(gerente.mostrar_info())
    print(f"Salario calculado: ${gerente.calcular_salario()}")
    print("\n--- Comparando con Empleado ---")
    empleado = Empleado("Juan", 30, 3000)
    print(empleado.mostrar_info())
    print(gerente.mostrar_info())
"""
class Desarrollador(Empleado):
    """Desarrollador - Hereda de Empleado"""
    def __init__(self, nombre, edad, salario_base, lenguaje, horas_extra=0, pago_hora=50):
        super().__init__(nombre, edad, salario_base)
        # Atributos específicos
        self.lenguaje = lenguaje
        self.horas_extra = horas_extra
        self.pago_hora = pago_hora
    def calcular_salario(self):
        """SOBRESCRITURA: El desarrollador gana extra por horas extra"""
        extra = self.horas_extra * self.pago_hora
        return self._salario_base + extra
    def mostrar_info(self):
        """SOBRESCRITURA: Mostrar información específica"""
        extra = self.horas_extra * self.pago_hora
        return (f"Desarrollador: {self.nombre}, Edad: {self.edad}, "
                f"Lenguaje: {self.lenguaje}, "
                f"Salario: ${self.calcular_salario():.2f} "
                f"(Base: ${self._salario_base} + "
                f"HE: {self.horas_extra} x ${self.pago_hora} = ${extra})")

# Probamos las tres clases
def mostrar_nomina(empleados):
    """FUNCIÓN QUE DEMUESTRA POLIMORFISMO"""
    print("\n" + "="*60)
    print("NÓMINA DE EMPLEADOS")
    print("="*60)
    total_nomina = 0
    for empleado in empleados:
        # POLIMORFISMO: Aunque todos son tipos diferentes,
        # todos entienden los mismos métodos
        print(empleado.mostrar_info())
        total_nomina += empleado.calcular_salario()
    print("-"*60)
    print(f"TOTAL NÓMINA: ${total_nomina:.2f}")
    print("="*60)
if __name__ == "__main__":

    # Creamos una lista con diferentes tipos de empleados
    empleados = [
        Empleado("Juan Pérez", 30, 3000),
        Gerente("Ana Gómez", 45, 5000, 2000, "Tecnología"),
        Desarrollador("Carlos López", 28, 3500, "Python", 10),
        Desarrollador("María Rodríguez", 32, 4000, "Java"),
        Gerente("Roberto Sánchez", 50, 8000, 3500, "Ventas")
    ]
mostrar_nomina(empleados)
# Demostración adicional: cada objeto usa su propio método
print("\n" + "="*60)
print("DEMOSTRACIÓN DE POLIMORFISMO")
print("="*60)
print("Cada tipo calcula su salario de manera diferente:\n")
for emp in empleados:
    # El mismo método, comportamiento diferente según el tipo
    print(f"{emp.nombre:15} ({type(emp).__name__:12}) → ${emp.calcular_salario():.2f}")

"""
if __name__ == "__main__":
    print("\n--- Probando Desarrollador ---")
    dev = Desarrollador("Carlos", 28, 3500, "Python", horas_extra=10)
    print(dev.mostrar_info())
    print(f"Salario calculado: ${dev.calcular_salario()}")
    print("\n--- Todos los tipos ---")
    empleados = [
        Empleado("Juan", 30, 3000),
        Gerente("Ana", 45, 5000, 2000, "TI"),
        Desarrollador("Carlos", 28, 3500, "Python", 10),
        Desarrollador("Maria", 32, 4000, "Java")
    ]
    for emp in empleados:
        print(emp.mostrar_info())
"""
def mostrar_menu():
    """Muestra las opciones disponibles"""
    print("\n" + "="*50)
    print("SISTEMA DE GESTIÓN DE EMPLEADOS")
    print("="*50)
    print("1. Agregar empleado regular")
    print("2. Agregar gerente")
    print("3. Agregar desarrollador")
    print("4. Ver todos los empleados")
    print("5. Calcular salario de un empleado")
    print("6. Ver total de nómina")
    print("7. Salir")
    print("-"*50)

def agregar_empleado(empleados):
    """Agrega un empleado regular"""
    print("\n--- NUEVO EMPLEADO REGULAR ---")
    nombre = input("Nombre: ")
    edad = int(input("Edad: "))
    salario = float(input("Salario base: $"))
    nuevo = Empleado(nombre, edad, salario)
    empleados.append(nuevo)
    print(f"✓ Empleado {nombre} agregado exitosamente")
    return empleados

def agregar_gerente(empleados):
    """Agrega un gerente"""
    print("\n--- NUEVO GERENTE ---")
    nombre = input("Nombre: ")
    edad = int(input("Edad: "))
    salario = float(input("Salario base: $"))
    bono = float(input("Bono: $"))
    depto = input("Departamento: ")
    nuevo = Gerente(nombre, edad, salario, bono, depto)
    empleados.append(nuevo)
    print(f"✓ Gerente {nombre} agregado exitosamente")
    return empleados

def agregar_desarrollador(empleados):
    """Agrega un desarrollador"""
    print("\n--- NUEVO DESARROLLADOR ---")
    nombre = input("Nombre: ")
    edad = int(input("Edad: "))
    salario = float(input("Salario base: $"))
    lenguaje = input("Lenguaje principal: ")
    horas = int(input("Horas extra (0 si no tiene): "))
    nuevo = Desarrollador(nombre, edad, salario, lenguaje, horas)
    empleados.append(nuevo)
    print(f"✓ Desarrollador {nombre} agregado exitosamente")
    return empleados

def ver_empleados(empleados):
    """Muestra todos los empleados"""
    if not empleados:
        print("\n⚠ No hay empleados registrados")
        return
    print("\n" + "="*60)
    print("LISTA DE EMPLEADOS")
    print("="*60)
    for i, emp in enumerate(empleados, 1):
        print(f"{i}. {emp.mostrar_info()}")
    print("="*60)
def calcular_salario_individual(empleados):
    """Calcula el salario de un empleado específico"""
    if not empleados:
        print("\n⚠ No hay empleados registrados")
        return
    print("\n--- SELECCIONE EMPLEADO ---")
    for i, emp in enumerate(empleados, 1):
        print(f"{i}. {emp.nombre} ({type(emp).__name__})")
    try:
        opcion = int(input("\nNúmero del empleado: ")) - 1
        if 0 <= opcion < len(empleados):
            emp = empleados[opcion]
            print("\n" + "-"*40)
            print(emp.mostrar_info())
            print(f"Salario calculado: ${emp.calcular_salario():.2f}")
            print("-"*40)
        else:
            print("⚠ Opción inválida")
    except ValueError:
        print("⚠ Por favor ingrese un número válido")
def ver_total_nomina(empleados):
    """Muestra el total de la nómina"""
    if not empleados:
        print("\n⚠ No hay empleados registrados")
        return
    total = sum(emp.calcular_salario() for emp in empleados)
    print("\n" + "="*50)
    print("RESUMEN DE NÓMINA")
    print("="*50)
    print(f"Total empleados: {len(empleados)}")
    print(f"Total nómina: ${total:.2f}")
    print("="*50)
if __name__ == "__main__":
    # Lista para almacenar empleados
    empleados = []
    # Agregar algunos empleados de ejemplo
    empleados.append(Empleado("Juan Pérez", 30, 3000))
    empleados.append(Gerente("Ana Gómez", 45, 5000, 2000, "Tecnología"))
    empleados.append(Desarrollador("Carlos López", 28, 3500, "Python", 10))
    print("\n🎯 SISTEMA DE EMPLEADOS CON HERENCIA Y POLIMORFISMO")
    print("📌 Empleados de ejemplo cargados")
    while True:
        mostrar_menu()
        opcion = input("Seleccione una opción: ")
        if opcion == "1":
            empleados = agregar_empleado(empleados)
        elif opcion == "2":
            empleados = agregar_gerente(empleados)
        elif opcion == "3":
            empleados = agregar_desarrollador(empleados)
        elif opcion == "4":
            ver_empleados(empleados)
        elif opcion == "5":
            calcular_salario_individual(empleados)
        elif opcion == "6":
            ver_total_nomina(empleados)
        elif opcion == "7":
            print("\n👋 ¡Hasta luego!")
            break
        else:
            print("\n⚠ Opción inválida. Intente nuevamente.")


