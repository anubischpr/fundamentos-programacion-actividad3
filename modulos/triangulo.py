from modulos.punto import Punto
import math

class Triangulo:
    """
    Representa un triángulo definido por tres puntos que forman sus vértices.

    Los métodos permiten calcular el área del triángulo, y determinar si es
    equilátero basándose en las coordenadas de los vértices.

    Atributos:
        vertice1 (Punto): Primer vértice del triángulo.
        vertice2 (Punto): Segundo vértice del triángulo.
        vertice3 (Punto): Tercer vértice del triángulo.
    """

    def __init__(self, vertice1 = Punto(), vertice2= Punto(), vertice3=Punto()):
        """
        Inicializa un Triángulo con tres vértices. Si no se proporcionan,
        se crean puntos en el origen (0, 0).

        Args:
            vertice1 (Punto, optional): Primer vértice del triángulo.
            vertice2 (Punto, optional): Segundo vértice del triángulo.
            vertice3 (Punto, optional): Tercer vértice del triángulo.
        """
        self.vertice1 = vertice1
        self.vertice2 = vertice2
        self.vertice3 = vertice3
        self.lado1 = self.vertice1.distancia(self.vertice2)
        self.lado2 = self.vertice2.distancia(self.vertice3)
        self.lado3 = self.vertice3.distancia(self.vertice1)

    def area(self):
        """
        Calcula el área del triángulo utilizando la fórmula de Herón.

        Returns:
            float: Área del triángulo.
        """
        s = (self.lado1 + self.lado2 + self.lado3)/2

        area = math.sqrt(s * (s - self.lado1) * (s - self.lado2) * (s - self.lado3))

        return area