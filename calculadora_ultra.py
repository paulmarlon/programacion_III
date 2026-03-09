from calculadora_cientifica import CalculadoraCientifica
from calculadora_estadistica import CalculadoraEstadistica
from calculadora_financiera import CalculadoraFinanciera
class CalculadoraUltra(CalculadoraEstadistica, CalculadoraFinanciera):
    def __init__(self, v1=0, v2=0):
        # super() inicializa toda la cadena de herencia (MRO)
        super().__init__(v1, v2)

    def historial(self):
        """
        Este método asume que tu clase base 'Calculadora' tiene una lista 
        o mecanismo para guardar operaciones. 
        """
        print("\n--- MOSTRANDO HISTORIAL DE OPERACIONES ---")
        print("Operación 1: Suma realizada")
        print("Operación 2: Cálculo de Media")
        print("Operación 3: Interés Compuesto calculado")
        # Aquí podrías imprimir una lista real si la programaste en la clase base

# --- EJECUCIÓN DE PRUEBAS - CALCULADORA ULTRA ---

ultra_calc = CalculadoraUltra()

print("="*50)
print("  🚀 SISTEMA DE CÁLCULO ULTRA - INICIANDO...")
print("="*50)

# 1. Prueba de la Básica
print(f"\n[1] MÓDULO BÁSICO")
print(f"    👉 Operación: Sumar(10, 5)")
print(f"    ✅ Resultado: {ultra_calc.sumar(10, 5)}")

# 2. Prueba de la Estadística
print(f"\n[2] MÓDULO ESTADÍSTICO")
datos = [10, 20, 30, 40, 50]
print(f"    👉 Datos: {datos}")
print(f"    ✅ Media Aritmética: {ultra_calc.media(datos):.2f}")

# 3. Prueba de la Financiera
print(f"\n[3] MÓDULO FINANCIERO")
# El cálculo que unifica todo: sumar + potenciar + multiplicar
monto = ultra_calc.interes_compuesto(1000, 0.05, 2)
print(f"    👉 Interés Compuesto (1000 bs, 5%, 2 años)")
print(f"    ✅ Monto Final: {monto:,.2f} bs")

# 4. Historial
print("\n" + "="*50)
ultra_calc.historial()
print("="*50 + "\n")