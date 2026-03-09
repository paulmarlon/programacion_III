import math
from calculadora_basica import Calculadora

class CalculadoraCientifica(Calculadora): 
    def __init__(self, v1, v2=0):
        # Llamamos al constructor del padre (Calculadora)
        super().__init__(v1, v2)

    def seno(self):
        return math.sin(math.radians(self.valor1))

    def coseno(self):
        return math.cos(math.radians(self.valor1))

    def tangente(self): # Agregados los :
        return math.tan(math.radians(self.valor1))

    def logaritmo(self): # Agregados los :
        # El logaritmo se aplica al valor directo, no a los radianes
        return math.log10(self.valor1)

    def raiz(self): # Agregados los :
        return math.sqrt(self.valor1)

    def potenciar(self, base=None, exponente=None):
        if base is not None and exponente is not None:
            return base ** exponente  
        return self.valor1 ** self.valor2

#cientifica = CalculadoraCientifica(90, 2) 

#print("--- Resultados de Funciones Científicas ---")
#print(f"Seno de 90:        {cientifica.seno():.2f}")
#print(f"Coseno de 90:      {cientifica.coseno():.2f}")
#print(f"Logaritmo de 90:   {cientifica.logaritmo():.2f}")
#print(f"Tangente de 90:    {cientifica.tangente()}")
#print(f"Raíz de 90:        {cientifica.raiz()}")
#print(f"90 elevado a la 2: {cientifica.potenciar()}")
#print("\n--- Resultados de Funciones Heredadas (Básicas) ---")
#print(f"Suma:              {cientifica.sumar()}")
#print(f"Resta:             {cientifica.restar()}")
#print(f"Multiplicación:    {cientifica.multiplicar()}")
#print(f"División:          {cientifica.dividir()}")