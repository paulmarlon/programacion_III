from calculadora_cientifica import CalculadoraCientifica

# IMPORTANTE: Cambia (Calculadora) por (CalculadoraCientifica)
class CalculadoraFinanciera(CalculadoraCientifica):
    def __init__(self, v1=0, v2=0):
        super().__init__(v1, v2)

    def interes_simple(self, capital, tasa, tiempo):
        return self.multiplicar(self.multiplicar(capital, tasa), tiempo)

    def interes_compuesto(self, capital, tasa, tiempo): 
        # Ahora self.potenciar ya no dará error porque heredamos de la Científica
        monto_total = self.multiplicar(capital, self.potenciar(self.sumar(1, tasa), tiempo))
        return monto_total

    def iva(self, monto, porcentaje=13):
        return self.multiplicar(monto, porcentaje / 100)
#calc_fin = CalculadoraFinanciera()
#capital_prestamo = 10000
#interes_mensual = 0.02  # 2% expresado en decimal
#tiempo_meses = 12
#ganancia_banco = calc_fin.interes_simple(capital_prestamo, interes_mensual, tiempo_meses)
#print(f"1. INTERÉS SIMPLE:")
#print(f"   Por un préstamo de {capital_prestamo} bs, el interés total es: {ganancia_banco} bs")
#ahorro_inicial = 5000
#tasa_anual = 0.05
#años = 10
#monto_final = calc_fin.interes_compuesto(ahorro_inicial, tasa_anual, años)
#print(f"\n2. INTERÉS COMPUESTO:")
#print(f"   Tras {años} años, tus {ahorro_inicial} bs se convertirán en: {monto_final:.2f} bs")
#costo_maquina = 15000
#impuesto = calc_fin.iva(costo_maquina) # Usa el 13% por defecto que pusimos
#print(f"\n3. CÁLCULO DE IVA (Bolivia - 13%):")
#print(f"   El impuesto a pagar por la máquina es: {impuesto} bs")