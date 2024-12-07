import cmath

class EcuacionCuadratica:
    def __init__(self, a, b, c):
        """
        Inicializa los coeficientes de la ecuación cuadrática.
        """
        self.a = a
        self.b = b
        self.c = c

    def calcular_discriminante(self):
        """
        Calcula el discriminante de la ecuación cuadrática: b^2 - 4ac.
        """
        return self.b**2 - 4*self.a*self.c

    def calcular_raices(self):
        """
        Calcula y devuelve las raíces de la ecuación cuadrática.
        Maneja raíces reales e imaginarias.
        """
        if self.a == 0:
            raise ValueError("El coeficiente 'a' no puede ser cero, ya que no sería una ecuación cuadrática.")
        
        discriminante = self.calcular_discriminante()
        raiz1 = (-self.b + cmath.sqrt(discriminante)) / (2 * self.a)
        raiz2 = (-self.b - cmath.sqrt(discriminante)) / (2 * self.a)
        
        return raiz1, raiz2

    def mostrar_resultado(self):
        """
        Muestra las raíces y el tipo de solución de la ecuación cuadrática.
        """
        try:
            raiz1, raiz2 = self.calcular_raices()
            discriminante = self.calcular_discriminante()
            
            if discriminante > 0:
                print("Las raíces son reales y diferentes:")
            elif discriminante == 0:
                print("Las raíces son reales e iguales:")
            else:
                print("Las raíces son complejas (imaginarias):")
            
            print(f"Raíz 1: {raiz1}")
            print(f"Raíz 2: {raiz2}")
        except ValueError as e:
            print(e)

# Programa principal
def main():
    print("Cálculo de raíces de una ecuación cuadrática ax^2 + bx + c = 0")
    try:
        a = float(input("Ingrese el coeficiente a: "))
        b = float(input("Ingrese el coeficiente b: "))
        c = float(input("Ingrese el coeficiente c: "))
        
        ecuacion = EcuacionCuadratica(a, b, c)
        ecuacion.mostrar_resultado()
    except ValueError:
        print("Por favor, ingrese valores numéricos válidos.")

if __name__ == "__main__":
    main()
