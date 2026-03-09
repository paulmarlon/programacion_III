class Calculadora:
    def __init__(self,v1,v2):
        self.valor1=v1
        self.valor2=v2
    def sumar(self,a=None,b=None):
        if a is not None and b is not None:
            return a + b
        return self.valor1 + self.valor2
    def restar(self):
        return self.valor1-self.valor2
    def multiplicar(self,a=None,b=None):
        if a is not None and b is not None:
            return a * b
        return self.valor1 * self.valor2
    def dividir(self):
        return self.valor1/self.valor2
#uso
#calc=Calculadora(10,5)
#print(calc.sumar())