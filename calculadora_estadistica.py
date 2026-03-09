import math
from calculadora_basica import Calculadora
class CalculadoraEstadistica(Calculadora): 
    def __init__(self, v1=0, v2=0):
        # Llamamos al constructor del padre (Calculadora)
        super().__init__(v1, v2)
    def media(self,lista):
        if not lista:
            return 0
        return sum(lista) / len(lista)

    def mediana(self,lista):
        if not lista:
            return 0
        lista_ordenada = sorted(lista)
        n = len(lista_ordenada)
        mitad =n//2

        if n % 2 == 0:
            return (lista_ordenada[mitad] + lista_ordenada[mitad-1]) / 2
        else:
            return lista_ordenada[mitad]
    def desviacion_estandar(self, lista):
        #Validación: Necesitamos al menos 2 números para hablar de dispersión
        if len(lista) < 2:
            return 0
        #Obtenemos el promedio usando el método que ya creamos
        media = self.media(lista)
        #Calculamos la suma de los cuadrados de las diferencias
        sumatoria = 0
        for x in lista:
            diferencia = x - media  # <-- Cambiado 'm' por 'media'
            cuadrado = diferencia ** 2
            sumatoria = sumatoria + cuadrado
            #Calculamos la varianza (el promedio de esos cuadrados)
        varianza = sumatoria / len(lista)
        #La desviación es la raíz cuadrada de la varianza
        return math.sqrt(varianza)
#est = CalculadoraEstadistica()
# Definimos una lista de datos (por ejemplo, notas de un examen)
#mis_datos = [55, 70, 85, 90, 45, 100, 70]
#promedio = est.media(mis_datos)
#print(f"El promedio es: {promedio}") 
# Suma todo y divide entre 7 elementos.
#centro = est.mediana(mis_datos)
#print(f"La mediana es: {centro}")
# El código ordenará los números: [45, 55, 70, 70, 85, 90, 100]
# Y te devolverá el 70, que está justo al medio.
#dispersion = est.desviacion_estandar(mis_datos)
#print(f"La desviación estándar es: {dispersion:.2f}")
# Esto te dirá qué tan alejadas están las notas del promedio.
# Usando métodos de la clase padre (Calculadora)
#suma_rapida = est.sumar() # Sumará v1 + v2 (que por defecto son 0, 0)
#print(suma_rapida)